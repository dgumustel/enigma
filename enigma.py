class Enigma:

    def __init__(self, U, L, M, R, P, KB):
        self.U = U
        self.L = L
        self.M = M
        self.R = R
        self.P = P
        self.KB = KB

    def encipher(self, letter):
        signal = self.KB.forward(letter)
        signal = self.P.forward(signal)
        signal = self.R.forward(signal)
        signal = self.M.forward(signal)
        signal = self.L.forward(signal)
        signal = self.U.reflect(signal)
        signal = self.L.backward(signal)
        signal = self.M.backward(signal)
        signal = self.R.backward(signal)
        signal = self.P.backward(signal)
        letter = self.KB.backward(signal)
        print('Your cyphertext is:', letter)