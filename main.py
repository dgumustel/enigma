"""
Reflector: A
Rotors: I-II-III
Plugboard: AR, GK, OX
Message: Hello, World!
"""

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma


I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')
KB = Keyboard()
PB = Plugboard(['AR', 'GK', 'OX'])

ENIGMA = Enigma(A, I, II, III, PB, KB)
print(ENIGMA.encipher(input("Enter a letter: ").upper()))




# I.show()
# I.rotate()
# I.show()