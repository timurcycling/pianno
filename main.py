from pygame import* 
from settings import WINDOW_WIDTH,WINDOW_HEIGHT, WHITE 

init() 
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
running = True 
while running: 
    for e in event.get(): 
        if e.type == QUIT: 
            running = False 
    screen.fill(WHITE) 
    display.update() 