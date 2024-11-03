import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
RED = pygame.Color('red')
WHITE = pygame.Color('white')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
GREEN = pygame.Color('green')
PURPLE = pygame.Color('purple')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        # Check for boundary collisions
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE))

    def change_color(self):
        self.image.fill(random.choice([RED, WHITE, GREEN, PURPLE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([LIGHTBLUE, BLUE, DARKBLUE])

all_sprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 40)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 360)
all_sprites.add(sp1)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bouncing Sprite')

bg_color = BLUE
screen.fill(bg_color)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE:
            change_background_color()

    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()