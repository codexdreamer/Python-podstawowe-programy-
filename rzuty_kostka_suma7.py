


# Program symuluje 1000 rzutów dwiema kośćmi sześciennymi
# i zlicza, ile razy suma wyrzuconych oczek wyniosła dokładnie 7.

import random

ilosc_rzutow = 0

ilosc_sumy_7 = 0

while ilosc_rzutow <1000:
    pierwsza_kosc = random.randint(1,6)
    druga_kosc = random.randint(1,6)

    if pierwsza_kosc + druga_kosc == 7:
        ilosc_sumy_7 += 1

    ilosc_rzutow += 1



print("Suma kości 1 i 2 wynosząca 7 wydarzyła się",ilosc_sumy_7,"razy.")
    