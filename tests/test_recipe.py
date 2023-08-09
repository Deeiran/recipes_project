from lib.recipe import Recipe

"""instract the recipe classs with
 table columns and intiate it.
 """
def test_recipe_constructs():
    recipe = Recipe(1,"chicken",20,3)
    assert recipe.id == 1
    assert recipe.name == "chicken"
    assert recipe.cooking_time == 20
    assert recipe.rating == 3