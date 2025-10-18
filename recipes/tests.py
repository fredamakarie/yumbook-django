# recipes/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Recipe, Ingredient

User = get_user_model()

class RecipeModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="chef", password="pass123")
        self.recipe = Recipe.objects.create(
            title="Pasta",
            description="Delicious pasta with tomato sauce",
            prep_time=15,
            cook_time=25,
            servings=2,
            author=self.user
        )
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name="Tomato",
            quantity="2 pcs"
        )

    def test_recipe_creation(self):
        """Ensure a recipe can be created"""
        self.assertEqual(self.recipe.title, "Pasta")
        self.assertEqual(self.recipe.author.username, "chef")

    def test_ingredient_linked_to_recipe(self):
        """Ensure ingredients are properly related"""
        self.assertEqual(self.ingredient.recipe, self.recipe)
        self.assertEqual(self.recipe.ingredient_set.count(), 1)

    def test_str_methods(self):
        """Check string representations"""
        self.assertEqual(str(self.recipe), "Pasta")
        self.assertEqual(str(self.ingredient), "Tomato (2 pcs)")


class RecipeAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="chef", password="pass123")
        self.client.login(username="chef", password="pass123")

        self.recipe = Recipe.objects.create(
            title="Rice",
            description="Steamed rice",
            prep_time=10,
            cook_time=15,
            servings=4,
            author=self.user
        )

        self.recipe_url = reverse("recipe-list")

    def test_list_recipes(self):
        """Ensure user can see their recipes"""
        response = self.client.get(self.recipe_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Rice", str(response.data))

    def test_create_recipe(self):
        """Ensure a user can create a new recipe via API"""
        data = {
            "title": "Soup",
            "description": "Hot chicken soup",
            "prep_time": 5,
            "cook_time": 20,
            "servings": 3,
        }
        response = self.client.post(self.recipe_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 2)

    def test_update_recipe(self):
        """Ensure a user can update their recipe"""
        url = reverse("recipe-detail", args=[self.recipe.id])
        data = {"title": "Fried Rice"}
        response = self.client.patch(url, data, format='json')
        self.recipe.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.recipe.title, "Fried Rice")

    def test_delete_recipe(self):
        """Ensure a user can delete their recipe"""
        url = reverse("recipe-detail", args=[self.recipe.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_recipe_pagination(self):
        """Ensure pagination works correctly"""
        for i in range(8):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Test recipe",
                prep_time=5,
                cook_time=10,
                servings=2,
                author=self.user
            )
        response = self.client.get(self.recipe_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.data)
        self.assertLessEqual(len(response.data["results"]), 6)  # PAGE_SIZE = 6
