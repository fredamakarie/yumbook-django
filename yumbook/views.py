from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Recipe
from .forms import RecipeCreationForm, RecipeUpdateForm, IngredientFormSet


# -------------------
# AUTHENTICATION VIEWS
# -------------------

class SignUpView(CreateView):
    """User registration view"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def my_login_view(request):
    """Manual login (optional; you can use LoginView instead)"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("recipe-list")
        else:
            return render(request, "registration/login.html", {"error": "Invalid credentials"})

    return render(request, "registration/login.html")


def my_logout_view(request):
    logout(request)
    return redirect("login")


# -------------------
# RECIPE CRUD VIEWS
# -------------------

class RecipeListView(ListView):
    """List all recipes"""
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    """View details of a recipe"""
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, View):
    """Create recipe with ingredients"""
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def get(self, request, *args, **kwargs):
        form = RecipeCreationForm()
        formset = IngredientFormSet()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = RecipeCreationForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # optional — only if Recipe has author field
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form, 'formset': formset})


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a recipe"""
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        # Only allow editing if the user owns the recipe
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author  # only if author field exists


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author  # only if author field exists
