import random
from time import sleep

# For randomizing numbers

def rand_number(int, int2):
    smth = random.randint(int, int2)
    
    return smth

# For tools, upgrades, and creating monsters
    
def tools(option):
    if option == "stick":
        tool = {
            "name": "Stick",
            "dmg": 5,
            "multi": 1,
            "cost": 0
        }
    elif option == "Sword":
        tool = {
            "name": "Sword",
            "dmg": 10,
            "multi": rand_number(1, 5),
            "cost": 20
        }
    elif option == "Enhanced Stick":
        tool = {
            "name": "Enhanced Stick",
            "dmg": 15,
            "multi": rand_number(1, 10),
            "cost": 50
        }
    elif option == "Enhanced Sword":
        tool = {
            "name": "Enhanced Sword",
            "dmg": 20,
            "multi": rand_number(1, 15),
            "cost": 100
        }
    
    return tool

def upgrades(option):
    if option == "Health":
        upgrade = {
            "name": "Health",
            "cost": 50
        }
    elif option == "Damage":
        upgrade = {
            "name": "Damage",
            "cost": 50
        }
    
    return upgrade
    
def create_monster(num):
    if num == 1:
        monster = {
            "name": "Slime",
            "dmg": rand_number(1, 50),
            "health": 50,
            "GOD": rand_number(1, 10)
        }
    elif num == 2:
        monster = {
            "name": "Wolf",
            "dmg": rand_number(1, 100),
            "health": 100,
            "GOD": rand_number(1, 25)
        }
    elif num == 3:
        monster = {
            "name": "Baby Dragon",
            "dmg": rand_number(1, 150),
            "health": 150,
            "GOD": rand_number(1, 50)
        }
        
    
    return monster

# For creating the user - DOES NOT SAVE UPON RESTART -
    
def create_user(name, age):
    user = {
        "name": name,
        "age": age,
        "health": 150,
        "gold": 0,
        "inventory": [tools("stick")]
    }
    
    return user

# For creating the user - DOES NOT SAVE UPON RESTART -

name = input("Enter a name: ")
age = input("Enter a age: ")
player = create_user(name, age)


while True:
    # What would the user like to do in the start of the game?
    questions = input("You made your way to town square, what would you like to do?\n(Fight Monster, Explore Caves, Shop): ")
    

    # Fight Monsters
    if questions == "Fight Monster":
        chance = rand_number(1, 10)
        if chance < 3:
            print("You didn't find any monsters")
        else:
            monster = create_monster(rand_number(1, 3))
            wtd = input(f"You found a {monster['name']}! What would you like to do?\n(Run, Attack, Dodge): ")
            if wtd == "Attack":
                dmg = monster["dmg"]
                player["health"] = player["health"] - dmg
                print(f"You lost {dmg} health!")
                wtd = input(f"What would you like to do?\n(Run, Attack, Dodge): ")
                if wtd == "Attack":
                    inv = player["inventory"][0]
                    pdmg = inv["dmg"] * inv["multi"]
                    monster["health"] = monster["health"] - pdmg
                elif wtd == "Run":
                    sleep(1)
                elif wtd == "Dodge":
                    chance = rand_number(1, 10)
                    if chance <= 5:
                        dmg = monster["dmg"]
                        player["health"] = player["health"] - dmg
                        print(f"You lost {dmg} health!")
                        wtd = input(f"What would you like to do?\n(Run, Attack, Dodge): ")
                        if wtd == "Attack":
                            inv = player["inventory"][0]
                            pdmg = inv["dmg"] * inv["multi"]
                            monster["health"] = monster["health"] - pdmg
                    else:
                        print("You managed to dodge the next attack")
                        sleep(1)
                        wtd = input(f"What would you like to do?\n(Run, Attack, Dodge): ")
                        print("NO!")
            if monster["health"] <= 0:
                print(f"You beat {monster['name']}!")
                player["gold"] = player["gold"] + monster["GOD"]
                print(f"You earned {monster['GOD']} gold!")
            elif player["health"] <= 0:
                print("You died!")
                sleep(2)

    # Explore Caves
    elif questions == "Explore Caves":
        chance = rand_number(1, 10)
        if chance < 5:
            print("You got no gold")
        else:
            gold = rand_number(1, 50)
            player["gold"] = player["gold"] + gold
            print(f"Congrats! You got {player['gold']} gold!")
    
    # Shop
    elif questions == "Shop":
        print(f"Welcome to the shop {player['name']}!")
        print(f"You have {player['gold']} gold!")
        wts = input("Welcome to the shop! What would you like to buy?\n(Tools, Upgrades): ")
        if wts == "Tools":
            buying = input("Choose something to buy: (Sword, Enhanced Stick, Enhanced Sword) ")
            bought = tools(buying)
            if int(player["gold"]) >= bought["cost"]:
                player["inventory"].append(bought)
                player["inventory"].pop(0)
                print(f"Successfully bought {bought}.\nCurrent Inventory: {player['inventory']}")
            else:
                print("Not enough gold")
        else:
            buying = input("Choose something to buy: (Health, Damage) ")
            if buying == "Health":
                pass
    elif questions == "%USERMOD%":
        edit = input("What to edit in user: (Name, Health, Gold, Inventory): ")
        if edit == "Name":
            name = input("What to change the users name to? ")
            player["name"] = name
            print(player["health"])
        elif edit == "Health":
            health = input("What to change the user's health to? ")
            player["health"] = health
            print(player["health"])
        elif edit == "Gold":
            gold = input("How much gold will the user have? ")
            player["gold"] = gold
            print(player["gold"])
        elif edit == "Inventory":
            inventory = input("What to add to the users inventory? ")
            player["inventory"].append(inventory)
            print(player["inventory"])