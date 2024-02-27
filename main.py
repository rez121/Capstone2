from room import Room #importing the Room class
from item import Item
from character import Enemy
from character import Friend
from character import Character


print("//////////////////////////////////////")
print("WELCOME TO THE BOOTCAMP ADVENTURE GAME")
print("//////////////////////////////////////")


#kitchen object
kitchen = Room("kitchen") #these are separate objects but are using the same class type (bc reusable)
kitchen.set_description("A dank and dirty room buzzing with flies")


#ballroom object
ballroom = Room("ballroom") #room name
ballroom.set_description("A large room with ornate decorations!") #room description


#dining hall object
dining_hall = Room("dining hall")
dining_hall.set_description("The place to eat!")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")





dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I want to eat your flesh!!")
dave.set_weakness("sword")

dining_hall.set_character(dave)



sam = Friend("Sam", "A strong heroic soldier") #Task 3
sam.set_conversation("I will defeat the enemy!")
sam.set_weakness("cheese")
sam.hug_character("dave")

ballroom.set_character(sam)



#THE ITEM - Key
key = Item()
key.set_item("key")
key.set_item_description("This is the key")
key.get_item_description()







current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character() #dave is the inhabitant - checking if there is an inhabitant in the room
    if inhabitant is not None:
        inhabitant.describe()

    command = input(">")
    current_room = current_room.move(command) #move - can move in any direction based on the command i give (north, south etc)






    command = input("> ")

# Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk": #Task 1
        dave.talk()   
    elif command == "fight": #Task 1
        dave.fight()
        if dave.fight() == False: #Task 2
            print("Game has ended")
        break









    


