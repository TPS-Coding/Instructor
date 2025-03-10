from settings import *
from button import Button

class UI:
    def __init__(self, font, score, clock):
        self.score = score
        self.font = font
        self.main_menu = True
        self.running = True
        self.clock = clock
        self.display_surface = pygame.display.get_surface()

        ## Button
        self.button_surf = pygame.image.load("../graphics/UI/Continue.png").convert_alpha()
        self.button_pos = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


        ## BG
        self.bg_image = pygame.image.load("../graphics/backgrounds/1.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_rect = self.bg_image.get_rect(topleft = (0,0))

        ## Title
        self.title_surf = self.font.render("TPS Birds", True, 'red')
        self.title_rect = self.title_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT*0.3))

       
    def main_menu_screen(self):
        while self.main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.check_click() == True:
                        self.main_menu = False
                        self.play_button.enabled = False

            ## draw
            self.display_surface.blit(self.bg_image,self.bg_rect)
            self.display_surface.blit(self.title_surf, self.title_rect)
            self.play_button = Button(self.button_surf, self.button_pos)

            ## update

            pygame.display.update()
            self.clock.tick(60)


   