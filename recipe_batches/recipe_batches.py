#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  if recipe.keys() > ingredients.keys():
    return 0

  batch = 0

  while True:

    for k,v in recipe.items():
      print(f"ingred key: {ingredients[k]}")
      ingredients[k] -= v
      print(ingredients[k])

    for k,v in ingredients.items():
      if v < 0:
        return batch
      else:
        pass

    batch += 1








  print(f"need: {ingredients_needed}")
  print(f"have: {ingredients_have}")









if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))