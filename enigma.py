class Enigma:

    def __init__(self, U, L, M, R, P, KB):
        self.U = U
        self.L = L
        self.M = M
        self.R = R
        self.P = P
        self.KB = KB

    def set_rings(self, rings):
        self.L.set_ring(rings[0])
        self.M.set_ring(rings[1])
        self.R.set_ring(rings[2])

    # Set code key
    def set_key(self, key):
        self.L.rotate_to_letter(key[0].upper())
        self.M.rotate_to_letter(key[1].upper())
        self.R.rotate_to_letter(key[2].upper())

    def encipher(self, letter):
        # Rotate rotors when key is pressed
        # TODO: check that rotations with notches here work as desired
        if self.M.left[0] == self.M.notch and self.R.left[0] == self.R.notch:
            self.L.rotate()
            self.M.rotate()
            self.R.rotate()
        # Double stepping below looks wrong to me 
        elif self.M.left[0] == self.M.notch:
            self.L.rotate()
            self.M.rotate()
            self.R.rotate() 
        elif self.R.left[0] == self.R.notch:
            self.M.rotate()
            self.R.rotate()
        else:
            self.R.rotate()

        # Pass signal through the machine
        signal = self.KB.forward(letter)
        path = [signal, signal]

        for component in [self.P, self.R, self.M, self.L]:
            signal = component.forward(signal)
            path.extend([signal, signal])

        signal = self.U.reflect(signal)
        path.extend([signal, signal, signal])

        for component in [self.L, self.M, self.R, self.P]:
            signal = component.backward(signal)
            path.extend([signal, signal])

        letter = self.KB.backward(signal)
        # print('Your cyphertext is:', letter)
        return path, letter