import os

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.score = 0
        self.deadcounter = 0

    def add_score(self, score):
        self.score  += score

    def sub_score(self, score):
        self.score  -= score
        if self.score < 0:
            self.score = 0

    def sub_hp(self, hp):
        self.hp -= hp

    def revive(self):
        self.hp = 100

    def died(self):
        self.deadcounter += 1
    def is_dead(self):
        if self.hp <= 0:
            return 1
        return 0

name = input("Please write your name\n")
player = Player(name)

# This only works for linux ; Use os.system('CLS') for windows
os.system("clear")

while (player.hp > 0):
    print("Welcome " + player.name + " to the most hard game ever!")




    if player.is_dead():
        player.died()
        die_input = input("You died. Type 1 to start again. Any other to exit\n")
        if die_input == "1":
            player.revive()