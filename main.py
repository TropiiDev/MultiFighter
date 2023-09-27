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
            "cost": 50,
            "health": 50
        }
    elif option == "Damage":
        upgrade = {
            "name": "Damage",
            "cost": 50,
            "multi": rand_number(1, 5)
        }
    
    return upgrade
    
def create_monster(num):
    if num == 1:
        monster = {
            "name": "Slime",
            "dmg": rand_number(1, 50),
            "health": 50,
            "GOD": rand_number(1, 10),
            "xp": rand_number(1, 10)
        }
    elif num == 2:
        monster = {
            "name": "Wolf",
            "dmg": rand_number(1, 100),
            "health": 100,
            "GOD": rand_number(1, 25),
            "xp": rand_number(1, 25)
        }
    elif num == 3:
        monster = {
            "name": "Baby Dragon",
            "dmg": rand_number(1, 150),
            "health": 150,
            "GOD": rand_number(1, 50),
            "xp": rand_number(1, 50)
        }
        
    
    return monster

# For creating the user - DOES NOT SAVE UPON RESTART -
    
def create_user(name, age):
    user = {
        "name": name,
        "age": age,
        "health": 150,
        "gold": 0,
        "inventory": [tools("stick")],
        "level": 1,
        "xp": 0,
        "multi": 0
    }
    
    return user
    
# for leveling system

def level(level, xp):
    if int(xp) >= int(level) * 10:
        player["level"] = int(level) + 1
        xp = int(xp) - int(level) * 10
        print(f"Leveled up! :)\n\nYou are now level {player['level']}!")
    else:
        print("Didn't level up! :(")
        
def check_level():
    if monster["health"] <= 0:
        print(f"You beat {monster['name']}!")
        player["gold"] = str(player["gold"]) + str(monster["GOD"])
        print(f"You earned {monster['GOD']} gold!")
        player["xp"] = int(player["xp"]) + int(monster["xp"])
        level(player["level"], player["xp"])
        print(f"You earned {monster['xp']} xp! You now have {player['xp']} xp!\nIn order to level up you need {int(player['level']) * 10 - player['xp']} xp.")
        return True
    elif int(player["health"]) <= 0:
        return False

# for fighting monsters

def fight():
    dmg = monster["dmg"]
    player["health"] = int(player["health"]) - int(dmg)
    print(f"You lost {dmg} health!")
    inv = player["inventory"][0]
    pdmg = int(inv["dmg"]) * int(inv["multi"]) + int(player['multi'])
    monster["health"] = monster["health"] - pdmg
    print(f"You did {pdmg} damage to {monster['name']}!")
    
def question():
    wtd = input(f"You found a {monster['name']}! What would you like to do?\n(Run, Attack, Dodge): ")
    
    return wtd

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
            wtd = question()
            if wtd == "Attack":
                fight()
                abc = check_level()
                if abc == False:
                    break
                elif abc == True:
                    print("")
                else:
                    wtd = question()
                    if wtd == "Attack":
                        fight()
                        abc = check_level()
                        if abc == False:
                            break
                        elif abc == True:
                            print("")
                        else:
                            wtd = question()
                            if wtd == "Attack":
                                fight()
                                abc = check_level()
                                if abc == False:
                                    break
                                elif abc == True:
                                    print("")
                                else:
                                    wtd = question()
                                    if wtd == "Attack":
                                        fight()
                                        abc = check_level()
                                        if abc == False:
                                            break
                                        elif abc == True:
                                            print("")
                                        else:
                                            wtd = question()
                                            fight()
                                            abc = check_level()
                                            if abc == False:
                                                break
                                            elif abc == True:
                                                print("")
                                            else:
                                                print("You managed to get away before you died.")

    # Explore Caves
    elif questions == "Explore Caves":
        chance = rand_number(1, 10)
        if chance < 5:
            print("You got no gold")
        else:
            gold = rand_number(1, 50)
            player["gold"] = player["gold"] + gold
            print(f"Congrats! You got {gold} gold!")
    
    # Shop
    elif questions == "Shop":
        print(f"Welcome to the shop {player['name']}!")
        print(f"You have {player['gold']} gold!")
        wts = input("Welcome to the shop! What would you like to buy?\n(Tools, Upgrades): ")
        if wts == "Tools":
            buying = input("Choose something to buy:\n(Sword, Enhanced Stick, Enhanced Sword) ")
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
                bought = upgrades(buying)
                if int(player["gold"]) >= bought["cost"]:
                    player["health"] = player["health"] + bought["health"]
                    print("Bought some health!")
                    print(f"You now have {player['health']} health!")
            elif buying == "Damage":
                bought = upgrades(buying)
                if int(player["gold"]) >= bought["cost"]:
                    player["multi"] = bought["multi"]
                    print(f"You now have a damage multiplier of {player['multi']}!")
    elif questions == "%USERMOD%":
        edit = input("What to edit in user:\n(Name, Health, Gold, Inventory, Level, XP, Multi): ")
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
            if tools(inventory):
                player["inventory"].pop(0)
                player["inventory"].append(tools(inventory))
            else:
                if upgrades(inventory):
                    if buying == "Health":
                        bought = upgrades(buying)
                        if int(player["gold"]) >= bought["cost"]:
                            player["health"] = player["health"] + bought["health"]
                    elif buying == "Damage":
                        bought = upgrades(buying)
                        if int(player["gold"]) >= bought["cost"]:
                            player["multi"] = bought["multi"]
                else:
                    print("Not a valid item!")
            print(player["inventory"])
        elif edit == "Level":
            level = input("What do you want the user's level to be? ")
            player['level'] = level
        elif edit == "XP":
            xp = input("What do you want the user's xp to be? ")
            player['xp'] = xp
            print(player['xp'])
        elif edit == "Multi":
            multi = input("What do you want the user's multi to be? ")
            player['multi'] = multi
            
    elif questions == "%CHECK%":
        check = input("What do you want to check for the user? ")
        if check == "Health":
            print(player["health"])
            sleep(1)
        elif check == "Inventory":
            print(player["inventory"])
            sleep(1)
        elif check == "Gold":
            print(player["gold"])
            sleep(1)
        elif check == "Level":
            print(player['level'])
            sleep(1)
        elif check == "XP":
            print(player['xp'])
            sleep(1)
        elif check == "Multi":
            print(player["multi"])
            sleep(1)