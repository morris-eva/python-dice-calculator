
# Online Python - IDE, Editor, Compiler, Interpreter

# bond represents the number of best friends or partners of the character
# that are in the party.
bond = 0

# dice are represented with a dictionary where the keys are the value of the face
# and the values are the number of faces with that value

class Die:
    def __init__(self, faces):
        self.faces=faces
    
    def display(self):
        print(self.faces)
    
    def add_to(self, die):
        result = {}
        for value_a, n_a in self.faces.items():
            for value_b, n_b in die.faces.items():
                result[value_a+value_b] = 0
      
        for value_a, n_a in self.faces.items():
            for value_b, n_b in die.faces.items():
                result[value_a+value_b] = result[value_a+value_b] + n_a*n_b
        return Die(result)
    
    def roll(self, n):
        result = Die({0:1})
        for i in range(n):
            result = result.add_to(self)
        return result

die_reduced = Die({1: 1, 0:5})
die_standard = Die({2+bond: 1, 1: 1, 0: 4})
die_skilled = Die({2+bond: 1, 1: 2, 0: 3})

die_standard.roll(3).display()
