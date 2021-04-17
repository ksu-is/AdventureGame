name = ()

health = (100)
stamina = (20)
hunger = (10)

turns_tkn = (0)

#gathering user's name to be used throughout the story
def name_func():
    user_name = input("what is your name? ")
    if user_name.isalpha():
        name = user_name
        print("Ahh, good to meet you", name, "I am Reiner")
        print("you're not from around these parts are you, ", name)
        print("Its dangerous out here to be alone")
        print("Local legends spoke of an enormous treasure deep within the dark forest on the outskirts of the village.")
        print("The treasure was believed to be the riches from a band of successful pirates who terrorized the area until the Yeti came along.")
        print("The Yeti stands taller than 9 feet with hands the size of pumpkins.")
        print("The Yeti must have wanted to take back his lands because he drove the pirates from their treasure.")
        print("No one has ever lived to see the treasure ever since the Yeti has reclaimed the forest.")
    else:
        print("try again")
        name_func()
name_func()


#first choice is an opportunity to replenish user health
choice_1 = input("Do you want to come into town with me to warm up and get some food. (Y/N)")

