import sys
import time

class player:
    def __init__(self, name, health, turns_tkn):
        self.name = name
        self.health = health
        self.turns_tkn = turns_tkn


active_string = ""
def type_slow():
    for char in active_string: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.09)
#gathering user's name to be used throughout the story
def name_func():
    user_name = input("what is your name? ")
    if user_name.isalpha():
        player_1 = player(user_name, 100, 0)
    else:
        print("try again")
        name_func()




name_func()
#print(turns_tkn)


#print("you're not from around these parts are you, ", name)
#print("Local legends spoke of an enormous treasure deep within the dark forest on the outskirts of the village.")
#print("The treasure was believed to be the riches from a band of successful pirates who terrorized the area until the Yeti came along.")
#print("The Yeti stands taller than 9 feet with hands the size of pumpkins.")
#print("The Yeti must have wanted to take back his lands because he drove the pirates from their treasure.")
#print("No one has ever lived to see the treasure ever since the Yeti has reclaimed the forest.")

f = open("intro_quips.txt", "r")
text_1 = print(f.readline())