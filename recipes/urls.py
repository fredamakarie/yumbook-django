from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecipeCreateView,
    RecipeListView,
    RecipeDetailView,
    RecipeDeleteView,
    RecipeUpdateView,
    RecipeViewSet,
)

# --- API Router setup ---
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')

urlpatterns = [
    # ---- HTML Views ----
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

    # ---- API Routes ----
    path('api/', include(router.urls)),
]
