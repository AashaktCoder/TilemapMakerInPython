import pygame

pygame.init()

class Button:
    def __init__(self, win, x, y, w, h, color, fcolor, text, border, radius, command):
        self.win = win
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.rect = [self.x, self.y, self.w, self.h]

        self.color = color
        self.fcolor = fcolor

        self.radius = radius
        self.border = border

        self.text = text

        self.command = command

        self.clicked = False

    def Draw(self):
        self.Button = pygame.draw.rect(self.win, self.color, self.rect, self.border, self.radius)
        self.text()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.TakeInput()

    def TakeInput(self):
        self.mouse = pygame.mouse.get_pos()
        if self.Button.collidepoint(self.mouse):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.Button = pygame.draw.rect(self.win, self.fcolor, self.rect, self.border, self.radius)
            self.text()

            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            if not(pygame.mouse.get_pressed()[0]):
                if self.clicked == True: 
                    self.command()
                    self.clicked = False

    def Update(self):
        self.Draw()