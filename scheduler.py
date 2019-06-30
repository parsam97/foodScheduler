import pandas as pd
import csv, pprint

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

class 

def main():
    dataAddress = 'Budget.xlsx'

    inventory = Inventory(pd.read_excel(dataAddress,'Inventory'))
    recipeBook = RecipeBook(pd.read_excel(dataAddress,'Recipes'))

    print(inventory.getDf())
    print(recipeBook.getDf())

if __name__ == "__main__":
    main()
