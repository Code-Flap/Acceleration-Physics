#imports
import pygame

#Initializing pygame
pygame.init()

#SEtting up screen
SIZE = (500,600)
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Projectile")
fps = 60
vel = 0.00005
velocity = 0
i = 0
#classes and functions

class Bullet:
    def __init__(self,color,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.released = False
    #Displaying the object
    def DrawObj(self):
        pygame.draw.rect(WIN, self.color, self.rect)

    def Move(self):
        global velocity, vel, i

        if self.released:
            pass
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                velocity -= vel

            elif keys[pygame.K_d]:
                velocity += vel

            else:
                if velocity > 0.005:
                    velocity -= 0.0001
                    if velocity < 0.005:
                        velocity=0

                elif velocity < -0.005:
                    velocity += 0.0001
                    if velocity > -0.005:
                        velocity=0

            self.x += velocity


            if keys[pygame.K_s]:
                velocity = 0


            self.rect = (self.x, self.y, self.width, self.height)
            i+=1

        # k = pygame.key.

    def GetBack(self):
        if self.x > 500:
            self.x = 0

        elif self.x < -25:
            self.x = 500

        self.rect = (self.x, self.y, self.width, self.height)

        if self.y < 0:
            global shooter
            self.y = 550
            self.x = shooter.x+10
            self.rect = (self.x, self.y, self.width, self.height)
            self.released = False



    def Released(self):
        if self.released:
            self.y -= 0.5
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.released = True




class Shooter:
    def __init__(self,color,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
    #Displaying the object
    def DrawObj(self):
        pygame.draw.rect(WIN, self.color, self.rect)



    def Move(self):
        global velocity, vel, i

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            velocity -= vel


        elif keys[pygame.K_d]:
            velocity += vel

        else:
            if velocity > 0.005:
                velocity -= 0.0001
                if velocity < 0.005:
                    velocity=0

            elif velocity < -0.005:
                velocity += 0.0001
                if velocity > -0.005:
                    velocity=0


        self.x += velocity



        if keys[pygame.K_s]:
            velocity = 0


        self.rect = (self.x, self.y, self.width, self.height)
        i+=1

        # k = pygame.key.

    def GetBack(self):
        if self.x > 500:
            self.x = 0

        elif self.x < -25:
            self.x = 500

        self.rect = (self.x, self.y, self.width, self.height)


class Enemy:
    def __init__(self):
        self.level = 0
    def making_Level(self):
        if self.level == 0:
            print("Blah")


# Window RE DRAW FUNCTION/Part of the main screen updating loop
def redrawWindow(player,bullet):
    WIN.fill((255,255,255))
    player.DrawObj()
    bullet.DrawObj()
    pygame.display.update()



#Loop for updating and displaying Entities on the Screen
shooter = Shooter("red",x=260,y=550,width=25,height=25)
bullet = Bullet('black',x=270,y=550,width=5,height=10)

run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawWindow(shooter,bullet)
    shooter.Move()
    shooter.GetBack()
    bullet.Move()
    bullet.GetBack()
    bullet.Released()


