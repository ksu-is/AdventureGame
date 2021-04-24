import sys
import time

#initializing the player and the players stats for the game
class player:
    def __init__(self, name, health, turns_tkn):
        self.name = name
        self.health = health
        self.turns_tkn = turns_tkn

#function to simulate typing on a keyboard from the code narrator of the game
def type_slow(active_string):
    for char in active_string: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.09)
#gathering user's name to be used throughout the story
def name_func():
    user_name = input("what is your name? ")
    if user_name.isalpha():
        player_1 = player(user_name.upper(), 100, 0)
        type_slow("Hello " + str(player_1.name))
        intro_func()
    else:
        print("try again")
        name_func()

#intro to 
def intro_func():
    f = open("intro_quips.txt", "r")
    narrate = f.readlines()
    type_slow(narrate[0])
    type_slow(narrate[1])
    type_slow(narrate[2])
    type_slow(narrate[3])
    type_slow(narrate[4])
    type_slow(narrate[5])
    type_slow(narrate[6])
    type_slow(narrate[7])



name_func()

#type_slow()
#print(turns_tkn)

