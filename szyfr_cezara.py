
import time

przesuniecie = 3

def menu():
    print("=== MENU SZYFRU CEZARA ===")
    print("1. Szyfruj tekst")
    print("2. Deszyfruj tekst")
    print("3. Zakończ program")
    print("==========================")
    print("")
    print("Podaj numer operacji do wykonania(1-3:)")
    operacja = input()
    if operacja == '1':
        return szyfruj_tekst()
    elif operacja == '2':
        return rozszyfruj_tekst()
    elif operacja == '3':
        return zakoncz_program()
    else:
        print("Operacja nie została wykryta!\nSpróbuj ponownie:")
        return menu()


def szyfruj_tekst():
    nowy_wyraz = []
    print("Podaj tekst do zaszyfrowania:")
    tekst=input()
    for litera in tekst:
        if litera.isalpha():
            nowa_litera = chr((ord(litera) - ord('a') + przesuniecie) % 26 + ord('a'))
            nowy_wyraz.append(nowa_litera)
        else:
            nowy_wyraz.append(litera)
    print("Twój zaszyfrowany wyraz to:",''.join(nowy_wyraz))
    print("")
    print("Wybierz dowolny znak by kontynuować!")
    znak = input()
    return menu()

def rozszyfruj_tekst():
    nowy_wyraz=[]
    print("Podaj zaszyfrowany tekst:")
    tekst=input()
    for litera in tekst:
        if litera.isalpha():
            nowa_litera = chr((ord(litera) - ord('a') - przesuniecie) % 26 + ord('a'))
            nowy_wyraz.append(nowa_litera)
        else:
            nowy_wyraz.append(litera)
    
    print("Twoja rozszyfrowa wiadomość to:",''.join(nowy_wyraz))
    print("")
    print("Wybierz dowolny znak by kontynuować!")
    znak = input()
    return menu()


def zakoncz_program():
    print("Program za chwile zostanie wyłączony!")
    time.sleep(2)
    exit()




menu()



