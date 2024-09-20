#Imports
import pygame

#Initializing local packages
pygame.init()

#Decaring Game and basic screen variables

SIZE = (500,600)

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("A Projectile")

#Classes and functioms

class Player:
    def __init__(self,color,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = (self.x,self.y,self.w,self.h)
        self.path = img

    def draw(self):
        self.obj = pygame.image.load(self.path)
        WIN.blit(self.obj, self.rect)

    def Move(self):
        pass

    def GetBack(self):
        pass

player = Player()

def Redraw():
    pygame.display.update()
#main loop



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



