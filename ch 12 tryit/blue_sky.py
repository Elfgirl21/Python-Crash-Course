import sys
import pygame
from setting_B import Settings

class BlueSky:

    def __init__(self):
        pygame.init()
        self.setting_B = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting_B.screen_width, self.setting_B.screen_height))
        pygame.display.set_caption("Blue sky Game")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()

            self.screen.fill(self.setting_B.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    bsg = BlueSky()
    bsg.run_game()