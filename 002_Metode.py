# Ex 02.  metode simple
class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def salut(self):
        print("Salut  " + self.nume + "!")
        print("Ai " + str(self.varsta) + " ani.")


p1 = Persoana("Sorin", 36)
p1.salut()
# => Salut  Sorin!
# => Ai 36 ani.

p2 = Persoana("Gabriel", 32)
p2.salut()
# => Salut  Gabriel!
# => Ai 32 ani.