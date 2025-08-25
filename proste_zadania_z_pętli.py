

#zad.1 program tabliczka mnożenia od 1 do 10 wszystkie przypadki

#for liczba in range(1,11):
 #   for liczba2 in range(1,11):
  #      print(liczba,"*",liczba2,"=",liczba*liczba2)

#------------------------------------------------------------
#zad 2

#program zgaduje liczbe od 1 do 100

#import random

#print("Podaj liczbe od 1 do 100")
#liczba = int(input())

#while True:
 #   liczba_wylosowana = random.randint(0,100)
  #  if liczba_wylosowana == liczba:
   #     print("Twoja liczba to: ",liczba)
    #    break
    #else:
     #   continue

#-----------------------------------------------
#zad 3
# Użytkownik podaje liczbę > 0.
#  Program odlicza w dół do zera
import time

print("Podaj liczbe całkowitą wieksza od zera")
liczba = int(input())
print("Rozpoczynamy odliczanie!")
while True:
    if liczba > 0:
        print(liczba)
        liczba -= 1
        time.sleep(0.5)
    break

print("0\nKoniec!")











