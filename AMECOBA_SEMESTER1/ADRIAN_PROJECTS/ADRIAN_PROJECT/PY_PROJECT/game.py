import pygame

pygame.init()

win  = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygameでオブジェクトを動かす")

x = 50
y  = 50

height = 50
width = 50

vel = 5


run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT]:
        x -= vel
    if keys [pygame.K_RIGHT]:
        x += vel
    if keys [pygame.K_UP]:
        y -= vel
    if keys [pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.circle(win, (128,0,250), (x, y), height, width)
    pygame.display.update()
pygame.quit()

