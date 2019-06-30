import pandas as pd
import csv, pprint

class Offer:
    def __init__(self):
        self.requirements = {}
        self.possibilities = []
        self.impossibilities = {}
        self.makeOffers()

    def checkPossibilities(self):
        for index, row in dfRecipes.iterrows():
            self.impossibilities[row['name']] = []
            for requirement in row['list_of_ingredients'].split(','):
                ingredient = requirement.split(':')[0]
                requiredAmount = requirement.split(':')[1]
                self.requirements[ingredient] = requiredAmount
                if float(inventory.amountOf(ingredient)) < float(requiredAmount):
                    self.impossibilities[row['name']].append("Missing {0}".format(ingredient))
                else:
                    pass
            if len(self.impossibilities[row['name']]) == 0:
                self.possibilities.append(row['name'])
                del self.impossibilities[row['name']]
            else:
                pass

        return self.possibilities

    def makeOffers(self):
        possibilities = self.checkPossibilities()

# class Ingredient:
#     """An object representing a single ingredient"""
#     def __init__(self, name, weight, quantity):
#         self.name = name
#         self.weight = weight
#         self.quantity = quantity
#
#     def getName(self):
#         return self.name
#
#     def getWeight(self):
#         return self.weight
#
#     def getQuantity(self):
#         return self.quantity

class Inventory():
    """An object holding all inventory elements within a Pandas DataFrame"""
    def __init__(self, inventory):
        self.inventory = inventory

    def getInventoryList(self):
        """Returns self.inventory DataFrame"""
        return self.inventory

# class Recipe():
#     """An object representing a single recipe"""
#     def __init__(self, name, duration, class, listOfIngredients):
#         self.name = name
#         self.duration = duration
#         self.class = class
#         self.listOfIngredients = listOfIngredients
#
#     def getName(self):
#         return self.name
#
#     def getDuration(self):
#         return self.duration
#
#     def getClass(self):
#         return self.class
#
#     def getListOfIngredients(self):
#         return self.listOfIngredients

class RecipeBook():
    """An object holding all recipes"""
    def __init__(self, recipes):
        self.recipes = recipes
        self.buildRecipeBook(recipes)

    def getRecipeBook(self):
        """Returns self.recipes"""
        return self.recipes

    def filterRecipes(self):
        """Returns a filtered DataFrame of all recipes"""

    def buildRecipeBook(self, recipes):
        """Populates self.recipes list with Recipe objects representing every recipe"""
        for index, row in recipes.iterrows():
            self.recipes.append(Recipe(row['name'],row['duration'],row['class'],row['list_of_ingredients']))

    def getRecipe(self, name):
        """Returns the desired (name) Recipe object from self.recipes list"""
        for recipe in self.recipes:
            if recipes.getName() == name:
                return recipe
            else:
                pass

    def requiredIngredients(self, recipe):
        """Returns a dictionary with every required ingredient (object) of the desired recipe"""
        desiredRecipe = getRecipe(recipe)

def main():
    dataAddress = 'Budget.xlsx'

    # dfIngredients = pd.read_excel(dataAddress,'Ingredients')
    inventory = Inventory(pd.read_excel(dataAddress,'Inventory').replace(pd.np.nan, '', regex=True, inplace=True))
    recipeBook = recipeBook(pd.read_excel(dataAddress,'Recipes'))

    a = Offer()

if __name__ == "__main__":
    main()
