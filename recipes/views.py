from db.query import fetch_all_recipes
from db.curd import create_recipe_into_db, update_recipe_into_db, delete_recipe_from_db, recipe_rating_into_db
from servers.response import Response
from servers import status


class WelcomeView:

    def get(self):
        data = 'Welcome to HelloFresh'
        return Response(data=data, status=status.HTTP_200_OK)


class AllRecipes:

    def get(self):
        data = fetch_all_recipes()
        return Response(data=data, status=status.HTTP_200_OK)


class SingleRecipe:

    def get(self, pk=None):
        recipes = fetch_all_recipes()
        return_data = []
        for recipe in recipes:
            if recipe['id'] == int(pk):
                return_data.append(recipe)
        return Response(data=return_data, status=status.HTTP_200_OK)


class CreateRecipe:

    def post(self, data):
        message, status_code = create_recipe_into_db(data=data)
        return Response(data=message, status=status_code)


class UpdateRecipe:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = update_recipe_into_db(data)
        return Response(data=message, status=status_code)


class DeleteRecipe:

    def delete(self, pk=None):
        message, status_code = delete_recipe_from_db({"id": pk})
        return Response(data=message, status=status_code)


class RecipeRating:

    def post(self, data, pk=None):
        data['id'] = pk
        message, status_code = recipe_rating_into_db(data=data)
        return Response(data=message, status=status_code)