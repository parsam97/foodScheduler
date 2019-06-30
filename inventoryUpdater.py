import pandas as pd
import time

def read_file():
    inventory = pd.read_excel("Budget.xlsx", "Inventory")
    return inventory.to_json()

initial = read_file()
while True:
    current = read_file()
    if initial != current:
        with open('inventory.json', 'w') as f:
            f.write(current)
        initial = current
    time.sleep(60)
