from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

'''Script to encode/decode an input message given an initial state for the enigma machine. 

Input: text file containing message to encode, text file containing initialization settings

Message file will just be plain text, one line.

Settings file will look like this:
QH YV GI OP TD WR MJ CS BN FK 
V III I
A
24 10 16
A W Q
'''

# Historical enigma components 
I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')

with open('message.txt', 'r') as f:
    message = f.read()

with open('initialization.txt', 'r') as f:
    settings = f.read().splitlines()

# Keyboard
KB = Keyboard()

# Plugboard
PB = Plugboard(settings[0].split())

# Enigma components
rotors = settings[1].split()
reflector = settings[2]

# Enigma machine
ENIGMA = Enigma(eval(reflector), 
                eval(rotors[0]),
                eval(rotors[1]),
                eval(rotors[2]), 
                PB, KB)

# Set the rings on each rotor
rings = settings[3].split()
ENIGMA.set_rings(rings)

# Set message key
key = settings[4].split()
ENIGMA.set_key(key)

OUTPUT = ''

# Send message through ENIGMA
for letter in message:
    if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        path, cipher = ENIGMA.encipher(letter)
        OUTPUT += cipher
    elif letter == ' ':
        OUTPUT += letter

# Write OUTPUT to text file
with open('message.txt', 'w') as f:
    f.write(OUTPUT)