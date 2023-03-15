import pygame

class Plugboard():

    def __init__(self, pairs):
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


        for pair in pairs:
            A, B  = pair
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            # note that Pythin strings don't support item assignment 
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal


    def draw(self, screen, x, y, w, h, font):

        # Rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, 'white', r, width=2, border_radius=15)

        for i in range(26):
            # Left side
            letter = self.left[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center = (x+w/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)

            # Right side
            letter = self.right[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center = (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)