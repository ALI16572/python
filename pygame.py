import pygame

pygame.init()

display = pygame.display.set_mode((400,500))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()

pygame.flip()            