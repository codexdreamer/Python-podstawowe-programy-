import time  #importuje moduł ,,time" w celu zamrażania programu komendą : time.sleep(ilosc sekund)



lista_zakupow = []  #lista zakupów

def wywolanie_listy(): #funcja wypisuje wszystkie elementy z listy 
    if lista_zakupow ==[]:
        print("Twoja lista jest PUSTA!") 
        time.sleep(2)
        return menu_programu()  

    else:
        print("Twoja lista zakupów:")
        time.sleep(1)
        for e in lista_zakupow:  #dla kazdego elemnetu w liście wyswietl element 
            print(e)
            time.sleep(1)  #usypia program na sekunde

        print("Wybierz dowolny znak by wrócić do MENU!")
        wybor_znaku_897987 = input()
        
        return menu_programu()


def del_element():  #funckja usuwa element z listy zakupow
   
    print("Podaj element do usunięcia:")
    element = input()   #pytamy uzytkownika o produkt do usuniecia i go pobieramy jako element
    
    if element in lista_zakupow: #jesli pobrany element jest w liscie zakupow
        lista_zakupow.remove(element) #element zostanie z niej usuniety
        print("Element:",element,"został usunięty z listy!") #uzytkownik zostanie o tym poinformowany
        time.sleep(1)  #usypia program na sekunde
        return menu_programu()  #  uzytkownik powraca do menu glownego
        

    else:    # jeśli taki element nie znajduje sie na liście zakupow pytamy użytkownika czy chce wybrac jeszcze raz element czy powrócic do menu
        print("W liście zakupów nie znajduje się podany element!")
        time.sleep(1)
        print("Chcesz spróbować jeszcze raz? Czy powrócić do menu programu?")
        time.sleep(1)
        print("jeszcze raz = j\nmenu = dowolny klawisz np. m + enter")
        wybor = input()   #pobieramy wybor uzytkownika
        if wybor == 'j':  # jesli rowna sie j czyli uzytkownik chce jeszcze raz funcja rozpocznie sie od nowa (del_element)
            time.sleep(1)
            return del_element()
        else:
            time.sleep(1)
            return menu_programu()  # jesli nie to powroci do menu

    


def add_element():  #funckja dodaje element do listy
    
    print("Podaj produkt jaki chcesz dodać do listy:")
    element=input()  # pyta i pobiera element od uzytkownika
    if element in lista_zakupow:  # jesli element jest w liscie pyta sie uzytkownika czy chce go dodac jeszcze raz
        print("Produkt znajduje sie w liście!\nCzy chcesz go dodać jeszcze raz?")
        print("t - tak \n dowolny klawisz - nie")
        wybor=input()  #pobiera wybor tak lub nie
        if wybor == 't' or wybor =='T':
            lista_zakupow.append(element)    #jesli tak doda ten element 
            return menu_programu()    # i powroci do menu glownego
        else:
            print("Chcesz powrócić do menu głównego czy spróbować dodać inny produkt? ") #jesli wybierze ,,nie" to wtedy pyta sie czy uzytkownik chce powrocic do menu czy sprobowac jeszcze raz
            print("p - powrót \n dowolny klawisz - inny produkt")
            wybor_2=input()     
            if wybor_2 == 'p':  #jesli wybierze powrot 
                return menu_programu()  #to wraca do menu glownego 
            else:
                return add_element() #w innym wypadku rozpoczyna funckje od nowa add_element i prosi uzytkownika o ponowne podanie elementu do dodania
    else: #jesli elementu nie ma w liscie to dodaje ten element do listy
        lista_zakupow.append(element)    
        return menu_programu()  # i wraca do menu programu
        



def clear_lista_zakupów(): #funckja czysci liste do zera
    print("Napewno chcesz usunąć listę?\nt-tak ,dowolny klawisz - nie") # na poczatku pyta sie o potwierdzenie tej decyzji
    wybor= input()
    if wybor == 't' or wybor=='T': #jesli tak to usunie kazdy element z listy 
        lista_zakupow.clear() #czysci liste do zera #lista zakupow = []
        print("Lista została wyczyszczona!")
        return menu_programu()  #informuje o udanym wyczyszczeniu i powraca do menu glownego
    else :
        print("Operacja nie została zatwierdzona!") # w przypadku  odmowy przez uzytkownika
        return menu_programu() #wraca do menu glownego

    
def zakonczenie_programu():  # funkcja kończąca program
    print("Czy na pewno chcesz wyjść z programu?")
    print("t = tak , dowolny inny znak = nie")
    wybor = input("Twój wybór: ")

    if wybor.lower() == 't':  #jeśli tak (małe lub duże T)
        print("Program za chwilę zostanie zamknięty!")
        time.sleep(2)
        exit()  #kończy definitywnie działanie programu
    else:  # jeśli nie  to wraca do menu głównego
        print("Powrót do Menu programu...")
        time.sleep(1.5)
        return menu_programu()


def menu_programu():    #funckja wyswietla menu główne programu 
    print("+-------------------------+")
    print("|     LISTA ZAKUPÓW      |")
    print("+-------------------------+")
    print("| 1. Dodaj element        |")
    print("| 2. Usuń element         |")
    print("| 3. Pokaż listę          |")
    print("| 4. Wyczyść listę        |")
    print("| 5. Zakończ              |")
    print("+-------------------------+")   # tutaj mamy wizualizacje tego menu 
    print("")
    print("Podaj operację jaką chcesz wykonać(1-5):") #wybor operacji
    wybor_operacji = input() #pobranie wyboru uzytkownika
    if wybor_operacji == '1':  #jesli 1 wywoluje funckcje ponizej
        return add_element()
    elif wybor_operacji =='2': #jesli 2 wywoluje funckcje ponizej
        return del_element()
    elif wybor_operacji =='3':#jesli 3 wywoluje funckcje ponizej
        return wywolanie_listy()
    elif wybor_operacji =='4':#jesli 4 wywoluje funckcje ponizej
        return clear_lista_zakupów()
    elif wybor_operacji == '5':#jesli 5 wywoluje funckcje ponizej
        return zakonczenie_programu()
    else:  # w innym wypadku informuje uzytkownika ze nie ma takie komendy/operacji
        print("Nie ma takiej operacji")
        print("Za chwilę załaduje sie menu")
        time.sleep(2)
        return menu_programu()  # i wraca do menu glownego programu
    


menu_programu()  #wywolanie poczatku programu ( funkcji menu_programu() )





