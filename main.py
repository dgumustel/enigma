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
plugboard_settings = input('Please input your plugboard settings: ')
PB = Plugboard(plugboard_settings.split())

# Enigma machine
'''
To save the initial state of the machine so that users can decrypt their own messages later, we need to track the following:
- reflector
- rotors L, M, R
- ring settings of each rotor
- initial key
- plugboard settings

These should all also be customizable so users can enter these settings upon initialization of the program.
TODO: implementation in progress, may consider creating a settings.py script responsible for handling user input
'''
rotor_selection = input('Please input your rotor selection. Choose from I, II, III, IV, V: ')
rotor_selection = rotor_selection.split()
reflector_selection = input('Please input your reflector selection. Choose from A, B, C: ')
component_options = {'I':I, 'II':II, 'III':III, 'IV':IV, 'V':V, 'A':A, 'B':B, 'C':C}

ENIGMA = Enigma(component_options[reflector_selection], 
                component_options[rotor_selection[0]],
                component_options[rotor_selection[1]],
                component_options[rotor_selection[2]], 
                PB, KB)

# Set the rings on each rotor
ring_settings = input('Please input your ring settings: ')
ring_settings = [int(i) for i in ring_settings]
ENIGMA.set_rings(ring_settings)

# Set message key
key_setting = input('Please input your key setting: ')
ENIGMA.set_key(key_setting)

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
    img = BOLD.render('Plugboard settings: ' + plugboard_settings, True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .9))

    img = BOLD.render('Rotor selection: ' + ' '.join(map(str, rotor_selection)), True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .6))

    img = BOLD.render('Reflector selection: ' + reflector_selection, True, 'grey')
    SCREEN.blit(img, (MARGINS['left'], HEIGHT - MARGINS['bottom'] * .3))

    img = BOLD.render('Rotor ring settings: ' + ' '.join(map(str, ring_settings)), True, 'grey')
    SCREEN.blit(img, (WIDTH*.65, HEIGHT - MARGINS['bottom'] * .9))
    
    img = BOLD.render('Rotor key setting: ' + key_setting, True, 'grey')
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
                key = event.unicode
                if key.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    letter = key.upper()
                    INPUT += letter
                    # Encipher input
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT += cipher
                    # print(INPUT)
                    # print(OUTPUT)
                    # print(PATH)

with open('message.txt', 'w') as f:
    f.write(OUTPUT)

