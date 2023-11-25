
# FUNCTIA property()
# Vom putea accesa atributele private "din afara clasei"
#    de fapt se apeleaza setterul si getterul
class Persoana:
    numar_persoane = 0

    def __init__(self, nume, adresa):
        self.__nume = nume
        self.__adresa = adresa

    # getter function
    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def set_nume(self, val):
        self.__nume = val

    def set_adresa(self, val):
        self.__nume = val
    # deleter function

    def del_nume(self):
        del self.__nume

    def del_adresa(self):
        del self.__adresa

    nume = property(get_nume, set_nume, del_nume)
    adresa = property(get_adresa, set_adresa, del_adresa)


p = Persoana("David", "Suceava")
print(p.nume, p.adresa)
p.nume = "Radu"
p.adresa = "Iasi"
print(p.nume, p.adresa)
# => David Suceava
# => Iasi Suceava

del p.nume
del p.adresa
# print(p.nume, p.adresa) # Eroare
