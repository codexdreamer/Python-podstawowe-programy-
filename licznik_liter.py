
#program bierze pod uwage tylko litery z alfabetu
#spacja,znaki specjalne, cyfry itp zostaną pominięte

print("Podaj zbiór liter")
zbior = input()
lista=[]
slownik={}

for e in zbior:
    lista.append(e)


while True:
    for litera in lista:
        if litera.isalpha():
            if litera in slownik:
                slownik[litera] +=1
            else:
                slownik[litera] = 1

            
        else:
            continue
    break



print("Twój ciąg liter ,,",zbior,"'' ma:")
for klucz,wartosc in slownik.items():
    print(klucz,":",wartosc)

      


