import pygame
import math
import random


pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
running = True
gravity = 2
Bounce = -0.9
Friction = 0.9
ClickDown = 0
ClickUp = 0
MoveVektorX = 0
MoveVektorY = 0
JumpForce = 0.1
AY = (0,1)

class Player:
    def __init__(self,x,y,radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0

    def DrawPlayer(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
    def UpdatePosition(self):
        self.vy += gravity
        self.y += self.vy 
        self.x += self.vx
    def Collision(self, O, closest_x, closest_y, x, y, distance):
        AB = (closest_x - x, closest_y - y)
        skalar = AY[0] * AB[0] + AY[1] * AB[1]
        if self.vx < 0:
            R_Vektor = (-1,0)
        else:
            R_Vektor = (1,0)
        skalar2 = R_Vektor[0] * AB[0] + R_Vektor[1] * AB[1]
        angle = math.degrees(math.acos(skalar/distance))
        angle2 = math.degrees(math.acos(skalar2/distance))
        if angle == 0:
            self.y = O.y - self.radius
            self.vy = self.vy * Bounce
            self.vx = self.vx * Friction
        if angle == 180:
            self.y = O.y + O.height + self.radius
            self.vy = self.vy * Bounce
            self.vx = self.vx * Friction
        if angle == 90:
            self.vx = self.vx * Bounce
        elif angle < 90 and angle != 0:
            if angle2 > 90:
                self.y = O.y - self.radius
                self.vy = self.vy * Bounce
            else:
                self.y = O.y - self.radius
                self.vy = self.vy * Bounce
                self.vx = self.vx * Bounce
        elif angle > 90 and angle != 180:
            if angle2 > 90:
                self.y = O.y + O.height + self.radius
                self.vy = self.vy * Bounce
            else:
                self.y = O.y + O.height + self.radius
                self.vy = self.vy * Bounce
                self.vx = self.vx * Bounce

        if abs(self.vy) < 1:
            self.vy = 0
        if abs(self.vx) < 1:
                self.vx = 0
        print(angle)
    def Jump(self, vx, vy):
        self.vy += vy * JumpForce
        self.vx += vx * JumpForce

class Object:
    def __init__(self,x,y,color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
    def DrawObject(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def Mouse(self, pos):
        self.x, self.y = pos



class Platform(Object):

    def __init__(self, color):
        x = random.randint(0, 300)
        y = random.randint(100, 500)
        width = random.randint(40, 100)
        color = color
        height = 40
        super().__init__(x, y, color, width, height)
    
    


def HitBox(O, x, y):
    Status = False
    closest_x = max(O.x, min(x, O.x + O.width))
    closest_y = max(O.y, min(y, O.y + O.height))
    dx = x - closest_x
    dy = y - closest_y
    distance = math.sqrt(dx**2 + dy**2)
    if distance <= P1.radius:
        P1.Collision(O, closest_x, closest_y, x, y, distance)
        Status = True
    return Status

def PlayerPositionAtTime(t):
    x = P1.x + P1.vx * t
    y = P1.y + P1.vy * t + 0.5 * gravity * t**2
    return x, y

 
P1 = Player(200,200,20,(255,255,255))
O1 = Object(150,400,(0,255,0),100,100)
O2 = Object(0,580,(0,255,0),400,20)
O3 = Object(0,530,(0,255,0),20,70)
O4 = Object(380,530,(0,255,0),20,70)
pl1 = Platform("blue")
pl2 = Platform("white")
pl3 = Platform("gray")


Objects = [O1,O2,O3,O4, pl1, pl2, pl3]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ClickDown = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            ClickUp = event.pos
            MoveVektorX = ClickUp[0] - ClickDown[0]
            MoveVektorY = ClickUp[1] - ClickDown[1]
            P1.Jump(MoveVektorX, MoveVektorY)
    P1.UpdatePosition()
    #O1.Mouse(pygame.mouse.get_pos())
    for object in Objects:
        object.DrawObject()

    for O in Objects:
        for t in range(11):
            x, y = PlayerPositionAtTime(t/10)
            Status = HitBox(O, x, y)
            if Status:
                break
    
    P1.DrawPlayer()
    pygame.display.flip()
    screen.fill("black")
    clock.tick(60) 

pygame.quit()
