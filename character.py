#create a character

class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

#describe character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

#set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

#talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

#fight with this character
    def fight(self, combat_items):
        print(self.name + " doesn't want to fight with you")
        return True




class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_items):
        if combat_items == self.weakness:
            print("you fend " + self.name + " off with the " + combat_items)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
        


class Friend(Character): #Task 3
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def hug_character(self, h_character): #Task 4
        hug = "🤗"
        hugged_character = hug + h_character + hug
        print(hugged_character)
    
    
        
