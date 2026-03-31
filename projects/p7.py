# Tiziana Rizzato
# 3/25/26
# Assignment 7: Working with dictionaries 



# Starting character
Norm = {
    "name": "Norm the Forester",
    "health": 100,
    "attack": 20,
    "level": 2 

}
# TODO: Add at least two more attributes to Norm
# (include "attack" for battle)


# TODO: Create two additional characters

FrostByte = {
    "name": "FrostByte the Ice Mage",
    "health": 80, 
    "attack": 25,
    "gold": 60,
    "armor": 15 
}

Vortx = {
    "name": "Vortx the Shadow Assassin",
    "attack": 30,
    "health": 70,
    "weapon": "Shadow Dagger",
    "stealth": 80
}

def update_health(character, amount):

    current_health = character.get("health", 0)

#change in health

    new_health = current_health + amount

    if new_health < 0: 
        new_health = 0
    elif new_health > 100:
         new_health = 100

    character ["health"] = new_health 


def display_character(character):
   
   print(f"Name: {character ['name']}")
   print(f"Health: {character['health']}")

   for key in character:
       if key not in ["name", "health"]:
           print(f"{key}: {character[key]}")

print()


def attack(attacker, defender):

    damage = attacker.get ("attack", 0 )

    print(f"{attacker['name']} attacks {defender['name']}!")
    print(f"{defender['name']} loses {damage} health.")

    update_health(defender, -damage)


# --- User Input for New Attribute ---
# TODO: ask user for attribute name
# TODO: ask user for value
# TODO: add to Norm dictionary

got_name = input("Enter attribute name: ")

got_value = input("Enter attribute value: ")

if got_value.isdigit():
    got_value = int(got_value)

Norm[got_name] = got_value

# --- Test your functions ---

update_health(Norm, -10)
attack(Norm, FrostByte)

print ()


display_character(Norm)
display_character(FrostByte)
display_character(Vortx)




