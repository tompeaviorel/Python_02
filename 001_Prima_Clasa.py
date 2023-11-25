class Persoana:
    oras = "Suceava"                                # Atribut de clasa (este partajat de toate obiectele)

    def __init__(self, nume="NoName", varsta=-1):   # Constructor
        self.nume = nume                            # Atribut de instanta (este specific fiecarui obiect)
        self.varsta = varsta


P1 = Persoana()
print(P1.oras, P1.nume, P1.varsta)
# => Suceava xyz -1

P2 = Persoana("Pop", 35)
print(P2.oras, P2.nume, P2.varsta)
# => Suceava Pop 35

P1.oras = "Iasi"
print(P1.oras, P2.oras)
# => Iasi Suceava

Persoana.oras = "Botosani"
print(P1.oras, P2.oras)
# => Iasi Botosani
