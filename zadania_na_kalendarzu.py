
import datetime

#zad 1
#Wypisz obecną datę i czas (datetime.now() i strftime) 
# w formacie: 2020‑04‑21 10:30:00

data = datetime.datetime.now()  #sprawdza date aktualna i przypisuje ją do zmiennej data
print(data) #wyswietla ją

formatowana_data = data.strftime("%Y-%m-%d %H:%M:%S")  #formatuje date w odpowiedni sposób

print(formatowana_data) #i ją wyświetla

#zad 2

#Podaj datę startową i liczbę dni n,
#  zwróć datę po n dniach (timedelta)

data_teraz = data = datetime.datetime.now() #pobiera czas aktualny

n = 5 #przypisuje 5 do n

przyszly_czas =data_teraz + datetime.timedelta(days = n) #dodaje aktualny czas + 5 dni

sformatowana_data = przyszly_czas.strftime("%Y-%m-%d %H:%M:%S") #fromatuje 

print(sformatowana_data) #wyświetla

#zad 3

import calendar

#- Dla zadanego roku i miesiąca wypisz kalendarz 
# (calendar.month())
#- Sprawdź, ile piątków 13‑tego jest w danym roku 
# (iterator z itermonthdays2())

rok = 2025
miesiac = 9

print(calendar.month(rok, miesiac))

ilosc_piatkow_13 = 0

for miesiac in range(1, 13):
    
    for dzien, dzien_tyg in calendar.Calendar().itermonthdays2(rok, miesiac):
        if dzien == 13 and dzien_tyg == 4:  
            ilosc_piatkow_13 += 1
            print(f"Piątek 13-go w {rok}-{miesiac:02d}")

print("Liczba piątków 13-tego w roku", rok, ":", ilosc_piatkow_13)


