from django.urls import path
from .views import (
    RecipeCreateView, RecipeUpdateView, RecipeDeleteView, RecipeListView, RecipeDetailView, LoginView, LogoutView, SignUpView
)

urlpatterns = [
    path('login/', LoginView.as_view (template_name='blog/login.html'), name='login'),
    path('register/', SignUpView.as_view (template_name='blog/register.html')),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('myrecipes/', RecipeListView.as_view(), name='recipe-list'),
    path('myrecipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('myrecipes/<int:pk>/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('myrecipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('myrecipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]
