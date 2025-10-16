from django.urls import path, include
from .views import RecipeCreateView, RecipeListView, RecipeDetailView, RecipeDeleteView, RecipeUpdateView
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'', RecipeViewSet, basename='recipe')

urlpatterns = [
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/recipe-list/', RecipeListView.as_view(), name='recipe-list'),
    path('', include(router.urls))
]
