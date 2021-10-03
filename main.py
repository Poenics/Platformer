import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()
pygame.display.set_caption(random.choice(["Snek","Your mom sucks", "You stink", "10% Bug free", "no", "wait, this isn't minecraft?"]))


def run():

    x = 69
    y = 300
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            x += 5

        y += 1
        x += 1


        screen.fill((50, 50, 50))
        #screen.blit(pygame.image.load("back.png"), (0,0))




        pygame.draw.rect(screen, (20, 255, 0), (200, 300, 20, 20))

        pygame.draw.rect(screen, (255, 0, 0), (x, y, 20, 20))



        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    run()
