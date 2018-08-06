import re
from recipes.views import *

welcome = WelcomeView()
recipes = AllRecipes()
recipe = SingleRecipe()
create_recipe = CreateRecipe()
update_recipe = UpdateRecipe()
delete_recipe = DeleteRecipe()


def get_path(path, request_type, data=None):
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
                    return 404, 'Not Found'

        if any(path in url for url in paths):

            if path == '/':
                return paths[0][1].status_code, paths[0][1].data

            elif path == '/recipes':

                return paths[1][1].status_code, paths[1][1].data

        else:
            return 404, 'Not Found'

    elif request_type == 'POST':
        get_pk = re.findall("\d+", path)
        paths = [
            ('/recipes', create_recipe.post(data)),
        ]
        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/recipes/{}'.format(pk), update_recipe.post(data=data, pk=pk)),
            ]

            if any(path in url for url in paths):
                if path == '/recipes/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data

                elif path == '/recipes/{}'.format(pk):
                    return paths[1][1].status_code, paths[1][1].data

                else:
                    return 404, 'Not Found'

        if any(path in url for url in paths):
            if path == '/recipes':
                return paths[0][1].status_code, paths[0][1].data

        else:
            return 404, 'Not Found'

    elif request_type == 'DELETE':
        get_pk = re.findall("\d+", path)

        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/recipes/{}'.format(pk), delete_recipe.delete(pk=pk)),
            ]
            if path == '/recipes/{}'.format(pk):
                return paths[0][1].status_code, paths[0][1].data
        else:
            return 404, 'Not Found'
