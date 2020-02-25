class screen:
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines
    def print_screen(self): # Maybe use \n instead of several prints?
        for line in self.lines:
            print(line)

screens_data = [ # For creating screen objects via screen class.
    ["Start_Screen",["###########################################################################",
                     "#                                                                         #",
                     "#                                                             A           #",
                     "#       A Dungeons and Dragons text-game                     / \          #",
                     "#                                                           /   \         #",
                     "#       'Delve into the depths'                            /     \        #",
                     "#                                                         /       \       #",
                     "#     Choose a number and press Enter              A     /  ____   \      #",
                     "#                                                 / \   /__/    \___\     #",
                     "#     1. New Game                                /  _\ /             \    #",
                     "#     2. Load Game                              /__/  V               \   #",
                     "#     3. Credits                               /       \               \  #",
                     "#                                             /         \               \ #",
                     "#                                            /           \               \#",
                     "#     Q. Exit Game                          /             \     v.0.0.2   #",
                     "#                                                                         #",
                     "###########################################################################"]],
    ["Credits_Screen",["###########################################################################",
                       "#                                                                         #",
                       "#       Coded by Eero 'Zhatelier' 'jarrutus' Huhtelin                     #",
                       "#                                                                         #",
                       "#       Rulesets by Wizards of the Coast                                  #",
                       "#       Implemented by Eero Huhtelin                                      #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "#                                                                         #",
                       "###########################################################################"]],
    ["New_Game",["###########################################################################",
                 "#                                                                         #",
                 "#       You're about to begin a new adventure.                            #",
                 "#       How many chatacters would you like to begin with (1-6)?           #",
                 "#                                                                         #",
                 "#       While the adventure goes on you might acquire                     #",
                 "#       more character to your party.                                     #",
                 "#                                                                         #",
                 "#              &&                                                         #",
                 "#            &&&&&&                                                       #",
                 "#       &&   &&&&&& %%                                                    #",
                 "#     &&&&&&  &&&& %%%%                                                   #",
                 "#     &&&&&&   ||  %%%%                                                   #",
                 "#      &&&&    ||  %%%%                                                   #",
                 "#       ||    &&   %%%%  &&                                               #",
                 "#       ||  &&&&&&  || &&&&&&                                             #",
                 "###########################################################################"]]
]

screens = {}

for i in range(len(screens_data)):
    screen_id = screen(screens_data[0][0],screens_data[0][1])
    screens[screens_data[0][0]] = screen_id
    screens_data.pop(0)