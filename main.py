import pygame
import random
# Sprites
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
font = pygame.font.SysFont('Sans-Serif', 45)

iFrames = 60
wasHit = False
health = 5

plane = pygame.image.load("plane.png").convert_alpha()
sky = pygame.image.load("sky.png").convert()
missile = pygame.image.load("missile.png").convert_alpha()
missileSpeed = 4
missileX = 250
missileY = 0
playerX = 250
playerY = 400

running = True
while running:
    healthText = font.render(str(health), False, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 12
        if event.key == pygame.K_RIGHT:
            playerX += 12

    if missileY > 500:
        missileY = -25
        missileX = random.randint(25,475)
        missileSpeed += 1
    screen.blit(sky, (0,0))


    screen.blit(missile, (missileX, missileY),)
    missileY += missileSpeed

    screen.blit(plane, (playerX, playerY),)

    screen.blit(healthText, (50,40))

    if playerX > missileX - 30 and playerX < missileX + 60 and playerY > missileY - 10 and playerY < missileY + 25 and iFrames > 59:
        print("HIT")
        wasHit = True
        health -= 1
    
    if wasHit == True:
        if iFrames > 0:
            iFrames -= 1
        elif iFrames <= 0:
            iFrames = 60
            wasHit = False

    pygame.display.flip()

    clock.tick(60)
pygame.quit()