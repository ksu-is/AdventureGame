import sys
import time

#initializing the player and the players stats for the game
class Player:
    turns_tkn = 0
    def __init__(self, name, health, xp):
        self.name = name
        self.health = 50
        self.xp = 0
        self.__class__.turns_tkn += 1
       
    #method to return user name for in-game replies
    def get_name(self):
        return self.name
         
#dictionary objects used for storing dialogue
bear_attk_dict = {
    "description": "You and Reiner set off into the forrest seeking the treaure...\nWhats that?... a bear is charging at you!",
    "attack": "you stood your ground and attempted to attack the bear back!",
    "run": "you ran away, saving your health but gaining little experience."
}

tornado_dict = {
    "description": "you look into the distance...\nis that a tornado coming closer to us!?",
    "attack": "you looked around for cover and found a sturdy rock cave to duck into!",
    "run": "you ran as fast as you could away from the tornado but you \nsuffered a blow from a tree limb!"
}

angry_bees_dict = {
    "description": "you hear a strange buzzing sound nearing your location.\na ton of angry bees are flying at you!",
    "attack": "you tried to flail your arms all around to try and kill the bees.\nthis attempt did not work very well.",
    "run": "you ran away from the bees, saving yourself from stings."
}

traitor_dict = {
    "description": "Reiner pulled out a sword!\nI fooled you so I could kill and rob you!",
    "attack": "you lunged at Reiner and tried\nto break the sword away from him.\nYou did it!",
    "run": "you tried to run away from him but he cut you down!"
}


#death by injury function ends game
def death_func():
    if player_1.health <= 0:
        f = open("intro_quips.txt", "r")
        narrate = f.readlines()
        type_slow(narrate[16])
        input()
        type_slow(narrate[17])
        print(player_1.name+", you ended the game with:",player_1.xp,"points!")
        sys.exit()
        

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
        player_1 = Player(user_name.upper(), 50, 0)
        type_slow("[You begin the game with 0 xp and 50 health.]\n")
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
    input("press ENTER after each line to continue")
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
    print("\n")
    fifty_fifty()

#first game decision is made
def fifty_fifty():
    user_ans = input(type_slow("Reiner: Would you like to help me find the treasure? (Y/N)\n")).lower()
    if user_ans == "y":
        player_1.turns_tkn += 1
        bear_attk()
    elif user_ans == "n":
        type_slow("Reiner: Ok, you have a great life now.\n*Reiner walked away into the forrest alone*\n")
        type_slow("The End.")
        sys.exit()
    else:
        type_slow("(try Y or N)\n")
        fifty_fifty()

#second game event takes place
def bear_attk():

    death_func()
    f = open("event_quips.txt", "r")
    narrate = f.readlines()
    type_slow(bear_attk_dict["description"])
    input()
    bear_inpt = input(type_slow("Quick!, do you want to run or fight?\n")).lower()
    if bear_inpt == "fight":
        player_1.turns_tkn += 1
        player_1.health -= 30
        player_1.xp += 15
        type_slow(bear_attk_dict["attack"])
        print("\n")
        type_slow(narrate[0])
        type_slow(narrate[1])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        tornado_time()
    elif bear_inpt == "run":
        player_1.turns_tkn += 1
        player_1.xp += 5
        type_slow(bear_attk_dict["run"])
        print("\n")
        type_slow(narrate[2])
        type_slow(narrate[3])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        tornado_time()
    else:
        print("you have to decide now!")
        bear_attk()

#third game event takes place
def tornado_time():
    death_func()
    input()
    f = open("event_quips.txt", "r")
    narrate = f.readlines()
    type_slow(tornado_dict["description"])
    input()
    tornado_inpt = input(type_slow("Quick!, do you want to run or find shelter?\n")).lower()
    if tornado_inpt == "find shelter":
        player_1.turns_tkn += 1
        player_1.xp += 10
        type_slow(tornado_dict["attack"])
        print("\n")
        type_slow(narrate[4])
        type_slow(narrate[5])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        angry_bees()
    elif tornado_inpt == "run":
        player_1.turns_tkn += 1
        player_1.health -= 20
        player_1.xp += 2
        type_slow(tornado_dict["run"])
        print("\n")
        type_slow(narrate[6])
        type_slow(narrate[7])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        angry_bees()
    else:
        type_slow("you have to decide now!")
        tornado_time()
#fourth game event takes place
def angry_bees():
    death_func()
    input()
    f = open("event_quips.txt", "r")
    narrate = f.readlines()
    type_slow(angry_bees_dict["description"])
    input()
    bees_inpt = input(type_slow("Quick!, do you want to run or try to fight the bees?\n")).lower()
    if bees_inpt == "fight":
        player_1.turns_tkn += 1
        player_1.health -= 10
        player_1.xp += 13
        type_slow(angry_bees_dict["attack"])
        print("\n")
        type_slow(narrate[8])
        type_slow(narrate[9])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        traitor_event()
    elif bees_inpt == "run":
        player_1.turns_tkn += 1
        player_1.xp += 20
        type_slow(angry_bees_dict["run"])
        print("\n")
        type_slow(narrate[10])
        type_slow(narrate[11])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        traitor_event()
    else:
        type_slow("you have to decide now!")
        angry_bees()

#fifth game event takes place
def traitor_event():
    death_func()
    input()
    f = open("event_quips.txt", "r")
    narrate = f.readlines()
    type_slow(traitor_dict["description"])
    input()
    traitor_inpt = input(type_slow("Quick!, do you want to run or fight!?\n")).lower()
    if traitor_inpt == "fight":
        player_1.turns_tkn += 1
        player_1.xp += 30
        player_1.health -= 20
        type_slow(traitor_dict["attack"])
        print("\n")
        type_slow(narrate[12])
        type_slow(narrate[13])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        death_func()
        defeat_reiner()
    elif traitor_inpt == "run":
        player_1.turns_tkn += 1
        player_1.health -= 50
        player_1.xp += 8
        type_slow(traitor_dict["run"])
        print("\n")
        type_slow(narrate[14])
        type_slow(narrate[15])
        type_slow("your current health is: "+str(player_1.health))
        print("\n")
        death_func()
    else:
        type_slow("you have to decide now!")
        traitor_event()
        
#final function called
def defeat_reiner():
    f = open("intro_quips.txt", "r")
    narrate = f.readlines()
    type_slow(narrate[18])
    input()
    type_slow(narrate[19])
    input()
    type_slow(narrate[20])
    input()
    type_slow(narrate[21])
    input()
    type_slow(narrate[22])
    input()
    type_slow(narrate[23])
    input()
    type_slow(narrate[24])
    input()
    type_slow(narrate[25])
    input()
    sys.exit(str(player_1.name)+", you earned: "+str(player_1.xp)+" points.")

name_func()


