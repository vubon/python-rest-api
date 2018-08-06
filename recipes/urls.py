from recipes.views import *
welcome = WelcomeView()
recipes = AllRecipes()
recipe = SingleRecipe()


paths = [
    ('/', welcome.get()),
    ('/recipes', recipes.get()),
    ('/recipes/{}', recipe),

]
