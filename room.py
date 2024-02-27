

class Room():
    def __init__(self, room_name): 
        self.name = room_name #name of the room we are in
        self.description = None #description of the room we are in
        self.linked_rooms = {} #empty dict - add some attributes and methods to handle linking multiple objects together
#you dont need to add as a param if the value is empty - like none and {}
        self.character = None

#array is an object
#dict to hold objects

    def set_character(self, new_character): #getting and setting a character in a new room
        self.character = new_character

    def get_character(self):
        return self.character



#set and get description
    def get_description(self):
        return self.description
    
    def set_description(self, new_description):
        self.description = new_description

    def describe(self):
        return self.description #instead of new_description because its not accessable
    


    #set and get the room name
    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
    


    #linking the rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link



    def get_details(self):
        print(self.name)
        print("---------------")
        print(self.description)
        
        for direction in self.linked_rooms: #for loop into a dict where direction is the key and an instance to the Room class is the value, loops thrpugh each direction and each room
            room = self.linked_rooms[direction] #if north south etc has a room linked then we get the name and direction
            print(f"The {room.get_name()} is {direction}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way!")
            return self
        
   