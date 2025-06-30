import pygame
import random
import time
pygame.init()

WIDTH = 900
HEIGHT = 700

WIN = pygame.dispay.set_mode([WIDTH,HEIGHT])

pygame.display.set_caption('Recycle Marathon')

def change_background(image):
    background = pygame.image.load(image)
    bg = pygame.transform.scale(background,(WIDTH,HEIGHT))
    WIN.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bin.png')
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

class Nonrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('plastic.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group() #recyclable
plastic_list = pygame.sprite.Group() #non-recyclable
allsprites = pygame.sprite.Group()

bin = Bin()

allsprites.add(bin)

images = ["item1.png","item2.png","item3.png"]

for i in range(50):
    item = Recyclable(random.choice(images))

    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    
    item_list.add(item)
    allsprites.add(item)

for i in range(20):
    plastic = Nonrecyclable()

    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plastic_list.add(plastic)
    allsprites.add(plastic)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

#font to print score on screen
myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score =" + str(0), True, BLACK)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
    timeElapsed = time.time()-start_time
    if timeElapsed >=60:
        if score >= 20:
            WIN.fill("green")
            text1 = myFont.render("Bin loot successful", True,RED)
        else:
            WIN.fill(RED)
            text1 = myFont.render("Better luck nex time",True, "GREEN")
        WIN.blit(text1,(250,40))
    else:
        change_background('bground.png')
        countDown = myFont.render("Time Left:" + str(60 - int(timeElapsed)), True,WHITE)
        WIN.blit(countDown, (20,10))
        


        

        





