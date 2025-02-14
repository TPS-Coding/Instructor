from settings import *


class Game():
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("TPS Birds")
        
        self.clock = pygame.time.Clock()
        self.running = True
        

    def run(self):
        dt = 0.08
        while self.running:

            self.clock.tick(FRAMERATE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()


            ## draw
            self.display_surface.fill('purple')


            ### update
            pygame.display.update()




if __name__ == '__main__':
    game = Game()
    game.run()
