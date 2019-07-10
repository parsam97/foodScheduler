<<<<<<< HEAD
# import pandas as pd
=======
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from collections import OrderedDict
>>>>>>> 7633d12d71506f115358538d93a8eb445bd0e4c1
import csv, pprint, json

class Inventory():
    """An object holding all inventory elements within a Pandas DataFrame"""
    def __init__(self, inventory):
        self.inventory = pd.DataFrame(inventory)

    def getDf(self):
        """Returns self.inventory DataFrame"""
        return self.inventory

    def selectFiltered(self, column, params, inverse=False):
        """Returns a filtered self.inventory df based on the conditions (column, params)"""
        if inverse is False:
            if type(params[0]) is int:
                return self.inventory[(self.inventory[column]>params[0]) & (self.inventory[column]<params[1])]
            else:
                return self.inventory[self.inventory[column].isin(params)]
        else:
            if type(params[0]) is int:
                return self.inventory[(self.inventory[column]<params[0]) | (self.inventory[column]>params[1])]
            else:
                return self.inventory[~self.inventory[column].isin(params)]

    def portionAte(self, recipe, recipeBookDF):
        """Takes in the recipe eaten and decreases the weight of the ingredients involved with that recipe in the inventory"""
        ingredients = recipeBookDF[recipeBookDF['Name'] == recipe]['ListOfIngredients'][0].split(',')
        print(self.inventory['Weight'])
        for ingredient in ingredients:
            ing = ingredient.split(':')[0]
            amt = float(ingredient.split(':')[1])
            print(amt)
            self.inventory.loc[self.inventory['Name'].isin([ing]), 'Weight'] = self.selectFiltered('Name', [ing])['Weight'].map(lambda x: x-amt)
        print(self.inventory['Weight'])

class RecipeBook():
    """An object holding all recipe elements within a Pandas DataFrame"""
    def __init__(self, recipes):
        self.recipes = pd.DataFrame(recipes)

    def getDf(self):
        """Returns self.inventory DataFrame"""
        return self.recipes

def main():
    dataAddress = 'Budget.xlsx'

<<<<<<< HEAD
    aa = json.loads('recipes')


    inventory = Inventory(json.loads('recipes.json'))
    recipeBook = RecipeBook(json.loads('inventory.json'))
=======
    with open('inventory.json') as f:
        inventory = Inventory(json.load(f, object_pairs_hook=OrderedDict))

    with open('recipes.json') as f:
        recipeBook = RecipeBook(json.load(f, object_pairs_hook=OrderedDict))

    inventory.portionAte('Noon Panir', recipeBook.getDf())
>>>>>>> 7633d12d71506f115358538d93a8eb445bd0e4c1

    # print(inventory.getDf().head())
    # print(recipeBook.getDf().head())

if __name__ == "__main__":
    main()


with open('helpme.json') as f:
    f.write(json.dumps({"hi":"bye","hiagain":"byeagain"}))
