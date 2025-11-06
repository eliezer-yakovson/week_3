from core.orc import Orc
from core.player import Player
import random

#from game import *


class Goblin(Orc):
    def __init__(self,name):
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.rating_armor = 1
        super().__init__(name)

    def speak(self):
        print(f"the {self.type} {self.name} is angry")

    

