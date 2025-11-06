import random

from core.player import Player
#from game import *


class Orc(Player):
    def __init__(self,name):
        self.type = "orc"
        type_weapon = ["Knife", "Sword", "Axe"]
        self.weapon = random.choice(type_weapon)
        speed = random.randint(0,5)
        power = random.randint(10,15)
        rating_armor = random.randint(2,8)
        super().__init__(name, 50, speed, power, rating_armor)

    def speak(self):
        print(f"name: {self.name}, type: {self.type}")


    def attack(self, other):
        print(f"The player is now {self.name}")
        multiplication_amount = {"Knife":0.5, "Sword":1, "Axe":1.5}
        sum_play_current = Player.roll_dice(20) +  self.speed 
        if sum_play_current < other.rating_armor:
            print("Attack failed")
            return 
        sum_play_other = (Player.roll_dice(6) +  other.power) * multiplication_amount[self.weapon]
        other.hp -= sum_play_other
        print(f"attack monster: {sum_play_current}, protection player: {other.rating_armor}")
        print(f"Damage amount: {sum_play_other} How much is left to player: {other.hp}")