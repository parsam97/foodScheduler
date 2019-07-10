# import pandas as pd
import csv, pprint, json

class Inventory():
    """An object holding all inventory elements within a Pandas DataFrame"""
    def __init__(self, inventory):
        self.inventory = inventory

    def getDf(self):
        """Returns self.inventory DataFrame"""
        return self.inventory

class RecipeBook():
    """An object holding all recipe elements within a Pandas DataFrame"""
    def __init__(self, recipes):
        self.recipes = recipes

    def getDf(self):
        """Returns self.inventory DataFrame"""
        return self.recipes

def main():
    dataAddress = 'Budget.xlsx'

    aa = json.loads('recipes')


    inventory = Inventory(json.loads('recipes.json'))
    recipeBook = RecipeBook(json.loads('inventory.json'))

    print(inventory.getDf())
    print(recipeBook.getDf())

if __name__ == "__main__":
    main()


with open('helpme.json') as f:
    f.write(json.dumps({"hi":"bye","hiagain":"byeagain"}))
