import random
import math

money = 10
win_percentage = 0.500000000001
kelly = (win_percentage - (1 - win_percentage)) * money

def flip(bet, win_percentage):
    global money
    global kelly
    if random.random() <= win_percentage:
        money += bet
    else:
        money -= bet
    kelly = (win_percentage - (1 - win_percentage)) * money
    print(money)

while money > 0:
    flip(kelly, win_percentage)