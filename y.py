import pygame

class Player:
    def __init__(self, speet, width, height, x, y, skin):
        self.textura = pygame.image.load(skin)
        self.textura = pygame.transform.scale(self.textura, [width, height])
        self.hitbox = self.textura.get_rect()
        self.hitbox.x - x
        self.hitbox.y = y
        self.speet = speet



    def draw(self, window):
        window.blit(self.textura, self.hitbox)


class Wall:
    def __init__(self, width, height, x, y, color):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color


    def draw(self, window):
        pygame.draw.rect(window, self.color,self.hitbox)



pygame.init()


window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background,[700, 500])

game = True


walls = [
    Wall(100, 20,80, 70,[123, 123, 123] )
]

player =  Player(10, 50, 50, 250, 260, "hero.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x, y)
    window.fill([255, 0, 0])
    window.blit(background, [0,0])
    player.draw(window)
    pygame.display.flip()

    for wall in walls:
        wall.draw(window)
    pygame.display.flip()

    fps.tick(60)


