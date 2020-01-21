__author__ = 'jarrutus'
import random
import sys
import copy

import line_of_sight

check_if_visible = line_of_sight.check_if_visible

class character:
    def __init__(self, name, gender, role, race, attributes):
        self.name = name
        self.gender = gender
        self.role = role
        self.race = race
        self.xp = 0
        self.lvl = 1
        self.strength = attributes[0]
        self.dexterity = attributes[1]
        self.constitution = attributes[2]
        self.intelligence = attributes[3]
        self.wisdom = attributes[4]
        self.charisma = attributes[5]
        self.proficiency = 2
        self.strength_modifier = (self.strength - (self.strength % 2) - 10) / 2
        self.dexterity_modifier = (self.dexterity - (self.dexterity % 2) - 10) / 2
        self.constitution_modifier = (self.constitution - (self.constitution % 2) - 10) / 2
        self.intelligence_modifier = (self.intelligence - (self.intelligence % 2) - 10) / 2
        self.wisdom_modifier = (self.wisdom - (self.wisdom % 2) - 10) / 2
        self.charisma_modifier = (self.charisma - (self.charisma % 2) - 10) / 2
        for i in range(12):
            if roles[i] == self.role:
                self.hp = role_hps[i] + self.constitution_modifier
                break
        self.temp_hp = self.hp


    def add_xp(self, additional_xp):
        """Adds xp to the character and checks if character levels up or not."""
        additional_xp = int(additional_xp)
        self.xp = self.xp + additional_xp
        print("%s has now %d experience points." % (self.name, self.xp))
        if self.xp > 300 and self.lvl == 1:
            self.lvl = 2
            print("%s has gained a level." % self.name)
        if self.xp > 900 and self.lvl == 2:
            self.lvl = 3
            print("%s has gained a level." % self.name)
        if self.xp > 2700 and self.lvl == 3:
            self.lvl = 4
            print("%s has gained a level." % self.name)


#class enemy:
#    def __init__(self, type):



roles = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock",
         "Wizard"]
role_hps = [12, 8, 8, 8, 10, 8, 10, 10, 8, 6, 8, 6]
races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
characters_c = {}
characters = []
character_slots = []
slot_buys = ["b", "c", "d", "e", "f", "g", "h", "i", "j"]
day = 1
names_dwarf_male = ["Kathumir", "Thrar", "Skovrom", "Durin", "Bruenor", "Gloin", "Oin", "Rumnum", "Galik", "Firrean"]
names_dwarf_female = ["Thotrere", "Kosdruni", "Kivolynn", "Houdiren", "Nargiren", "Marbibo", "Vodwebo", "Moberika",
                      "Umidruthra", "Yuzona"]
names_elf_male = ["Elrond", "Haldir", "Vaeril", "Hastos", "Kolvar", "Illithor", "Aias", "Aithlin", "Estelar", "Folwin"]
names_elf_female = ["Allisa", "Cellica", "Cremia", "Arwen", "Galadriel", "Lyndis", "Talila", "Syndra", "Sorsastra",
                    "Mylaerla"]
names_halfling_male = ["Odilon", "Leger", "Fridolin", "Brutus", "Bilbo", "Samwise", "Alaric", "Hagen", "Ragnfred",
                       "Fastolph"]
names_halfling_female = ["Terri", "Tatiana", "Mindy", "Alpais", "Linda", "Robinia", "Rhoda", "Caitlin", "Yolanda",
                         "Clothild"]
names_human_male = ["Frederic", "Elyot", "Challes", "Leo", "Roulf", "Artus", "Guilhelm", "Reymond", "Jacke", "Gavin"]
names_human_female = ["Birgida", "Muriel", "Isabel", "Marione", "Ioletta", "Mirils", "Elisabeth", "Emily", "Josephine",
                      "Astrida"]
names_dragonborn_male = []

battle_ground_1 = [[".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", "W", "W", ".", "W", "W", ".", ".", ".", ".", ".", ".", ".", "W", "W", "W", "W", "W"],
                   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
                   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
                   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
                   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", "W", "W", "W", "W"],
                   [".", ".", ".", ".", ".", ".", ".", ".", "W", "W", ".", "W", "W", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", "."]
                   ]


def starting_screen():
    """Prints out the starting screen. All you need to start with."""
    print("###########################################################################")
    print("#                                                                         #")
    print("#                                                             A           #")
    print("#       A Dungeons and Dragons text-game                     / \          #")
    print("#                                                           /   \         #")
    print("#       'Delve into the depths'                            /     \        #")
    print("#                                                         /       \       #")
    print("#                                                  A     /  ____   \      #")
    print("#     Choose a number and press Enter             / \   /__/    \___\     #")
    print("#                                                /  _\ /             \    #")
    print("#     1. New Game                               /__/  V               \   #")
    print("#                                              /       \               \  #")
    print("#     2. Load Game                            /         \               \ #")
    print("#                                            /           \               \#")
    print("#     3. Credits                            /             \     v.0.0.1   #")
    print("#                                                                         #")
    print("###########################################################################")
    #   print("123456789012345678901234567890123456789012345678901234567890123456789012345") 75
    pointer = 0
    while pointer == 0:
        choice = input("Your choice: \n")
        if 4 > int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                pointer = 1
                prepare_new_game()
                start_new_game()
            elif choice == 2:
                pointer = 1
                # load_game()
            elif choice == 3:
                pointer = 1
                creators()
            else:
                print("The number you chose is not an option")
        if pointer != 0:
            break
        else:
            print("This was not an option, try again")


def prepare_new_game():
    for i in range(50):
        ticket = "a" + str(i)
        character_slots.append(ticket)


def creators():
    """Credits screen"""
    print("###########################################################################")
    print("#                                                                         #")
    print("#       Coded by Eero 'Zhatelier' 'jarrutus' Huhtelin                     #")
    print("#                                                                         #")
    print("#       Rulesets by Wizards of the Coast                                  #")
    print("#       Implemented by Eero Huhtelin                                      #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    back = input("Press 'Enter' to get back to the start screen: \n")
    if back == "":
        starting_screen()
    else:
        print("Leave input blank")
        pointer = 0
        while pointer == 0:
            back = input("Press 'Enter' to get back to the start screen: \n")
            if back == "":
                pointer = 1
                starting_screen()


def start_new_game():
    """Guides the player through character creation(s) and starts game process"""
    print("###########################################################################")
    print("#                                                                         #")
    print("#       You're about to begin a new adventure.                            #")
    print("#       How many chatacters would you like to begin with (1-6)?           #")
    print("#                                                                         #")
    print("#       While the adventure goes on you might acquire                     #")
    print("#       more character to your party.                                     #")
    print("#                                                                         #")
    print("#              &&                                                         #")
    print("#            &&&&&&                                                       #")
    print("#       &&   &&&&&& %%                                                    #")
    print("#     &&&&&&  &&&& %%%%                                                   #")
    print("#     &&&&&&   ||  %%%%                                                   #")
    print("#      &&&&    ||  %%%%                                                   #")
    print("#       ||    &&   %%%%  &&                                               #")
    print("#       ||  &&&&&&  || &&&&&&                                             #")
    print("###########################################################################")
    pointer = 0
    while pointer == 0:
        choice = input("Your choice: \n")
        if 7 > int(choice) > 0:
            choice = int(choice)
            for i in range(choice):
                create_character_1()
            pointer = 1
        if pointer != 0:
            break
        else:
            print("This was not an option, try again")
    beginning()
    play_game()


def create_character_1():
    """Determines the gender of the character after which directs to appropriate option (random or manual)"""
    print("###########################################################################")
    print("#                                                                         #")
    print("#       You are creating a new character.                                 #")
    print("#       You may create it step-by-step,                                   #")
    print("#       or let random generator do it for you.                            #")
    print("#                                                                         #")
    print("#       In any case, please choose a gender                               #")
    print("#       for the character first.                                          #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#       1. Create a man step-by-step                                      #")
    print("#       2. Create a woman step-by-step                                    #")
    print("#       3. Create a randomized man                                        #")
    print("#       4. Create a randomized woman                                      #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    pointer = 0
    while pointer == 0:
        choice = input("Your choice: \n")
        if 5 > int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                pointer = 1
                create_character_2("Male")
            elif choice == 2:
                pointer = 1
                create_character_2("Female")
            elif choice == 3:
                pointer = 1
                create_character_random("Male")
            elif choice == 4:
                pointer = 1
                create_character_random("Female")
            else:
                print("The number you chose is not an option")
        if pointer != 0:
            break
        else:
            print("This was not an option, try again")


def create_character_2(gender):
    if gender == "Male":
        print("###########################################################################")
        print("#                                                                         #")
        print("#       You are creating a male character.                                #")
        print("#       Next step is to choose a race:                                    #")
        print("#                                                                         #")
        print("#       1. Dwarf                                                          #")
        print("#       2. Elf                                                            #")
        print("#       3. Half-Elf                                                       #")
        print("#       4. Halfling                                                       #")
        print("#       5. Human                                                          #")
        print("#       6. Dragonborn                                                     #")
        print("#       7. Gnome                                                          #")
        print("#       8. Half-Orc                                                       #")
        print("#       9. Tiefling                                                       #")
        print("#                                                                         #")
        print("#                                                                         #")
        print("###########################################################################")

    elif gender == "Female":
        print("###########################################################################")
        print("#                                                                         #")
        print("#       You are creating a female character.                              #")
        print("#       Next step is to choose a race:                                    #")
        print("#                                                                         #")
        print("#       1. Dwarf                                                          #")
        print("#       2. Elf                                                            #")
        print("#       3. Half-Elf                                                       #")
        print("#       4. Halfling                                                       #")
        print("#       5. Human                                                          #")
        print("#       6. Dragonborn                                                     #")
        print("#       7. Gnome                                                          #")
        print("#       8. Half-Orc                                                       #")
        print("#       9. Tiefling                                                       #")
        print("#                                                                         #")
        print("#                                                                         #")
        print("###########################################################################")

    pointer = 0
    while pointer == 0:
        choice = input("Your choice of race: \n")
        if 10 > int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                pointer = 1
                race = "Dwarf"
            elif choice == 2:
                pointer = 1
                race = "Elf"
            elif choice == 3:
                pointer = 1
                race = "Half-Elf"
            elif choice == 4:
                pointer = 1
                race = "Halfling"
            elif choice == 5:
                pointer = 1
                race = "Human"
            elif choice == 6:
                pointer = 1
                race = "Dragoborn"
            elif choice == 7:
                pointer = 1
                race = "Gnome"
            elif choice == 8:
                pointer = 1
                race = "Half-Orc"
            elif choice == 9:
                pointer = 1
                race = "Tiefling"
            else:
                print("The number you chose is not an option")
        if pointer != 0:
            break
        else:
            print("This was not an option, try again")

    print("###########################################################################")
    print("#                                                                         #")
    print("#       Now choose a class for your character.                            #")
    print("#                                                                         #")
    print("#       1. Barbarian                                                      #")
    print("#       2. Bard                                                           #")
    print("#       3. Cleric                                                         #")
    print("#       4. Druid                                                          #")
    print("#       5. Fighter                                                        #")
    print("#       6. Monk                                                           #")
    print("#       7. Paladin                                                        #")
    print("#       8. Ranger                                                         #")
    print("#       9. Rogue                                                          #")
    print("#       10. Sorcerer                                                      #")
    print("#       11. Warlock                                                       #")
    print("#       12. Wizard                                                        #")
    print("###########################################################################")

    pointer = 0
    while pointer == 0:
        choice = input("Your choice of class: \n")
        if 13 > int(choice) > 0:
            choice = int(choice)
            if choice == 1:
                pointer = 1
                role = "Barbarian"
            elif choice == 2:
                pointer = 1
                role = "Bard"
            elif choice == 3:
                pointer = 1
                role = "Cleric"
            elif choice == 4:
                pointer = 1
                role = "Druid"
            elif choice == 5:
                pointer = 1
                role = "Fighter"
            elif choice == 6:
                pointer = 1
                role = "Monk"
            elif choice == 7:
                pointer = 1
                role = "Paladin"
            elif choice == 8:
                pointer = 1
                role = "Ranger"
            elif choice == 9:
                pointer = 1
                role = "Rogue"
            elif choice == 10:
                pointer = 1
                role = "Sorcerer"
            elif choice == 11:
                pointer = 1
                role = "Warlock"
            elif choice == 12:
                pointer = 1
                role = "Wizard"
            else:
                print("The number you chose is not an option")
        if pointer != 0:
            break
        else:
            print("This was not an option, try again")

    attributes = roll_attributes()
    printables = ""
    for i in range(6):
        text = attributes[i]
        if text > 9:
            printables = printables + str(text) + " "
        else:
            printables = printables + " " + str(text) + " "

    print("###########################################################################")
    print("#                                                                         #")
    print("#       Next your character needs a name.                                 #")
    print("#                                                                         #")
    print("#       We have also rolled you your scores for attributes.               #")
    print("#       It's up to you to distribute them however you see fit.            #")
    print("#                                                                         #")
    print("#       %s                                                #" % printables)
    print("#                                                                         #")
    print("#       You'll have to assign scores to Strength, Dexterity               #")
    print("#       Constitution, Inteligence, Wisdom and Charisma.                   #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    name = input("Give a name here: \n")
    scores = []
    while True:
        strength = input("Choose a score to use for strength:\n")
        if int(strength) in attributes:
            strength = int(strength)
            attributes.remove(strength)
            scores.append(strength)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    while True:
        dexterity = input("Choose a score to use for dexterity:\n")
        if int(dexterity) in attributes:
            dexterity = int(dexterity)
            attributes.remove(dexterity)
            scores.append(dexterity)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    while True:
        constitution = input("Choose a score to use for constitution:\n")
        if int(constitution) in attributes:
            constitution = int(constitution)
            attributes.remove(constitution)
            scores.append(constitution)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    while True:
        intelligence = input("Choose a score to use for intelligence:\n")
        if int(intelligence) in attributes:
            intelligence = int(intelligence)
            attributes.remove(intelligence)
            scores.append(intelligence)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    while True:
        wisdom = input("Choose a score to use for wisdom:\n")
        if int(wisdom) in attributes:
            wisdom = int(wisdom)
            attributes.remove(wisdom)
            scores.append(wisdom)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    while True:
        charisma = input("Choose a score to use for charisma:\n")
        if int(charisma) in attributes:
            charisma = int(charisma)
            attributes.remove(charisma)
            scores.append(charisma)
            print("You have following scores left: " + str(attributes).strip("[").strip("]"))
            break
        else:
            print("Score you gave was not a valid option (give the numeric value)")

    bio1 = "You have created a %s %s" % (race, role)
    bio2 = "Name of created character is %s" % name
    print("###########################################################################")
    print("#                                                                         #")
    print("#       %s " % bio1 + (" " * (65 - len(bio1))) + "#")
    print("#       %s " % bio2 + (" " * (65 - len(bio2))) + "#")
    print("#                                                                         #")
    print("#       Your attributes are as follows:                                   #")
    print("#                                                                         #")
    print("#       Strength: %s " % scores[0] + (" " * (55 - len(str(scores[0])))) + "#")
    print("#       Dexterity: %s " % scores[1] + (" " * (54 - len(str(scores[1])))) + "#")
    print("#       Constitution: %s " % scores[2] + (" " * (51 - len(str(scores[2])))) + "#")
    print("#       Intelligence: %s " % scores[3] + (" " * (51 - len(str(scores[3])))) + "#")
    print("#       Wisdom: %s " % scores[4] + (" " * (57 - len(str(scores[4])))) + "#")
    print("#       Charisma: %s " % scores[5] + (" " * (55 - len(str(scores[5])))) + "#")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    accept = input("Is this character fine? (y/n):\n")
    if accept == "y":
        character_slots[0] = character(name, gender, role, race, scores)
        id = character_slots.pop(0)
        characters_c[name] = id
        characters.append(name)
    else:
        create_character_1()


def create_character_random(gender):
    roll_race = random.randint(0, 8)
    race = races[roll_race]
    roll_class = random.randint(0, 11)
    role = roles[roll_class]
    attributes = roll_attributes()
    scores = assign_attributes_auto(role, attributes)
    name = grant_random_name(race, gender)
    character_slots[0] = character(name, gender, role, race, scores)
    id = character_slots.pop(0)
    characters_c[name] = id
    characters.append(name)
    bio1 = "We have created a %s %s for you" % (race, role)
    bio2 = "Name of created character is %s" % name
    print("###########################################################################")
    print("#                                                                         #")
    print("#       %s " % bio1 + (" " * (65 - len(bio1))) + "#")
    print("#       %s " % bio2 + (" " * (65 - len(bio2))) + "#")
    print("#                                                                         #")
    print("#       Their attributes are as follows:                                  #")
    print("#                                                                         #")
    print("#       Strength: %s " % scores[0] + (" " * (55 - len(str(scores[0])))) + "#")
    print("#       Dexterity: %s " % scores[1] + (" " * (54 - len(str(scores[1])))) + "#")
    print("#       Constitution: %s " % scores[2] + (" " * (51 - len(str(scores[2])))) + "#")
    print("#       Intelligence: %s " % scores[3] + (" " * (51 - len(str(scores[3])))) + "#")
    print("#       Wisdom: %s " % scores[4] + (" " * (57 - len(str(scores[4])))) + "#")
    print("#       Charisma: %s " % scores[5] + (" " * (55 - len(str(scores[5])))) + "#")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("###########################################################################")
    while True:
        forward = input("Press Enter to continue: ")
        if forward == "":
            break


def roll_an_attribute():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    roll4 = random.randint(1, 6)
    min_roll = min(roll1, roll2, roll3, roll4)
    attribute = roll1 + roll2 + roll3 + roll4 - min_roll
    return attribute


def roll_attributes():
    attributes = []
    for i in range(6):
        attribute = roll_an_attribute()
        attributes.append(attribute)
    return attributes


def assign_attributes_auto(role, attributes):
    if role == roles[0]:
        scores = assign_attributes_barbarian(attributes)
    elif role == roles[1]:
        scores = assign_attributes_bard(attributes)
    elif role == roles[2]:
        scores = assign_attributes_cleric(attributes)
    elif role == roles[3]:
        scores = assign_attributes_druid(attributes)
    elif role == roles[4]:
        scores = assign_attributes_fighter(attributes)
    elif role == roles[5]:
        scores = assign_attributes_monk(attributes)
    elif role == roles[6]:
        scores = assign_attributes_paladin(attributes)
    elif role == roles[7]:
        scores = assign_attributes_ranger(attributes)
    elif role == roles[8]:
        scores = assign_attributes_rogue(attributes)
    elif role == roles[9]:
        scores = assign_attributes_sorcerer(attributes)
    elif role == roles[10]:
        scores = assign_attributes_warlock(attributes)
    elif role == roles[11]:
        scores = assign_attributes_wizard(attributes)
    else:
        scores = attributes
    return scores


def assign_attributes_barbarian(attributes):
    scores = []
    strength = max(attributes)
    attributes.remove(strength)
    constitution = max(attributes)
    attributes.remove(constitution)
    dexterity = max(attributes)
    attributes.remove(dexterity)
    intelligence = attributes[0]
    wisdom = attributes[1]
    charisma = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_bard(attributes):
    scores = []
    charisma = max(attributes)
    attributes.remove(charisma)
    dexterity = max(attributes)
    attributes.remove(dexterity)
    constitution = max(attributes)
    attributes.remove(constitution)
    strength = attributes[0]
    intelligence = attributes[1]
    wisdom = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_cleric(attributes):
    scores = []
    wisdom = max(attributes)
    attributes.remove(wisdom)
    charisma = max(attributes)
    attributes.remove(charisma)
    constitution = max(attributes)
    attributes.remove(constitution)
    strength = attributes[0]
    intelligence = attributes[2]
    dexterity = attributes[1]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_druid(attributes):
    scores = []
    wisdom = max(attributes)
    attributes.remove(wisdom)
    intelligence = max(attributes)
    attributes.remove(intelligence)
    constitution = max(attributes)
    attributes.remove(constitution)
    strength = attributes[1]
    charisma = attributes[2]
    dexterity = attributes[0]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_fighter(attributes):
    scores = []
    strength = max(attributes)
    attributes.remove(strength)
    dexterity = max(attributes)
    attributes.remove(dexterity)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = attributes[0]
    wisdom = attributes[1]
    charisma = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_monk(attributes):
    scores = []
    dexterity = max(attributes)
    attributes.remove(dexterity)
    wisdom = max(attributes)
    attributes.remove(wisdom)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = attributes[0]
    strength = attributes[1]
    charisma = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_paladin(attributes):
    scores = []
    strength = max(attributes)
    attributes.remove(strength)
    charisma = max(attributes)
    attributes.remove(charisma)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = attributes[0]
    wisdom = attributes[1]
    dexterity = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_ranger(attributes):
    scores = []
    dexterity = max(attributes)
    attributes.remove(dexterity)
    wisdom = max(attributes)
    attributes.remove(wisdom)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = attributes[0]
    strength = attributes[1]
    charisma = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_rogue(attributes):
    scores = []
    dexterity = max(attributes)
    attributes.remove(dexterity)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = max(attributes)
    attributes.remove(intelligence)
    wisdom = attributes[0]
    strength = attributes[1]
    charisma = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_sorcerer(attributes):
    scores = []
    charisma = max(attributes)
    attributes.remove(charisma)
    intelligence = max(attributes)
    attributes.remove(intelligence)
    constitution = max(attributes)
    attributes.remove(constitution)
    wisdom = attributes[0]
    strength = attributes[1]
    dexterity = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_warlock(attributes):
    scores = []
    charisma = max(attributes)
    attributes.remove(charisma)
    wisdom = max(attributes)
    attributes.remove(wisdom)
    constitution = max(attributes)
    attributes.remove(constitution)
    intelligence = attributes[0]
    strength = attributes[1]
    dexterity = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def assign_attributes_wizard(attributes):
    scores = []
    intelligence = max(attributes)
    attributes.remove(intelligence)
    wisdom = max(attributes)
    attributes.remove(wisdom)
    constitution = max(attributes)
    attributes.remove(constitution)
    charisma = attributes[0]
    strength = attributes[1]
    dexterity = attributes[2]
    scores.append(strength)
    scores.append(dexterity)
    scores.append(constitution)
    scores.append(intelligence)
    scores.append(wisdom)
    scores.append(charisma)
    return scores


def grant_random_name(race, gender):
    if race == races[0]:
        if gender == "Male" and len(names_dwarf_male) > 0:
            pointer = random.randint(0, len(names_dwarf_male))
            name = names_dwarf_male[pointer]
            names_dwarf_male.remove(name)
            return name
        elif gender == "Female" and len(names_dwarf_female) > 0:
            pointer = random.randint(0, len(names_dwarf_female))
            name = names_dwarf_female[pointer]
            names_dwarf_female.remove(name)
            return name
    elif race == races[1]:
        if gender == "Male" and len(names_elf_male) > 0:
            pointer = random.randint(0, len(names_elf_male))
            name = names_elf_male[pointer]
            names_elf_male.remove(name)
            return name
        elif gender == "Female" and len(names_elf_female) > 0:
            pointer = random.randint(0, len(names_elf_female))
            name = names_elf_female[pointer]
            names_elf_female.remove(name)
            return name
    elif race == races[2]:
        if gender == "Male" and len(names_halfling_male) > 0:
            pointer = random.randint(0, len(names_halfling_male))
            name = names_halfling_male[pointer]
            names_halfling_male.remove(name)
            return name
        elif gender == "Female" and len(names_halfling_female) > 0:
            pointer = random.randint(0, len(names_halfling_female))
            name = names_halfling_female[pointer]
            names_halfling_female.remove(name)
            return name
    elif race == races[3]:
        if gender == "Male" and len(names_human_male) > 0:
            pointer = random.randint(0, len(names_human_male))
            name = names_human_male[pointer]
            names_human_male.remove(name)
            return name
        elif gender == "Female" and len(names_human_female) > 0:
            pointer = random.randint(0, len(names_dwarf_female))
            name = names_dwarf_female[pointer]
            names_dwarf_female.remove(name)
            return name
    else:
        number = 0
        name = "Bob"
        while True:
            if name not in characters:
                break
            else:
                number += 1
                name = "Bob" + str(number)
        return name


def beginning():
    print("###########################################################################")
    print("#                                                                         #")
    print("#   Your party is currently in the town of Stoneshade, which has been     #")
    print("#   overrun by forces of the evil lich Ogverac. His minion, Morden,       #")
    print("#   is the new governor of Stoneshade. Streets are patrolled by bandits   #")
    print("#   loyal to Ogverac and Morden. Gates are guarded by undead creatures    #")
    print("#   but some skilled individuals have a chance of getting in or out of    #")
    print("#   the town by climbing the walls. With such brave individuals comes     #")
    print("#   similar news from other towns near by. Your small party of brave      #")
    print("#   individuals has managed to scavenge some crude gear and has vowed     #")
    print("#   to take a stand against the forces of evil.                           #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#   Press Enter to continue.                                              #")
    print("#                                                                         #")
    print("###########################################################################")
    forward = input("")
    while True:
        if forward == "":
            break
        else:
            forward = input("Press Enter to continue:\n")


def day_menu():
    print("###########################################################################")
    print("#                                                                         #")
    print("#   Day %d " % day + (" " * (65 - len(str(day)))) + "#")
    print("#   C - Characters                                                        #")
    print("#   T - Town status                                                       #")
    print("#   H - Skirmish enemy                                                    #")
    print("#   A - Assault a location                                                #")
    print("#   E - Send expedition outside the town                                  #")
    print("#   R - Short rest                                                        #")
    print("#   F - Craft                                                             #")
    print("#   P - Shop                                                              #")
    print("#                                                                         #")
    print("#   N - Next day                                                          #")
    print("#                                                                         #")
    print("#   S = Save game                                              Q - Quit   #")
    print("#                                                                         #")
    print("###########################################################################")
    choice = input("What will you do?:\n")
    choice = str(choice).strip().lower()
    if choice == 'q':
        print("Shutting down the game.")
        sys.exit()
    #elif choice == "s":
        #save_game()
    elif choice == 'c':
        character_screen(characters, 0)
    #elif choice == "t":
        #town_status(locations)
    elif choice == "h":
        battle(battle_ground_1)
    #elif choice == "a":
        #assault(characters)
    #elif choice == "e":
        #expedition(characters)
    #elif choice == "r":
        #short_rest()
    #elif choice == "f":
        #crafting()
    #elif choice == "p":
        #shopping()
    else:
        print("You what now?")
        day_menu()


def character_screen(character_list, page):
    number = len(character_list)
    max_pages = int(number / 10)
    pointer = 0 + int(page) * 10
    print("###########################################################################")
    print("#                                                                         #")
    print("#   1. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   2. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   3. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   4. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   5. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   6. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   7. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   8. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   9. %s" % character_list[pointer] + (" " * (67 - len(character_list[pointer]))) + "#")
    if (pointer + 1) < number:
        pointer += 1
        print("#   10. %s" % character_list[pointer] + (" " * (66 - len(character_list[pointer]))) + "#")
    print("#                                                                         #")
    if max_pages == 0:
        print("#                                                                         #")
    elif page == 0:
        print("#   N - Next page                                                         #")
    elif page == max_pages:
        print("#                                                     P - previous page   #")
    else:
        print("#   N - Next page                                     P - previous page   #")
    print("#   B - Back to action menu                                               #")
    print("#                                                                         #")
    print("###########################################################################")
    choice = input("Type your choice here:\n")
    if choice == "B":
        day_menu()
    elif choice == "N":
        if page < max_pages:
            character_screen(character_list, (page + 1))
        else:
            print("You can't go to next page since you're currently on the last page.")
            character_screen(character_list, page)
    elif choice == "P":
        if 0 < page:
            character_screen(character_list, (page - 1))
        else:
            print("You can't go to previous page since you're currently on the first page.")
            character_screen(character_list, page)
    elif 0 < int(choice) < 11:
        pointer = int(choice) - 1 + page * 10
        character_stats(characters_c[character_list[pointer]], page)
    else:
        while True:
            print("This was not a valid option.")
            choice = input("Type your choice here:\n")
            if choice == "B":
                day_menu()
            elif choice == "N":
                if page < max_pages:
                    character_screen(character_list, (page + 1))
                else:
                    print("You can't go to next page since you're currently on the last page.")
                    character_screen(character_list, page)
            elif choice == "P":
                if 0 < page:
                    character_screen(character_list, (page - 1))
                else:
                    print("You can't go to previous page since you're currently on the first page.")
                    character_screen(character_list, page)


def character_stats(character, page):
    name = character.name
    gender = character.gender
    race = character.race
    role = character.role
    strength = character.strength
    dexterity = character.dexterity
    constitution = character.constitution
    intelligence = character.intelligence
    wisdom = character.wisdom
    charisma = character.charisma
    hp = character.hp
    temp_hp = character.temp_hp
    xp = character.xp
    print("###########################################################################")
    print("#                                                                         #")
    print("#   %s" % name + (" " * (70 - len(str(name)))) + "#")
    print("#   %s %s %s" % (gender, race, role) + (" " * (68 - len(gender) - len(race) - len(role))) + "#")
    print("#   HP: %d/%d" % (temp_hp, hp) + (" "*(64 - len(str(temp_hp)) - len(str(hp)) - len(str(xp)))) + "XP: %d #" %
          xp)
    print("#   Strength: %d" % strength + (" " * (60 - len(str(strength)))) + "#")
    print("#   Dexterity: %d" % dexterity + (" " * (59 - len(str(dexterity)))) + "#")
    print("#   Constitution: %d" % constitution + (" " * (56 - len(str(constitution)))) + "#")
    print("#   Intelligence: %d" % intelligence + (" " * (56 - len(str(intelligence)))) + "#")
    print("#   Wisdom: %d" % wisdom + (" " * (62 - len(str(wisdom)))) + "#")
    print("#   Charisma: %d" % charisma + (" " * (60 - len(str(charisma)))) + "#")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#   Press Enter to go back.                                               #")
    print("#                                                                         #")
    print("###########################################################################")
    back = input("")
    character_screen(characters, page)


def battle(field_base): #,characters, enemies
    field = copy.deepcopy(field_base)
    fieldB = copy.deepcopy(field_base)
    printableA = printable_row(field, 0) # These rows are inverted, so may be confusing
    printableB = printable_row(field, 1)
    printableC = printable_row(field, 2)
    printableD = printable_row(field, 3)
    printableE = printable_row(field, 4)
    printableF = printable_row(field, 5)
    printableG = printable_row(field, 6)
    printableH = printable_row(field, 7)
    printableI = printable_row(field, 8)
    printableJ = printable_row(field, 9)
    printableK = printable_row(field, 10)
    printableL = printable_row(field, 11)
    print("###########################################################################")
    print("#                                                    1 1 1 1 1 1 1 1 1 1 2#")
    print("#                                  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0#")
    print("#                                 #########################################")
    print("#                                A#%s#" % printableA)
    print("#                                B#%s#" % printableB)
    print("#                                C#%s#" % printableC)
    print("#                                D#%s#" % printableD)
    print("#                                E#%s#" % printableE)
    print("#                                F#%s#" % printableF)
    print("#                                G#%s#" % printableG)
    print("#                                H#%s#" % printableH)
    print("#                                I#%s#" % printableI)
    print("#                                J#%s#" % printableJ)
    print("#                                K#%s#" % printableK)
    print("# W = Wall, A-H = You, 1-8 = Ene.L#%s#" % printableL)
    print("###########################################################################")
    while True:
        print("This is a test feature. To exit, press Enter")
        start = input("Give starting coordinates separeted by space (like '10 A'): ")
        if start == "":
            break
        end = input("Give target coordinates, separated by a space: ")
        if end == "":
            break
        start_split = start.split() # These could be done in half the rows as currently, but is this way for clarity.
        end_split = end.split()
        initiator = convert_y_to_numbers(start_split)
        target = convert_y_to_numbers(end_split)
        visible = check_if_visible(fieldB, initiator, target)
        if visible == 1:
            print("Target is visible.")
            # Do attack roll 
        if visible == 0:
            print("Target is not visible.")
        
    day_menu()

def printable_row(field, row):
    # Makes map rows into one string
    printable = ""
    for i in range(len(field[row]) - 1):
        key = str(field[row].pop(0))
        printable = printable + key + "|"
    key = str(field[row].pop(0))
    printable = printable + key
    return printable


#def create_enemy(type):

def convert_y_to_numbers(coordinates):
    if coordinates[1] == "A":
        coordinates[1] = 0
    elif coordinates[1] == "B":
        coordinates[1] = 1
    elif coordinates[1] == "C":
        coordinates[1] = 2
    elif coordinates[1] == "D":
        coordinates[1] = 3
    elif coordinates[1] == "E":
        coordinates[1] = 4
    elif coordinates[1] == "F":
        coordinates[1] = 5
    elif coordinates[1] == "G":
        coordinates[1] = 6
    elif coordinates[1] == "H":
        coordinates[1] = 7
    elif coordinates[1] == "I":
        coordinates[1] = 8
    elif coordinates[1] == "J":
        coordinates[1] = 9
    elif coordinates[1] == "K":
        coordinates[1] = 10
    elif coordinates[1] == "L":
        coordinates[1] = 11
    coordinates[0] = int(coordinates[0]) - 1
    return coordinates



def play_game():
    while True:
        day_menu()


if __name__ == '__main__':
    starting_screen()
