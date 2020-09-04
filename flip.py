import random
import math

money = 10
gain = 1
win_percentage = 0.6
kelly = (win_percentage * gain - (1 - win_percentage)) / gain * money

def flip(bet, win_percentage):
    global money
    global kelly
    if random.random() <= win_percentage:
        money += bet
    else:
        money -= bet
    kelly = (win_percentage * gain - (1 - win_percentage)) / gain * money
    print(money)

while money > 0:
    flip(kelly, win_percentage)