from django.urls import path, include
from .views import RecipeCreateView
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'', RecipeViewSet, basename='recipe')

urlpatterns = [
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('', include(router.urls))
]
