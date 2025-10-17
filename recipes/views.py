from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm, IngredientFormSet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets, permissions, filters
from .serializers import RecipeSerializer

# Create your views here.


#------------
# HTML VIEWS
#------------


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
        form = RecipeForm()
        formset = IngredientFormSet()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST, request.FILES)
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
    form_class = RecipeForm
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


#------------
# API VIEWS
#------------


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ingredients__item', 'category', 'title']
    ordering_fields = ['prep_time', 'cook_time', 'servings', 'title']
    ordering = ['title']  # default ordering


    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Show all recipes or only the user's recipes if authenticated
        if self.request.user.is_authenticated:
            return Recipe.objects.filter(author=self.request.user)
        return Recipe.objects.all()
