import pandas as pd
import time

def read_file():
    recipe = pd.read_excel("Budget.xlsx", "Recipes")
    return recipe.to_json()

initial = read_file()
while True:
    current = read_file()
    if initial != current:
        with open('recipes.json', 'w') as f:
            f.write(current)
        initial = current
    time.sleep(60)
