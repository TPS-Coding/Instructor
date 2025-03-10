from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.image.load("../graphics/birds/Bird01/Bird01_00.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH*0.2, WINDOW_HEIGHT/2))
        self.velocity = 0
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.gravity = 10

    def apply_gravity(self,dt):
        self.velocity += self.gravity * dt
        self.pos.y += self.velocity * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction = -50


    def update(self,dt):
        self.apply_gravity(dt)
        self.jump()
