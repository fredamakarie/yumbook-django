from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, path
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeCreationForm, RecipeUpdateForm

# Create your views here.

#sign up, login and logout
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'



urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]



def my_login_view(request):
    if request.method == "recipe":
        username = request.recipe["username"]
        password = request.recipe["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # start session
            return redirect("blog")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def my_logout_view(request):
    logout(request)
    return redirect("login")

#RECIPES
#Recipe list
class RecipeListView(ListView):
    model = Recipe
    template_name = 'blog/recipe_list.html'
    context_object_name = 'recipe'

#recipe detail
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blog/recipe_detail.html'

#recipe creation
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreationForm
    template_name = 'blog/recipe_form.html'
    permission_required = 'blog.add_recipe'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
#recipe edit
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'blog/recipe_form.html'
    login_required = 'blog.change_recipe'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

#recipe deletion
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'blog/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')
    login_required = 'blog.delete_recipe'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
