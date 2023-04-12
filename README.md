# Enigma
Can I recreate the enigma machine in Python? The answer is most certainly yes. 

There are a few different steps to this. From what I understand, the design of the World War II enigma machine had several components that worked in combination to scramble messages in any one of nearly 1.59 hundred quintillion ways. 

The transformation steps that happen to encode a message are as follows:

Encryption = PRMLUL<sup>-1</sup>M<sup>-1</sup>R<sup>-1</sup>P<sup>-1</sup>

where P is a plugboard that allowed operators to swap letter signals in pairs; R, M, L are the right, middle, and left rotors (there were 5 to choose from); and U is the reflector (one of three). You might notice that the encryption process is palindromic, allowing operators to type in ciphertext and receive the plaintext message through reverse substitution. 

I don't use much OOP in my work (nor do I know anything about cryptography!) so this object-oriented programming project was good practice. There were a few classes to create here:

- a plugboard class that swaps specified pairs of letters in the alphabet 
- a rotor class with a customizable wiring to scramble a signal; the rotor class also needs to rotate so that incoming signals of the same value are not guaranteed to be encoded as the same letter. The frequency of turnover and rotation position at which this turnover happens should be customizable
- a reflector class with customizable wiring to further scramble a signal 
- a keyboard class for converting letters to signals and back again
- an enigma class to string it all together into one object
- a drawing class responsible for handling the animations

This is off to a good start already. I completed the base design of the machine but would like to add more functionality to make it more interesting and user-friendly. Brainstorming such features below, in no particular order:
- Allow users to upload a text file to be encrypted
- Allow users to save encrypted files 
- Allow users to export enigma settings with encrypted files 
- Give users an interface to enter their settings on initialization 
- Rearrange the GUI so that it more closely resembles the original machine design. It'd be cool to have displays for the keyboard, lampboard, and plugboard, and to be able to see the rotors moving with each keypress. 
- Give users the option to decrypt an encrypted message 

# Resources

I followed a great set of tutorials as a guide and referenced the Wikipedia pages for the enigma machine and the enigma rotor details frequently:

- [Coding an enigma machine](https://www.youtube.com/watch?v=StI2R__7DBA)
- [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine)
- [Enigma rotor details](https://en.wikipedia.org/wiki/Enigma_rotor_details)
