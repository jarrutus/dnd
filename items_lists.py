class weapon: # WIP, will need to add in more structure, damage rolls etc.
    def __init__(self,data): # Data is a list of the weapon's attributes: [name, damage, 1H_or_2H, range, attribute, base_price]
        self.name = data[0]
        self.hit_dice = data[1].split("D") #hit_dice[0] is number of dice, [1] determines the dice used, D6, D8 etc.
        self.versatility = data[2]
        
    def roll_damage(hands):
        damage = 0
        max_damage = int(self.hit_dice[1])
        if self.versatility == "Both" and hands == 2:
            max_damage += 2
        for i in range(int(self.hit_dice[0])):
            damage += random.randint(1,max_damage)
        return damage
    
# The Prices will need to be balanced, currently merely placeholders.
ranges = [[0,0],[20,60],[30,120],[80,320],[100,400],[150,600]]

weapon_data = { #template "Weapon":{"Damage":"1D6","Hands":"1H","Range":0,"Attribute":"STR","Price":50} // Removed Thrown:Y/N since Range already does the same. 
    # Prices need a lot of balancing, currently just placeholders
    # Simple Melee Weapons
    "Club":{"Damage":"1D6","Hands":"1H","Range":0,"Attribute":"STR","Price":50},
    "Dagger":{"Damage":"1D4","Hands":"1H","Range":1,"Attribute":"S/D","Price":75},
    "Greatclub":{"Damage":"1D8","Hands":"2H","Range":0,"Attribute":"STR","Price":100},
    "Handaxe":{"Damage":"1D6","Hands":"1H","Range":1,"Attribute":"STR","Price":100},
    "Javelin":{"Damage":"1D6","Hands":"1H","Range":2,"Attribute":"STR","Price":120},
    "Light Hammer":{"Damage":"1D4","Hands":"1H","Range":1,"Attribute":"STR","Price":75},
    "Mace":{"Damage":"1D6","Hands":"1H","Range":0,"Attribute":"STR","Price":150},
    "Quarterstaff":{"Damage":"1D6","Hands":"Both","Range":0,"Attribute":"STR","Price":60},
    "Sickle":{"Damage":"1D4","Hands":"1H","Range":0,"Attribute":"STR","Price":60},
    "Spear":{"Damage":"1D6","Hands":"Both","Range":1,"Attribute":"STR","Price":75},
    # Simple Ranged Weapons
    "Light Crossbow":{"Damage":"1D8","Hands":"2H","Range":3,"Attribute":"DEX","Price":500},
    "Dart":{"Damage":"1D4","Hands":"1H","Range":1,"Attribute":"S/D","Price":5},
    "Shortbow":{"Damage":"1D6","Hands":"1H","Range":3,"Attribute":"DEX","Price":500},
    "Sling":{"Damage":"1D4","Hands":"1H","Range":0,"Attribute":"STR","Price":50},
    # Martial Melee Weapons
    "Battleaxe":{"Damage":"1D8","Hands":"Both","Range":0,"Attribute":"STR","Price":300},
    "Flail":{"Damage":"1D8","Hands":"1H","Range":0,"Attribute":"STR","Price":275},
    "Glaive":{"Damage":"1D10","Hands":"2H","Range":0,"Attribute":"STR","Price":350},
    "Greataxe":{"Damage":"1D12","Hands":"2H","Range":0,"Attribute":"STR","Price":450},
    "Greatsword":{"Damage":"2D6","Hands":"2H","Range":0,"Attribute":"STR","Price":500},
    "Halberd":{"Damage":"1D10","Hands":"2H","Range":0,"Attribute":"STR","Price":350},
    "Lance":{"Damage":"1D12","Hands":"2H","Range":0,"Attribute":"STR","Price":450}, # Will need some special rules if and when mounted combat is a thing.
    "Longsword":{"Damage":"1D8","Hands":"Both","Range":0,"Attribute":"STR","Price":300},
    "Maul":{"Damage":"2D6","Hands":"2H","Range":0,"Attribute":"STR","Price":250},
    "Morningstar":{"Damage":"1D8","Hands":"1H","Range":0,"Attribute":"STR","Price":275},
    "Pike":{"Damage":"1D10","Hands":"2H","Range":0,"Attribute":"STR","Price":250},
    "Rapier":{"Damage":"1D8","Hands":"1H","Range":0,"Attribute":"S/D","Price":325},
    "Scimitar":{"Damage":"1D6","Hands":"1H","Range":0,"Attribute":"S/D","Price":300},
    "Shortsword":{"Damage":"1D6","Hands":"1H","Range":0,"Attribute":"S/D","Price":300},
    "Trident":{"Damage":"1D6","Hands":"Both","Range":1,"Attribute":"STR","Price":250},
    "War Pick":{"Damage":"1D8","Hands":"1H","Range":0,"Attribute":"STR","Price":250},
    "Warhammer":{"Damage":"1D8","Hands":"Both","Range":0,"Attribute":"STR","Price":275},
    "Whip":{"Damage":"1D4","Hands":"1H","Range":0,"Attribute":"S/D","Price":150},
    # Martial Ranged Weapons
    "Hand Crossbow":{"Damage":"1D6","Hands":"1H","Range":2,"Attribute":"DEX","Price":500},
    "Heavy Crossbow":{"Damage":"1D10","Hands":"2H","Range":4,"Attribute":"DEX","Price":400},
    "Longbow":{"Damage":"1D8","Hands":"2H","Range":5,"Attribute":"DEX","Price":400}
    }

armor_data = { # Template "Armor":{"Base_AC":10,"Bonus":"DEX","Strength":0,"Stealth":0,"Price":0} // Strength = min STR to use, Stealth = penalty for stealth.
    # Light Armor
    "Clothing":{"Base_AC":10,"Bonus":"DEX","Strength":0,"Stealth":0,"Price":0},
    "Padded":{"Base_AC":11,"Bonus":"DEX","Strength":0,"Stealth":1,"Price":0},
    "Leather":{"Base_AC":11,"Bonus":"DEX","Strength":0,"Stealth":0,"Price":0},
    "Studded Leather":{"Base_AC":12,"Bonus":"DEX","Strength":0,"Stealth":0,"Price":0},
    # Medium Armor
    "Hide":{"Base_AC":12,"Bonus":"DEX2","Strength":0,"Stealth":0,"Price":0},
    "Chain Shirt":{"Base_AC":13,"Bonus":"DEX2","Strength":0,"Stealth":0,"Price":0},
    "Scale Mail":{"Base_AC":14,"Bonus":"DEX2","Strength":0,"Stealth":1,"Price":0},
    "Breastplate":{"Base_AC":14,"Bonus":"DEX2","Strength":0,"Stealth":0,"Price":0},
    "Half Plate":{"Base_AC":15,"Bonus":"DEX2","Strength":0,"Stealth":1,"Price":0},
    # Heavy Armor
    "Ring Mail":{"Base_AC":14,"Bonus":"None","Strength":0,"Stealth":1,"Price":0},
    "Chain Mail":{"Base_AC":16,"Bonus":"None","Strength":13,"Stealth":1,"Price":0},
    "Splint":{"Base_AC":17,"Bonus":"None","Strength":15,"Stealth":1,"Price":0},
    "Plate":{"Base_AC":18,"Bonus":"None","Strength":15,"Stealth":1,"Price":0},
    # Shield
    "Shield":{"Base_AC":2,"Bonus":"None","Strength":0,"Stealth":0,"Price":0}
    }
    
basic_general_items = [ # List is incomplete.
        ["Torch",10],["Rope",25]
    ]

list_simple_weapons = ["Club","Dagger","Greatclub","Handaxe","Javelin","Light Hammer","Mace","Quarterstaff","Sickle","Spear"]
list_simple_ranged = ["Light Crossbow","Dart","Shortbow","Sling"]
list_martial_weapons = ["Battleaxe","Flail","Glaive","Greataxe","Greatsword","Halberd","Lance","Longsword","Maul","Morningstar","Pike","Rapier","Scimitar","Shortsword","Trident","War Pick","Warhammer","Whip"]
list_martial_weapons_1H = ["Battleaxe","Flail","Longsword","Morningstar","Rapier","Scimitar","Shortsword","Trident","War Pick","Warhammer","Whip"]
list_martial_ranged= ["Hand Crossbow","Heavy Crossbow","Longbow"]