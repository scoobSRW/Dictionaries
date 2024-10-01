restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#update add bevs
restaurant_menu.update({"Beverages": {"Fountain Drinks" : 1.99, "Bottled Cokes": 2.87,
             "Water Bottles": 2.13}})

#update steak price
restaurant_menu.update({"Main Course": {"Steak": 17.99, "Salmon": 13.99}})

#remove Bruschetta from "Starters"
restaurant_menu["Starters"].pop("Bruschetta")

#i love this format so here we're formatting...
for k, v in restaurant_menu.items():
    print(k, v)
