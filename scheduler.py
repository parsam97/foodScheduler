import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from collections import OrderedDict
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

    def changeInWeight(self, df, amt):
        """Takes in a DataFrame (df) and adds the amount (amt) to the 'Weight in store' value of that ingredient"""
        mask = (self.inventory['Name'] not in list(df['Name']))
        self.inventory['Weight in store'] = self.inventory['Name'].apply(lambda x: x+amt if x in list(df['Name']) else x)


class RecipeBook():
    """An object holding all recipe elements within a Pandas DataFrame"""
    def __init__(self, recipes):
        self.recipes = pd.DataFrame(recipes)

    def getDf(self):
        """Returns self.inventory DataFrame"""
        return self.recipes

def main():
    dataAddress = 'Budget.xlsx'

    with open('inventory.json') as f:
        inventory = Inventory(json.load(f, object_pairs_hook=OrderedDict))

    with open('recipes.json') as f:
        recipeBook = RecipeBook(json.load(f, object_pairs_hook=OrderedDict))


    # print(inventory.getDf().head())
    # print(recipeBook.getDf().head())

if __name__ == "__main__":
    main()
