from pygame import *
main_win = display.set_mode((700,500))
fps = 60
clock = time.Clock()
display.set_caption('Ping Pong')
running = True
while running:
    for a in event.get():
        if a.type == QUIT:
            running = False
    clock.tick(60)
    display.update()