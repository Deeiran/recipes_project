from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

'''
When we call #all method on recipe_repository,
we get all the recipes back to the list
'''
def test_get_all_recipes(db_connection):
    db_connection.seed('seeds/recipe.sql')
    repository = RecipeRepository(db_connection)

    assert repository.all() == [
        Recipe(1, 'chicken', 20.0, 3),
        Recipe(2, 'pizza', 10.0, 3),
        Recipe(3, 'lazania', 25.5, 3),
        Recipe(4, 'pasta', 15.5, 3),
        Recipe(5, 'soup', 5.5, 3)
    ]

'''
We call #find method to find a single recipe
'''
def test_find_single_recipe(db_connection):
    db_connection.seed('seeds/recipe.sql')
    repository = RecipeRepository(db_connection)

    assert repository.find(2) == Recipe(2, 'pizza', 10.0, 3)