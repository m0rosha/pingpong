from pygame import *
win = display.set_mode((700,500))
bkgrnd_img = image.load('kosmos-mlechnyy-put-zvezdy.jpg')
bkgrnd = transform.scale(bkgrnd_img,(700,500))
fps = 60
clock = time.Clock()

display.set_caption('Ping Pong')
running = True
while running:
    win.blit(bkgrnd,(0,0))
    
    for a in event.get():
        if a.type == QUIT:
            running = False
    clock.tick(60)
    display.update()