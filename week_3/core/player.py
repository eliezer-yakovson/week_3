#from game import *

import random

class Player:
    def __init__(self, name, hp, speed, power, rating_armor):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.rating_armor = rating_armor

    def speak():
        pass
    def attack():
        pass

    @staticmethod
    def roll_dice(sides):
        return random.randint(1,sides)

class Regular_player(Player):
    def __init__(self, name):
        data = ["fighter", "cure"]
        self.profession = random.choice(data)
        hp = 50
        if self.profession == "cure":
            hp += 10
        speed = random.randint(5,10)
        power = random.randint(5,10)
        if self.profession == "fighter":
            power+=2
        rating_armor = random.randint(5,15)
        super().__init__(name, hp, speed, power, rating_armor)

    def speak(self):
        print(f"name: {self.name}")

    def attack(self, other):
        print(f"The player is now {self.name}")
        sum_play_current = Player.roll_dice(20) +  self.speed
        if sum_play_current < other.rating_armor:
            print("Attack failed")
            return 
        sum_play_other = Player.roll_dice(6) +  other.power
        other.hp -= sum_play_other
        print(f"attack player: {sum_play_current}, protection_monster: {other.rating_armor}")
        print(f"Damage amount: {sum_play_other} How much is left to monster: {other.hp}")



