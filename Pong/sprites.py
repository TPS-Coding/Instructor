from settings import *
from random import choice, uniform


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        ## image
        self.image = pygame.Surface(SIZE['paddle'])
        self.image.fill(COLORS['paddle'])


        ## rect and movement
        self.direction = 0 
        self.rect = self.image.get_frect(center=POS['player'])


    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def update(self, dt):
        self.get_direction()
        self.move(dt)


class Player(Paddle):
    def __init__(self,groups):
        super().__init__(groups)


        self.speed = SPEED['player']

    
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])




class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)

        self.paddle_sprites = paddle_sprites
        self.speed = SPEED['ball']

        ##image
        self.image = pygame.Surface(SIZE["ball"], pygame.SRCALPHA)
        #self.image.fill(COLORS["ball"])
        pygame.draw.circle(self.image,COLORS["ball"], (SIZE['ball'][0]/2,
                                                     SIZE['ball'][1]/2),
                                                     SIZE['ball'][0]/2)


        ## rect 
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.Vector2(choice([1,-1]), uniform(0.7, 0.8)*choice([-1,1]))
        

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

        self.collision("horizontal")


    def wall_collision(self):
        ## y direction
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

       

    
    def collision(self, direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    self.speed += 20
                    if self.rect.right >= sprite.rect.left and self.direction.x == 1:
                        self.rect.right = sprite.rect.left
            
                    if self.rect.left <= sprite.rect.right and self.direction.x == -1:
                        self.rect.left = sprite.rect.right
                        
                    self.direction.x *= -1

 
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.wall_collision()


class Opponent(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)

        self.speed = SPEED['opponent']
        self.rect = self.image.get_frect(center = POS['opponent'])
        self.ball = ball

    def get_direction(self):
        self.direction = 1 if self.ball.rect.centery > self.rect.centery else -1


class Player2(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)

        self.speed = SPEED['opponent']
        self.rect = self.image.get_frect(center = POS['opponent'])
        self.ball = ball

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])


class Obstacle(Paddle):
    def __init__(self, groups, pos):
        super().__init__(groups)

        self.image = pygame.Surface(SIZE['obstacle'])
        self.image.fill(COLORS['paddle'])

        self.rect = self.image.get_frect(center = pos)

        self.speed = 0

    def get_direction(self):
        self.direction = 0