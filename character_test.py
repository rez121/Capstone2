from character import Enemy
from character import Friend



dave = Enemy("Dave", "A smelly zombie") 
dave.describe()
dave.set_conversation("I want to eat your flesh")
dave.talk()
dave.set_weakness("sword")



sam = Friend("Sam", "A strong heroic soldier")
sam.set_conversation("I will defeat the enemy!")
sam.talk()
sam.set_weakness("cheese")
sam.hug_character("dave") #Task 4

weapon = print("what will you fight with?")
fight_with = input()
dave.fight(fight_with)

weapon = print("what will you fight with?")
fight_with = input()
sam.fight(fight_with)




