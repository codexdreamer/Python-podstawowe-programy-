
#liczbie liczby znaków , lini oraz słów w pliku txt

sciezka_pliku = '/home/sartosz/Pulpit/Tekst.txt'

try:
    with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
        linie = plik.readlines()
    
    liczba_linii = len(linie)  #liczy liczbe lini w pliku
    liczba_znakow = sum(len(linia) for linia in linie)  #liczy liczbe znakow w pliku
    
    liczba_slow = 0
    for linia in linie:   #liczy liczbe slow w pliku
        slowa = linia.split()  
        liczba_slow += len(slowa)

    print(f"Liczba linii: {liczba_linii}")
    print(f"Liczba znaków: {liczba_znakow}")
    print(f"Liczba słów: {liczba_slow}")
    plik.close()

except FileNotFoundError:
    print("Nie ma takiego pliku!")
    


#-------------------------------------------------
#dodawanie tekstu w pliku na końcu

with open(sciezka_pliku,'a',encoding='utf-8') as plik:
    plik.write("Koniec tekstu\n")
    plik.close()

with open(sciezka_pliku,'r',encoding='utf-8') as plik:
    zawartosc = plik.read()
    print(zawartosc)
    plik.close()
    

