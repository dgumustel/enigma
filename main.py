import pygame 

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw
from random import sample
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
component_options = {'I':I, 'II':II, 'III':III, 'IV':IV, 'V':V, 'A':A, 'B':B, 'C':C}

plugboard, reflector, rotors, rings, key = initial_state()
print(key)
print(' '.join(key))

# Keyboard
KB = Keyboard()

# Plugboard
PB = Plugboard(plugboard.split())

# Enigma machine
ENIGMA = Enigma(component_options[reflector], 
                component_options[rotors[0]],
                component_options[rotors[1]],
                component_options[rotors[2]], 
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

    # Display INPUT 
    text = BOLD.render(INPUT, True, 'white')
    text_box = text.get_rect(center = (WIDTH/2, MARGINS['top']/3))
    SCREEN.blit(text, text_box)

    # Display OUTPUT
    text = BOLD.render(OUTPUT, True, 'grey')
    text_box = text.get_rect(center = (WIDTH/2, 20+MARGINS['top']/3))
    SCREEN.blit(text, text_box)

    # Display initialization settings
    img = BOLD.render('Plugboard settings: ' + plugboard, True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .9))

    img = BOLD.render('Rotor selection: ' + ' '.join(map(str, rotors)), True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .6))

    img = BOLD.render('Reflector selection: ' + reflector, True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .3))

    img = BOLD.render('Rotor ring settings: ' + ' '.join(map(str, rings)), True, 'grey')
    SCREEN.blit(img, (WIDTH*.65, HEIGHT - MARGINS['bottom'] * .9))
    
    img = BOLD.render('Rotor key setting:   ' + ' '.join(key), True, 'grey')
    SCREEN.blit(img, (WIDTH*.65, HEIGHT - MARGINS['bottom'] * .6))

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

with open('initialization.txt', 'w') as f:
    f.write('Enigma initialization: \n')
    f.write('Plugboard settings: ' + plugboard + '\n')
    f.write('Rotor selection: ' + ' '.join(map(str, rotors)) + '\n')
    f.write('Reflector selection: ' + reflector + '\n')
    f.write('Rotor ring settings: ' + ' '.join(map(str, rings)) + '\n')
    f.write('Rotor key setting: ' + ' '.join(key))

with open('message.txt', 'w') as f:
    f.write(OUTPUT)

