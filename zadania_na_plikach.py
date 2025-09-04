#ZADANIA NA PLIKACH PYTHON


#zad.1
# -Stwórz strukturę katalogów a/b/c/d (os.makedirs)
#- Przejdź do katalogu d (os.chdir), wyświetl bieżący katalog
#- Wróć do folderu startowego i usuń strukturę (os.removedirs)

import os #import modułu os

start = os.getcwd() #zapisuje aktualny katalog roboczy pod zmienną : start
folder = 'a/b/c/d' #sciezka zagniezdzenia folderu
nowy_katalog = os.makedirs(folder) #tworzy strukture katalogu
os.chdir("a/b/c/d") #zmienia jego strukture na podana czyli a/b/c/d
print(os.getcwd()) #pokazuje w jakim miejscu sie znajdujemy
os.chdir(start) #wraca do katalogu roboczego
os.removedirs(folder) #usuwa ten folder

#zad2
#Wypisz os.name, platform.system(),
#platform.machine() — pokaż, co zwracają

import platform

print(os.name)  #typ systemu np. posix
print(platform.system()) # nazwa systemu np. Linux
print(platform.machine()) #architektura procesora np. AMD64




