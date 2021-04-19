import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)
f = pygame.font.SysFont('arial', 35)
sc_text = f.render('made by zoomerroma', 1, (255, 0, 0))


pygame.display.set_caption("Cosmo-haters")
pygame.display.set_icon(pygame.image.load("images/ship.png"))



BLACK = (0, 0, 0)

W, H = 1280, 720
sc = pygame.display.set_mode((W, H))
speed = 5

bg = pygame.image.load('images/background1.png').convert_alpha()


clock = pygame.time.Clock()
FPS = 60

balls_images = ['ball1.png', 'ball2.png', 'ball3.png']
balls_surf = [pygame.image.load('images/'+path).convert_alpha() for path in balls_images]



balls = pygame.sprite.Group()

ship_surf = pygame.image.load('images/ship.png').convert_alpha()
ship_surf = pygame.transform.scale(ship_surf, (ship_surf.get_width()//2, ship_surf.get_height()//2))
ship_rect = ship_surf.get_rect(center=(W//2, H//1.25))


def createBall(group):
    indx = randint(0, len(balls_surf)-2)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], group)

x = 0
y = -400


createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)



    sc.blit(bg, (x, y))

    if y < 1:
        y += 0.7
    else:
        y -= 400

    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        ship_rect.x -= speed
        if ship_rect.x < 0:
            ship_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        ship_rect.x += speed
        if ship_rect.x > W - ship_rect.height:
            ship_rect.x = W - ship_rect.height


    sc.blit(sc_text, (850, 650))
    balls.draw(sc)
    sc.blit(ship_surf, ship_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)
