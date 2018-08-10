import re
from servers.default_user import user_data
from servers.status import *
from recipes.views import *

from settings.response_messages import *

welcome = WelcomeView()
recipes = AllRecipes()
recipe = SingleRecipe()
create_recipe = CreateRecipe()
update_recipe = UpdateRecipe()
delete_recipe = DeleteRecipe()
recipe_rating = RecipeRating()

key = user_data()


def get_path(path, request_type, data=None, authentication=None):

    if request_type == 'GET':
        get_pk = re.findall("\d+", path)

        paths = [
            ('/', welcome.get()),
            ('/recipes', recipes.get()),
        ]
        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/recipes/{}'.format(pk), recipe.get(pk=pk)),
            ]

            if any(path in url for url in paths):
                if path == '/recipes/{}'.format(pk):

                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        if any(path in url for url in paths):

            if path == '/':
                return paths[0][1].status_code, paths[0][1].data

            elif path == '/recipes':

                return paths[1][1].status_code, paths[1][1].data

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'POST':
        get_pk = re.findall("\d+", path)

        if authentication is None and path == '/recipes':
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(key):
            paths = [
                ('/recipes', create_recipe.post(data)),
            ]

            if any(path in url for url in paths):
                if path == '/recipes':
                    return paths[0][1].status_code, paths[0][1].data

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        elif authentication is None:
            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}/rating'.format(pk), recipe_rating.post(data=data, pk=pk)),
                ]

                if any(path in url for url in paths):
                    if path == '/recipes/{}/rating'.format(pk):
                        return paths[0][1].status_code, paths[0][1].data

                    else:
                        return HTTP_404_NOT_FOUND, URL_NOT_FOUND

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

    elif request_type == 'PUT':
        get_pk = re.findall("\d+", path)

        if authentication is None:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(key):

            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}'.format(pk), update_recipe.post(data=data, pk=pk)),
                ]

                if any(path in url for url in paths):
                    if path == '/recipes/{}'.format(pk):
                        return paths[0][1].status_code, paths[0][1].data
                    else:
                        return HTTP_404_NOT_FOUND, URL_NOT_FOUND

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

    elif request_type == 'DELETE':
        get_pk = re.findall("\d+", path)

        if authentication is None:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        elif authentication == 'Basic ' + str(key):
            if get_pk:
                pk = get_pk[0]
                paths = [
                    ('/recipes/{}'.format(pk), delete_recipe.delete(pk=pk)),
                ]
                if path == '/recipes/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data

                return HTTP_404_NOT_FOUND, URL_NOT_FOUND
            else:
                return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        else:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED
