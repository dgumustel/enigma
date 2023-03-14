class Plugboard():

    def __init__(self, pairs):
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


        for pair in pairs:
            A, B  = pair
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            # note that Pythin strings don't support item assignment 
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal