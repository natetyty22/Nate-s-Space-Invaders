import pygame

class Menu:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.options = ["Start Game", "High Score", "Exit"]
        self.option_font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 55)

    def draw(self):
        title_text = self.title_font.render('Space Invaders', True, self.color)
        title_rect = title_text.get_rect(center=(400, 100))
        self.screen.blit(title_text, title_rect)
        for i in range (len(self.options)):
            option = self.options[i]
            option_text = self.option_font.render(option, True, self.color)
            option_rect = option_text.get_rect(center=(400, 200 + i * 50))  #????????????????/
            self.screen.blit(option_text, option_rect)
