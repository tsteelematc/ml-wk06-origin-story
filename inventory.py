import pandas as pd

# read the CSV
df = pd.read_csv("inventory.csv")

# define category groupings
health_food_cols = ["protein_shake", "powerade", "protein_bar", "vitamins"]
apparel_cols = ["nike_sneakers", "adidas_boots"]
digital_cols = ["fitbit", "fitness_watch"]

# create new aggregated columns
df["health_food"] = df[health_food_cols].sum(axis=1)
df["apparel"] = df[apparel_cols].sum(axis=1)
df["digital"] = df[digital_cols].sum(axis=1)

# optional: keep only buyer + new categories
result = df[["buyer", "health_food", "apparel", "digital"]]

print(result)
