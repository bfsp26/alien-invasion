import sys
import pygame
from settings import Settings


class AlienInvasion:
    """"Overall class to manage game assets and behavior."""

    def __init__(self):
        """"Initialize the game, and create game resources."""
        # The pygame.init() function initializes the background settings that Pygame needs to work properly.
        pygame.init()
        # Create an instance of Settings
        self.settings = Settings()

        # We call pygame.display.set_mode() to create a display window, on which we’ll draw all the game’s graphical
        # elements.
        self.screen = pygame.display.set_mode((self.settings.screen_with, self.settings.screen_with))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
