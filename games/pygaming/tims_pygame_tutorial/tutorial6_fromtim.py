import pygame
pygame.init()
from os.path import join

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load(join('tims_pygame_images', 'R1.png')),
pygame.image.load(join('tims_pygame_images', 'R2.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R3.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R4.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R5.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R6.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R7.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R8.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'R9.png')).convert_alpha()]

walkLeft = [pygame.image.load(join('tims_pygame_images', 'L1.png')),
pygame.image.load(join('tims_pygame_images', 'L2.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L3.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L4.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L5.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L6.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L7.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L8.png')).convert_alpha(),
pygame.image.load(join('tims_pygame_images', 'L9.png')).convert_alpha()]

bg = pygame.image.load(join('tims_pygame_images', 'bg.jpg')).convert_alpha()
char = pygame.image.load(join('tims_pygame_images', 'standing.png')).convert_alpha()

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))



class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load(join('tims_pygame_images', 'R1E.png')),
    pygame.image.load(join('tims_pygame_images', 'R2E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R3E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R4E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R5E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R6E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R7E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R8E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R9E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R10E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'R11E.png')).convert_alpha()]

    walkLeft = [pygame.image.load(join('tims_pygame_images', 'L1E.png')),
    pygame.image.load(join('tims_pygame_images', 'L2E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L3E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L4E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L5E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L6E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L7E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L8E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L9E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L10E.png')).convert_alpha(),
    pygame.image.load(join('tims_pygame_images', 'L11E.png')).convert_alpha()]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0



def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 300)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()