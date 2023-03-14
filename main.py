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
ENIGMA = Enigma(B, IV, II, I, PB, KB)

# Set the rings on each rotor
ENIGMA.set_rings((1, 1, 1))

# Set message key
ENIGMA.set_key('CAT')
ENIGMA.R.show()

# Encipher message
message = 'TESTINGTESTINGTESTINGTESTING'
cipher_text = ''
for letter in message:
    cipher_text += ENIGMA.encipher(letter)

print(cipher_text)




# I.show()
# I.rotate()
# I.show()