# Enigma
Can I recreate the enigma machine in Python? The answer is most certainly yes. 

There are a few different steps to this. From what I understand, the design of the World War II enigma machine had several components that worked in combination to scramble messages in any one of nearly 1.59 hundred quintillion ways. 

The transformation steps that happen to encode a message are as follows:

Encryption = PRMLUL<sup>-1</sup>M<sup>-1</sup>R<sup>-1</sup>P<sup>-1</sup>

where P is a plugboard that allowed operators to swap letter signals in pairs; R, M, L are the right, middle, and left rotors (there were 5 to choose from); and U is the reflector (one of three). You might notice that the encryption process is symmetric, allowing the same key to be used for the encryption and decryption of a message.

I don't use much OOP in my work (nor do I know anything about cryptography!) so this object-oriented programming project was good practice. There were a few classes to create here:

- a plugboard class that swaps specified pairs of letters in the alphabet 
- a rotor class with a customizable wiring to scramble a signal; the rotor class also needs to rotate so that incoming signals of the same value are not guaranteed to be encoded as the same letter. The frequency of turnover and rotation position at which this turnover happens should be customizable
- a reflector class with customizable wiring to further scramble a signal 
- a keyboard class for converting letters to signals and back again
- an enigma class to string it all together into one object
- a drawing script responsible for handling the animations

I also added a settings script for handling user input of the initial state of the machine on launch; if a user declines manually setting this, an initial state is randomly generated. An additional script for handling the encryption/decryption of text files may also be added. 

More improvements to the display and functionality of this program are being tracked under the "Improvements" issue. 

# Resources

I followed a great set of tutorials as a guide and referenced the Wikipedia pages for the enigma machine and the enigma rotor details frequently:

- [Coding an enigma machine](https://www.youtube.com/watch?v=StI2R__7DBA)
- [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine)
- [Enigma rotor details](https://en.wikipedia.org/wiki/Enigma_rotor_details)
