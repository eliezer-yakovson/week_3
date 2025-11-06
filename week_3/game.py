import random

from core.goblin import Goblin
from core.orc import Orc
from core.player import Regular_player


def start(): 
    #יצירת שחקנים
    player = create_player()
    monster = choose_random_monster()
    #הדפסת שמות
    player.speak()
    monster.speak()
    #הצגת תפריט(לשחק או לא)
    if show_menu() == "2":
        return
    battle(player,monster)
   


def show_menu():
    inp = input("Enter the game press 1 Exit 2")
    return inp

def create_player():
    play = Regular_player("eli")
    return play

def choose_random_monster():
    monster_list = [Orc("ori") , Goblin("jo")]
    monster = random.choice(monster_list)
    return monster

def battle(player, monster):
     #מי ראשון
    play = roll_dice(6)
    mons = roll_dice(6)
    while True:
        if play >= mons:
            attack = player.attack(monster)
            attack = monster.attack(player)
        else:
            attack = monster.attack(player)
            attack = player.attack(monster)
        if  player.hp <= 0:
            print(f"The winner is {monster.name}")
            return
        if monster.hp <= 0:
            print(f"The winner is {player.name}")
            return
        input()

def roll_dice(sides):
    return random.randint(1,sides)