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

	print("\nWould you like to continue onward? (Y/N)")
	ans = input().lower()

	if ans == "y":
		encounter = random.randint(1,100)
		if encounter < 10:
			locked = True
			while locked == True:

			print("You found a chest while out adventuring! It appears to be locked...Do you want to try and unlock it? (Y/N)")
				chest = input().lower()

				if chest != "y" and chest != "n":
					print("Please enter a valid action")

				elif chest == "y":
					unlock = random.randint(1,100)

					if player.lockpicks == True:
						if unlock <= 80:
							gold = random.randint(2,10)
							player.gold = player.gold + gold
							print(f"You opened the chest! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
							locked = False
						elif unlock > 80:
							print("Unfortunately, you were not able to open the chest")
							locked = False
							continue

					elif unlock > 80:
						gold = random.randint(2,10)
						player.gold = player.gold + gold
						print(f"You opened the chest! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
						locked = False

					elif unlock <= 80:
						print("Unfortunately, you were not able to open the chest")
						locked = False
						continue

				elif chest == "n":
					continue
		elif encounter >= 10:
			battle = True

			while battle == True:
				if player.upg == 0:
					enemy_class = random.choice([Goblin, Spider])
				else:
					enemy_class = random.choice([Goblin, Spider, Orc])

				enemy = enemy_class()
				enemy_name = enemy_class.__name__

				print(f"You encounter a {enemy_name}! (A to attack)")

				enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

				while enemy.hp > 0 or player.hp > 0:
					print("Press A to attack")
					user = input().lower()

					if user != "a" and user != "y":
						print("Please enter a valid action")
						continue

					if user == "a":
						enemy.hp = enemy.hp - player.dmg
						print(f"You dealt {player.dmg} damage to the {enemy_name}!")

					if enemy.hp <= 0:
						print("The enemy is slain!")
						battle = False

						loot = random.randint(1,100)

						if loot >= 70:
							print("Whats this...? You found a health potion on the corpse! Some of your wounds have been healed!")
							player.hp = player.hp + 5
							print(f"You now have {player.hp} health.")
						else:
							gold = random.randint(1, 4)
							player.gold = player.gold + gold

							print(f"Whats this..? You found {gold} gold on the corpse!\nYou now have {player.gold} gold!")
						break

					if user == "a":
						enemy.dmg = enemy.dmg + random.choice([0, 1]) - player.ac
						player.hp = player.hp - enemy.dmg

						if enemy.dmg > 0:
							print(f"The {enemy_name} hits back! it deals {enemy.dmg} damage to you!")
						elif enemy.dmg <= 0:
							print(f"The {enemy_name}'s blow was completely deflected by your {player.armor}!")
					if player.hp <= 0:

						print(f"The {enemy_name} knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
						player.gold = 0
						print(f"You now have {player.gold} gold")
						player.hp = 6
						battle = False
						break
elif ans == "n":
		print(f"\n{player.hp} is your current health. {player.maxhp} is your maximum health currently.")
		print("You walk to the local village to stop at and rest for a while.\nThe local tavern costs 2 gold pieces to stay the night in,\nor you could go to the local marketplace and browse the various shops.\nYou can also see the steeple of a local church nearby, with it's high towers easily being the most noticeable object in the near vicinity.")
		print("\nWhere will you go? (Tavern/Market/Church)")
		village = input().lower()

        	if village == "tavern":
			print(f"The tavern is bustling with the local folk. They offer drinks for one gold piece and rooms for two gold pieces. You have {player.gold} gold.\nOne of the innkeepers asks how they can help you. (Drink/Sleep)")

			inn = input().lower()

			if inn == "sleep":
				if player.gold < 2:
					print("\nYou do not have enough gold!")
					continue

				elif player.gold >= 2:
					cost = 2
					player.gold = player.gold - cost
					print(f"You stay the night at the Tavern and heal slightly.\nYou now have {player.gold} gold left in your pockets, and your health returns to {player.maxhp} health.")
					player.hp = player.maxhp

                    	if inn == "drink":
				if player.gold < 1:
					print("You do not have enough gold!")
					continue

				elif player.gold >= 1:
					cost = 1
					player.gold = player.gold - cost
					print(f"You stop at the bar and grab yourself a mug of grog to drink.\nYou now have {player.gold} gold left in your pockets.")
					drinking_event = random.randint(1,100)

					if drinking_event > 10 and drinking_event <= 30:
						print(f"The grog is especially good tonight. Warmth fills your veins and you feel renewed with energy and vigor.")
						player.hp = player.hp + 5
						print(f"{player.hp} is your current health. {player.maxhp} is your maximum health currently.")

					elif drinking_event >30 and drinking_event <=80:

						if player.gold >= 5:
							bad_bet = random.randint(1,5)
						elif player.gold >= 2 and player.gold < 5:
							bad_bet = random.randint(1,2)
						elif player. gold < 2:
							continue
						player.gold = player.gold - bad_bet
						print(f"Drinking was not such a good idea after all...while drunk, someone snatched {bad_bet} gold from your pockets...\nYou now have only {player.gold} gold left.")

					elif drinking_event >80:
						good_bet= random.randint(1,5)
						player.gold = player.gold + good_bet
						print(f"The night was filled with laughter and many bets! You won multiple bets, totaling in {good_bet} gold.\nYou now have {player.gold} gold!")



					elif drinking_event <= 10:

                        print(f"While drunk, a tavern wench convinces you to join her in her room upstairs.\nWhile alone, she proceeds to demand all your gold and takes out a dagger.\nIt's no wench--it's a goblin in disguise!")
						enemy_class = Goblin()
						while enemy.hp > 0 or player.hp > 0:
							print("Press A to attack")
							user = input().lower()

							if user != "a" and user != "y":
								print("Please enter a valid action")
								continue

							if user == "a":
								enemy.hp = enemy.hp - player.dmg
								print(f"You dealt {player.dmg} damage to the goblin wench!")

							if enemy.hp <= 0:
								print("The enemy is slain!")

								loot = random.randint(1,100)
								if loot >= 70:
									print("Whats this...? You found a health potion on the corpse! Some of your wounds have been healed!")
									player.hp = player.hp + 5
								else:
									gold = random.randint(2, 5)
									player.gold = player.gold + gold

									print(f"Whats this..? You found {gold} gold on the corpse!")
								break











name_func()
fifty_fifty()
#print(player_1.get_name())
#type_slow()
#print(turns_tkn)

