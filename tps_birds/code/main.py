from settings import *
from background import BG
from player import Player
from obs import Obstacle
from timer import Timer
from support import *
from ui import UI
from button import Button


class Game():
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("TPS Birds")

        self.clock = pygame.time.Clock()
        self.running = True
        self.continue_menu = False
        self.lives = 1
        self.score = 0

        

        ## load assets
        self.load_assets()
        self.ui = UI(self.med_font,self.score,self.clock)

        ## Button
        self.button_surf = pygame.image.load("../graphics/UI/Continue.png").convert_alpha()
        self.button_pos = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


        ## timers
        self.hit_timer = Timer(1500)
        self.spawn_timer = Timer(1000)
        self.score_timer = Timer(1000, autostart=True)

        ## groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        ## sprites

        BG(self.all_sprites)
        self.player = Player(self.all_sprites)

         ## Gameover
        self.gameover_surf = self.med_font.render("Game Over", True, 'red')
        self.gameover_rect = self.gameover_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT*0.3))



    def display_gameover(self):
        self.display_surface.blit(self.gameover_surf, self.gameover_rect)
        self.play_button = Button(self.button_surf, self.button_pos)

    def check_collisions(self):
        for sprite in self.collision_sprites:
            if pygame.sprite.collide_mask(self.player, sprite) and not self.hit_timer.active:
                self.lives -= 1
                self.hit_timer.activate()
                if self.lives <= 0:
                    self.player.kill()
                    self.continue_menu = True

    def reset(self):
        self.player = Player(self.all_sprites)
        self.lives = 1
        self.score = 0
        self.score_timer.activate()

    def spawn_obstacles(self):
        self.spawn_timer.activate()
        direction = choice(["up", "down"]) ## this will randomly choose between up and down
        if direction == 'up':
            pos = (WINDOW_WIDTH + 50, WINDOW_HEIGHT - 100)
        else:
            pos = (WINDOW_WIDTH + 50, 0+100)
        Obstacle((self.all_sprites, self.collision_sprites), pos, direction)

    def load_assets(self):
        self.player_surfs = import_folder(BIRDS['bird1'])
        self.font = pygame.font.Font("../graphics/font/BD_Cartoon_Shout.ttf", 30)
        self.poof_surfs = import_folder(EFFECTS['poof'])
        self.med_font = pygame.font.Font("../graphics/font/BD_Cartoon_Shout.ttf", 60)

    def add_score(self):
        if not self.score_timer.active and self.running and not self.continue_menu:
            self.score += 20
            self.score_timer.activate()

    def display_score(self):
        score_surf = self.font.render('Score: ' + str(self.score), False, 'white')
        score_rect = score_surf.get_frect(topleft = (WINDOW_WIDTH/2, 10))
        self.display_surface.blit(score_surf, score_rect)

    def continue_menu_screen(self):
        ### This is completely unnecessary, but too lazy to change it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()


        self.display_gameover()



    def run(self):
        dt = 0.08
        while self.running:

            self.clock.tick(FRAMERATE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if self.continue_menu and event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.check_click() == True:
                        self.continue_menu = False
                        self.reset()
                        self.play_button.enabled = False


            if not self.spawn_timer.active:
                self.spawn_obstacles()

            if self.continue_menu == True:
                self.continue_menu_screen()
                




            ## draw
            self.display_surface.fill('purple')
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.continue_menu == True:
                self.continue_menu_screen()
                


            ### update
            self.add_score()
            self.hit_timer.update()
            self.spawn_timer.update()
            self.score_timer.update()
            self.all_sprites.update(dt)
            self.check_collisions()
            pygame.display.update()


            self.clock.tick(120)




if __name__ == '__main__':
    game = Game()
    game.ui.main_menu_screen()
    game.run()
