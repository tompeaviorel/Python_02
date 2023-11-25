# Ex 03. public / private / protected
class Punct:
    def __init__(self):
        self.__x = 0                # Privat  => NU poate fi accesat  obiect.__x
        self.__y = 0                # Privat
        self._culoare = "incolor"   # Protected => poate fi accesat din afara clasei dar NU ar trebui !

    def set_punct(self, x, y):
        self.__x = x
        self.__y = y

    def get_punct(self):
        p = [self.__x, self.__y, self._culoare]
        return p


def start():
    print("Start: ")

    p1 = Punct()
    p1._culoare = "verde"
    p1.set_punct(2, 3)
    print("Obiect p1:", p1.get_punct())
    # print(p1.__x) # Eroare  p1 nu poate accesa __x (pentru ca e privat)

    p2 = Punct()
    p2._culoare = "rosu"
    p2.__x = 8      # nu va modifica atributul __x, va crea altul
    print("p2.__x: ", p2.__x)   # Merge pentru ca se creeaza p2.__x in linia precedenta (doar pentru p2)
    print("Obiect p2:", p2.get_punct())

# => Obiect p1: [2, 3, 'verde']
# => p2.__x:  8
# => Obiect p2: [0, 0, 'rosu']


if __name__ == '__main__':
    start()
