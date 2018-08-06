from db.query import fetch_all_recipes
from servers.response import Response
from servers import status


def all_recipes():
    """
    :return:
    """
    return fetch_all_recipes()


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
                return return_data.append(recipe)
        return Response(data=return_data, status=status.HTTP_200_OK)



