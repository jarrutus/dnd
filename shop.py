

def shopping_screen(money, items):
    coins = divide_money(money)
    length = length_of_coins(coins)
    print("###########################################################################")
    print("#   Your money: %d GP %d SP %d CP" % (coins[0],coins[1],coins[2]) + (" " * (47 - length)) + "#")
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
    print("#                                                                         #")
    print("#                                                                         #")
    print("#                                                                         #")
    print("#   B - Back to Day Menu                                                  #")
    print("###########################################################################")
    

def divide_money(money):
    """Divides total money into Gold, Silver and copper pieces, 1 GP = 100 SP = 10 000 CP."""
    non_gold = money % 10000
    gold = int(money/10000)
    copper = non_gold % 100
    silver = int(non_gold/100)
    coins = [gold,silver,copper]
    return coins

def length_of_coins(coins):
    """Takes the numbers of coins, calculates the length of the strings for printing purposes."""
    gold_length = len(str(coins[0]))
    silver_length = len(str(coins[1]))
    copper_length = len(str(coins[2]))
    length = gold_length + silver_length + copper_length
    return length
    
def get_shop_items(freedom_score):
    items = [] #placeholder
    return items