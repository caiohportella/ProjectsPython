import pygame

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Draw a line')
screen.fill((0, 0, 0))
pygame.draw.line(screen, (100,0,255), (20,20), (70,80), 2)
pygame.display.flip()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False