import pgzrun
import random
import time
import math

WIDTH =610
HEIGHT= 410
card_w = 140
card_h = 190




card_f  = []
for i in range(1,5):
    card_f.append('{:02}'.format(i) + 'cardclubs')
    card_f.append('{:02}'.format(i) + 'cardhearts')
random.shuffle(card_f)

card_b = 'cardback_blue5'

card = []
count = 0
total = 0
turn_card =[]
wait_flg = False
point = 0

x = 10
y = 10

for i in range(2):
    for n in range(4):
        card.append(Actor(card_b, topleft = (x,y)))
        x += card_w + 10
    x = 10
    y += card_h + 10
 

def draw():
    screen.clear()
    if point == len(card)/2:
            message = ['Score', 'Challenge : ' + str(total), 'Rarte : ' +  str(math.floor(point/total*100)) + '%']
            for i in range(3):
                screen.draw.text(message[i], (100, 150+i*50),  color='orange', fontsize=48)
    else:
        for c in card:
            c.draw()



def on_mouse_down(pos):
    global count
    global turn_card
    global wait_flg
    if wait_flg:
        return
    
    for i in range(len(card)):
        if card[i].collidepoint(pos):
            if card[i].image == card_b:
                card[i].image =card_f[i]
                turn_card.append(card[i]) 
                count += 1

    if count == 2:
        count = 0
        clock.schedule_unique(restore, 1)
        wait_flg = True

def restore():
    global point
    global turn_card
    global wait_flg
    global total

    if turn_card[0].image[:2] != turn_card[1].image[:2]:
        turn_card[0].image = card_b
        turn_card[1].image =  card_b
    else:
        point += 1
    total += 1    
    turn_card.clear()
    wait_flg = False
            
            
pgzrun.go()
