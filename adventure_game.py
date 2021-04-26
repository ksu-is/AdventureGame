import sys
import time

#initializing the player and the players stats for the game
class Player:
    def __init__(self, name, health, experience, turns_tkn):
        self.name = name
        self.health = health
        self.experience = experience
        self.turns_tkn = turns_tkn

#method to return amount of turns a player has taken
    def get_turns(self, turns_tkn):
        return self.turns_tkn

#method to change amount of turns tkn
    def add_turn(self, turns_tkn):
        self.turns_tkn + 1

#method to return user name for in-game replies
    def get_name(self):
        return self.name

    #def exp_check(self):
        #if self.experience >= 100:
            #code for finding the treasure
            
bear_attk = {
    "description": "you enter the dark forrest...\n a bear is charging at you!",
    "attack": "you stood your ground and attempted to attack the bear back!",
    "flee": "you ran away, saving your health but gaining little experience."
}
#print(bear_attk["attack"])
#function to simulate typing on a keyboard from the code narrator of the game
def type_slow(active_string):
    for char in active_string: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.00)

#gathering user's name to be used throughout the story
def name_func():
    user_name = input("what is your name? ")
    if user_name.isalpha():
        global player_1
        player_1 = Player(user_name.upper(), 100, 0, 0)
        type_slow("Hello " + str(player_1.name))
        intro_func()
    else:
        print("try again")
        name_func()

#intro to game
def intro_func():
    f = open("intro_quips.txt", "r")
    narrate = f.readlines()
    type_slow(narrate[0])
    input("press ENTER to continue")
    type_slow(narrate[1])
    input()
    type_slow(narrate[2])
    input()
    type_slow(narrate[3])
    input()
    type_slow(narrate[4])
    input()
    type_slow(narrate[5])
    input()
    type_slow(narrate[6])
    input()
    type_slow(narrate[7])
    input()
    type_slow(narrate[8])
    input()
    type_slow(narrate[9])
    input()
    type_slow(narrate[10])
    input()
    type_slow(narrate[11])
    input()
    type_slow(narrate[12])
    input()
    type_slow(narrate[13])
    input()
    type_slow(narrate[14])
    input()
    type_slow(narrate[15])
    input()

def fifty_fifty():
    user_ans = input(type_slow("would you like to help me find the treasure? (Y/N)")).lower()
    if user_ans == "y":
        player_1.add_turn(1)
        print(player_1.get_turns(1))
        #call next function
    elif user_ans == "n":
        print(type_slow("ok, you have a great life now? *Reiner walked away into the forrest alone*"))
    else:
        print(type_slow("try Y or N"))
        fifty_fifty()

print("You rest for a short while. You have been walking today for hours, but you've been traveling the known world for as long as you remember.\nNearby you see a small village, surrounded by the forest you are currently in.\nMaybe you will stay in this area a while, and see what is has to offer...")
while player.hp > 0:
if player.hp > player.maxhp:
		player.hp = player.maxhp








name_func()
fifty_fifty()
#print(player_1.get_name())
#type_slow()
#print(turns_tkn)

