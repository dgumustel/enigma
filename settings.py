from string import ascii_uppercase
from random import sample, randint

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

def initial_state(manual_entry = input('Would you like to input settings? If not, settings will be randomized (y/n): ')):
    
    if manual_entry == 'n':
        letters = sample(ascii_uppercase, 20)
        plugboard_settings = ''
        for i in range(0, 20, 2):
            plugboard_settings += letters[i] + letters[i+1] + ' '
        rotor_selection = sample(['I', 'II', 'III', 'IV', 'V'], 3)
        reflector_selection = sample(['A', 'B', 'C'], 1)[0]
        ring_settings = [randint(1, 26) for i in range(3)]
        key_setting = [sample(ascii_uppercase, 1)[0] for i in range(3)]
    elif manual_entry == 'y':
        plugboard_settings = input('Please input your plugboard settings: ')

        # TODO: alter input so that each rotor can only be chosen 1 time
        rotor_selection = input('Please input your rotor selection. Choose from I, II, III, IV, V: ')
        rotor_selection = rotor_selection.split()

        reflector_selection = input('Please input your reflector selection. Choose from A, B, C: ')
        
        ring_settings = input('Please input your ring settings: ')
        ring_settings = ring_settings.split()

        key_setting = input('Please input your key setting: ')
        key_setting = key_setting.split()
        
    return plugboard_settings, reflector_selection, rotor_selection, ring_settings, key_setting


