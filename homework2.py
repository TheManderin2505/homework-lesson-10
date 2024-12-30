import pgzrun
from random import randint

WIDTH = 200
HEIGHT = 100



numbers1 = randint(0,100)
numbers2 = randint(0,100)

ans = (numbers1 + numbers2)

def draw():
    screen.draw.text(str(ans),(50,50), color = "white")


pgzrun.go()