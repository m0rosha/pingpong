from pygame import *
win = display.set_mode((700,500))
bkgrnd_img = image.load('kosmos-mlechnyy-put-zvezdy.jpg')
bkgrnd = transform.scale(bkgrnd_img,(700,500))
fps = 60
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, image,x,y,width,height,speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y
        self.width = width
        self.height = height
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed 
    def update_2(self):
        keys = key.get_pressed()
        if keys [K_UP]:
            self.rect.y -= self.speed
        if keys [K_DOWN]:
            self.rect.y += self.speed 



display.set_caption('Ping Pong')
running = True
while running:
    win.blit(bkgrnd,(0,0))
    
    for a in event.get():
        if a.type == QUIT:
            running = False
    clock.tick(60)
    display.update()
