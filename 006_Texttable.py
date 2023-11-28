"""
    Trebuie instalat pachetul textable:
    1. Click Butonul Main Menu (stanga sus)
    2. Settings
    3. Project ( a 6 - a optiune din Settings)
    4.     Python Interpreter
    5.        Butonul +
    6.        cauta  / scrie texttable
    7.        Install

    /// Pentru alt proiect trebuie intalat din nou
"""

from texttable import Texttable


def start():
    my_table = Texttable()      # my_table = obiect de tip Texttable

    row_1 = [1, 2, 3]
    my_table.add_row(row_1)     # apelez functia add_rou pentru  my_table

    row_2 = [6, 7, 8]
    my_table.add_row(row_2)

    print(my_table.draw())      # apelez functia draw pentru my_table aceasta functie probabil returneaza un __str__


if __name__ == '__main__':
    start()
