import pygame
import random
# Sprites
pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 4
        if event.key == pygame.K_RIGHT:
            playerX += 4

    if missileY > 550:
        missileY = -50
        missileX = random.randint(25,475)
        missileSpeed += 1
    screen.blit(sky, (0,0))


    screen.blit(missile, (missileX, missileY),)
    missileY += missileSpeed

    screen.blit(plane, (playerX, playerY),)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
