
import time

spis_kontaktow = {}


def menu():
    print("===== KSIĄŻKA KONTAKTÓW =====")
    print("1. Wyświetl kontakty")
    print("2. Usuń kontakt")
    print("3. Edytuj kontakt")
    print("4. Dodaj kontakt")
    print("5. Zobacz zawartość kontaktów")
    print("6. Wyjście z programu")
    print("=============================")
    time.sleep(1)
    print("Wybierz rodzaj operacji(1-5):")
    wybor = input()
    if wybor == '1':
        return wyswietl_slownik()
    elif wybor == '2':
        return usun_kontakt()
    elif wybor =='3':
        return edytuj_kontakt()
    elif wybor == '4':
        return dodaj_kontakt()
    elif wybor =='6':
        return zakoncz_program()
    elif wybor == '5':
        return zawartosc_kontaktow()
    else:
        print("Błędny wybór operacji!")
        print("Spróbuj jeszcze raz!")
        time.sleep(1)
        return menu()


def wyswietl_slownik():
    if spis_kontaktow == spis_kontaktow == {}:
        print("W spisie znajduje się 0 kontaktów!")
        time.sleep(2)
    else:
        for key in spis_kontaktow:
            print(key)
        time.sleep(1)
    print("Podaj dowolny znak by kontynuować!")
    znak=input()
    time.sleep(1)
    return menu()   

def usun_kontakt():
    if spis_kontaktow == spis_kontaktow == {}:
        print("W spisie znajduje się 0 kontaktów!")
        time.sleep(2)
        return menu()
    else:
        for key in spis_kontaktow:
            print(key)
        while True:
            time.sleep(1)
            print("Podaj który kontakt chcesz usunąć:")
            wybor_kon = input()
            if wybor_kon in spis_kontaktow:
                del spis_kontaktow[wybor_kon]
                print("Kontakt został usunięty!")
                time.sleep(1)
                return menu()
            else:
                print("Nie ma takiego kontaktu!")
                print("Spróbuj jeszcze raz!")
                continue


      
                     
         
def edytuj_kontakt():
    if not spis_kontaktow:
        print("W spisie znajduje się 0 kontaktów!")
        print("Za chwilę nastąpi powrót do menu!")
        time.sleep(2)
        return menu()
    else:
        print("Wybierz kontakt do edycji:")
        for key in spis_kontaktow:
            print(f"- {key}")
        klucz = input()
        if klucz in spis_kontaktow:
            kontakt = spis_kontaktow[klucz]
            print("Dane kontaktu:")
            for pole, wartosc in kontakt.items():
                print(f"{pole}: {wartosc}")
            print("Podaj nazwę pola do zmiany (Wiek, Adres, Stanowisko pracy, Numer tel):")
            wybor_do_zmiany = input()
            if wybor_do_zmiany in kontakt:
                print(f"Podaj nową wartość dla pola '{wybor_do_zmiany}':")
                nowa_wartosc = input()
                kontakt[wybor_do_zmiany] = nowa_wartosc
                print("Dane zostały zaktualizowane.")
            else:
                print("Nie ma takiego pola w kontakcie.")
        else: 
            print("Nie ma takiej osoby")
            print("Spróbuj jeszcze raz!")
            time.sleep(1)
            return edytuj_kontakt()
    time.sleep(2)
    return menu()


def zawartosc_kontaktow():
    if spis_kontaktow == spis_kontaktow == {}:
        print("Brak zawartości")
        time.sleep(2)
        return menu()
    else:
        for klucz,wartosc in spis_kontaktow.items():
            print(f"{klucz}: {wartosc}")
        print("Żeby wrócić do menu podaj dowolny znak!")
        znak = input()
        time.sleep(1)
        return menu()
    



def dodaj_kontakt():
    print("Podaj imie i nazwisko")
    imie_nazwisko = input()
    print("Podaj wiek")
    wiek=input()
    print("Podaj adres")
    adres=input()
    
    print("Podaj stanowisko pracy")
    praca=input()
    print("Podaj numer telefonu")
    numer_tel = input()

    spis_kontaktow[imie_nazwisko] = {
    'Wiek': wiek,
    'Adres': adres,
    'Stanowisko pracy': praca,
    'Numer tel': numer_tel 
    }

    print("Kontakt został zapisany!")
    time.sleep(2)
    return menu()

def zakoncz_program():
    print("Program za chwilę zostanie zamknięty!")
    time.sleep(2)
    exit()




menu()