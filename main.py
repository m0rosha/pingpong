from pygame import *
win = display.set_mode((700,500))
bkgrnd_img = image.load('kosmos-mlechnyy-put-zvezdy.jpg')
bkgrnd = transform.scale(bkgrnd_img,(700,500))
fps = 60
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, image_name,x,y,width,height,speed):
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
player1 = Player('wood.png', 20, 200,50,200,5)
player2 = Player('wood.png',500,200,50,200,5)
ball = GameSprite('ball.png',200,200,50,200,5)

display.set_caption('Ping Pong')
running = True
while running:
    win.blit(bkgrnd,(0,0))
    player2.reset()
    player1.reset()
    player1.update_1()
    player2.update_2()

    
    for a in event.get():
        if a.type == QUIT:
            running = False
    clock.tick(60)
    display.update()
