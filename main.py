import pygame 

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# Set up pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Enigma simulator')

# Create fonts
MONO = pygame.font.SysFont('FreeMono', 20)
BOLD = pygame.font.SysFont('FreeMono', 20, bold=True)

# Global vars
WIDTH = 1200
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {'top':100, 'bottom':100, 'left':100, 'right':100}
GAP = 50

INPUT = ''
OUTPUT = ''
PATH = []

# Historical enigma components 
I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')

# Keyboard and plugboard
KB = Keyboard()
PB = Plugboard(['AB', 'CD', 'EF'])

# Enigma machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# Set the rings on each rotor
ENIGMA.set_rings((1, 1, 1))

# Set message key
ENIGMA.set_key('CAT')
# ENIGMA.R.show()

# Encipher message
# message = 'TESTINGTESTINGTESTINGTESTING'
# cipher_text = ''
# for letter in message:
#     cipher_text += ENIGMA.encipher(letter)

# print(cipher_text)


animating = True
while animating:
    # Background 
    SCREEN.fill('#333333')

    # Display INPUT 
    text = BOLD.render(INPUT, True, 'white')
    text_box = text.get_rect(center = (WIDTH/2, MARGINS['top']/2))
    SCREEN.blit(text, text_box)

    # Display OUTPUT
    text = BOLD.render(OUTPUT, True, 'grey')
    text_box = text.get_rect(center = (WIDTH/2, 20+MARGINS['top']/2))
    SCREEN.blit(text, text_box)

    # Draw enigma machine
    draw(ENIGMA, PATH,  SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # Update screen
    pygame.display.flip()

    # Track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                I.rotate()
            else: 
                key = event.unicode
                if key.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    letter = key.upper()
                    INPUT += letter
                    # Encipher input
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT += cipher
                    print(INPUT)
                    print(OUTPUT)
                    print(PATH)

