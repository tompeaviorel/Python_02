# Functia  __str__
class Persoana:
    def __init__(self, nume, varsta):
        self.__nume = nume
        self.__varsta = varsta

    def __str__(self):
        return "Numele tau este {} si ai  {} ani".format(self.__nume, self.__varsta)
        # return f"{self.__nume}{self.__varsta}"


p1 = Persoana("Sorin", 36)
print(p1)

# => Numele tau este Sorin si ai  36 ani
