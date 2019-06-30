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

class Ingredient:
    """An object representing a single ingredient"""
    def __init__(self, name, weight, quantity):
        self.name = name
        self.weight = weight
        self.quantity = quantity

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getQuantity(self):
        return self.quantity

class Inventory():
    """An object holding all inventory elements"""
    def __init__(self, inventory):
        self.inventory = []
        self.buildInventory(inventory)

    def buildInventory(self, inventory):
        """Populates self.inventory list with Ingredient objects representing every ingredient"""
        for index, row in inventory.iterrows():
            self.inventory.append(Ingredient(row['name'],row['weight'],row['quantity']))

    def getInventoryList(self):
        """Returns self.inventory"""
        return self.inventory

    def getIngredient(self, name):
        """Returns the desired (name) Ingredient object from self.inventory list"""
        for ingredient in self.inventory:
            if ingredient.getName() == name:
                return ingredient
            else:
                pass

    def amountOf(self, name):
        """ Returns the weight or quantity attribute of the desired Ingredient object """
        currIngredient = self.getIngredient(name)
        if currIngredient.getWeight() == '':
            return currIngredient.getQuantity()
        else:
            return currIngredient.getWeight()

class Recipe():
    """An object representing a single recipe"""
    def __init__(self, name, duration, class, listOfIngredients):
        self.name = name
        self.duration = duration
        self.class = class
        self.listOfIngredients = list_of_ingredients

    def getName(self):
        return self.name

    def getDuration(self):
        return self.duration

    def getClass(self):
        return self.class

    def getListOfIngredients(self):
        return self.listOfIngredients


class RecipeBook():
    """An object holding all recipes"""

def main():
    dataAddress = 'Budget.xlsx'

    dfIngredients = pd.read_excel(dataAddress,'Ingredients')
    dfRecipes = pd.read_excel(dataAddress,'Recipes')
    dfInventory = pd.read_excel(dataAddress,'Inventory')
    dfInventory.replace(pd.np.nan, '', regex=True, inplace=True)

    inventory = Inventory(dfInventory)

    a = Offer()

if __name__ == "__main__":
    main()
