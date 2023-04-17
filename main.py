import pygame 

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw, display_messages, display_settings
from settings import initial_state

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

plugboard, reflector, rotors, rings, key = initial_state()

# Keyboard
KB = Keyboard()

# Plugboard
PB = Plugboard(plugboard.split())

# Enigma machine
ENIGMA = Enigma(eval(reflector), 
                eval(rotors[0]),
                eval(rotors[1]),
                eval(rotors[2]), 
                PB, KB)

# Set the rings on each rotor
ENIGMA.set_rings(rings)

# Set message key
ENIGMA.set_key(key)

# Initialize screen once user settings have been inputted 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

animating = True
while animating:
    # Background 
    SCREEN.fill('#333333')

    # Display input/output text and machine settings
    display_messages(BOLD, INPUT, OUTPUT, WIDTH, MARGINS, SCREEN)
    display_settings(BOLD, SCREEN, WIDTH, HEIGHT, MARGINS, plugboard, rotors, reflector, rings, key)

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
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + ' '
                OUTPUT = OUTPUT + ' '
            else: 
                key_press = event.unicode
                if key_press.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    letter = key_press.upper()
                    INPUT += letter
                    # Encipher input
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT += cipher

# Write machine settings and output to text files
with open('initialization.txt', 'w') as f:
    f.write(plugboard + '\n')
    f.write(' '.join(map(str, rotors)) + '\n')
    f.write(reflector + '\n')
    f.write(' '.join(map(str, rings)) + '\n')
    f.write(' '.join(key))

with open('message.txt', 'w') as f:
    f.write(OUTPUT)

