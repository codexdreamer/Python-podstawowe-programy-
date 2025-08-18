from random import randrange
import random

#bot gra jako : x
#uzytkownik gra jako: o
import time
print("")
print("Witaj w grze kółko i krzyżyk")
time.sleep(2)
print("Zaczynasz jako ,,o")
time.sleep(2)
print("Ja zaczynam :)")  
time.sleep(2)              # wstep (wykonywany jednorazowo na samym poczatku)




slownik_ruchow={                 #slownik zapisujacy ruchy 
    '1':'0',
    '2':'0',
    '3':'0',             
    '4':'0',
    '5':'0',
    '6':'0',
    '7':'0',
    '8':'0',
    '9':'0'

}


def tablica_gry():
    def pole(nr):
        return slownik_ruchow[nr] if slownik_ruchow[nr] != "0" else nr

    print(" ")
    print(" ")
    print("-------------------------------------")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("|    ",pole("1"),"   ","|    ",pole("2"),"   ","|    ",pole("3"),"   ","|")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("-------------------------------------")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("|    ",pole("4"),"   ","|    ",pole("5"),"   ","|    ",pole("6"),"   ","|")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("-------------------------------------")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("|    ",pole("7"),"   ","|    ",pole("8"),"   ","|    ",pole("9"),"   ","|")
    print("|    "," ","   ","|    "," ","   ","|    "," ","   ","|")
    print("-------------------------------------")
    print(" ")
    print(" ")


def losowanie_pola_BOT():
    print("Tak wygłada tablica gry aktualnie:")
    tablica_gry()
    print("")
    pole = random.randint(1,9)  
    pole = str(pole)
    if pole in slownik_ruchow:
        if slownik_ruchow[pole] == "0":
            slownik_ruchow[pole] = "x"
            wynik = sprawdzanie_wygranej()
            if wynik:
            
                tablica_gry()
                print(wynik)
                exit()
            print("---------------------------------------------------")
            print("Tak wygląda tablica gry po moim ruchu!")
            return wybor_pola_uzytkownik()
        else:
            
            return losowanie_pola_BOT()
    else:
        return losowanie_pola_BOT()



def wybor_pola_uzytkownik():

    #print("")
    tablica_gry()
    print(" ")
    print("Podaj numer pola!")
    wybor=input()
    wybor=str(wybor)
    if wybor in slownik_ruchow:
        if slownik_ruchow[wybor] == "0":
            slownik_ruchow[wybor] = "o"
            sprawdzanie_wygranej

            wynik = sprawdzanie_wygranej()
            if wynik:
                tablica_gry()
                print(wynik)
                exit()
        
            return losowanie_pola_BOT()
            
        else:
            print("Wskazane pole jest już zajęte bądź nie istnieje!")
            return wybor_pola_uzytkownik()
    else:
        print("Wskazane pole jest już zajęte bądź nie istnieje!")
        return wybor_pola_uzytkownik()


    
    
def sprawdzanie_wygranej():
   if slownik_ruchow["1"] == "x" and slownik_ruchow["2"] == "x" and slownik_ruchow["3"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["4"] == "x" and slownik_ruchow["5"] == "x" and slownik_ruchow["6"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["7"] == "x" and slownik_ruchow["8"] == "x" and slownik_ruchow["9"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["1"] == "x" and slownik_ruchow["4"] == "x" and slownik_ruchow["7"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["2"] == "x" and slownik_ruchow["5"] == "x" and slownik_ruchow["8"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["3"] == "x" and slownik_ruchow["6"] == "x" and slownik_ruchow["9"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["1"] == "x" and slownik_ruchow["5"] == "x" and slownik_ruchow["9"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   elif slownik_ruchow["3"] == "x" and slownik_ruchow["5"] == "x" and slownik_ruchow["7"] == "x":
       print("Niestety przegrałeś! Wygrał Bot!")
       return nowe_ropoczecie()
   if slownik_ruchow["1"] == "o" and slownik_ruchow["2"] == "o" and slownik_ruchow["3"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["4"] == "o" and slownik_ruchow["5"] == "o" and slownik_ruchow["6"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["7"] == "o" and slownik_ruchow["8"] == "o" and slownik_ruchow["9"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["1"] == "o" and slownik_ruchow["4"] == "o" and slownik_ruchow["7"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["2"] == "o" and slownik_ruchow["5"] == "o" and slownik_ruchow["8"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["3"] == "o" and slownik_ruchow["6"] == "o" and slownik_ruchow["9"] == "o":
      print( "Gratulację WYGRAŁEŚ!!")
      return nowe_ropoczecie()
   elif slownik_ruchow["1"] == "o" and slownik_ruchow["5"] == "o" and slownik_ruchow["9"] == "o":
       print( "Gratulację WYGRAŁEŚ!!")
       return nowe_ropoczecie()
   elif slownik_ruchow["3"] == "o" and slownik_ruchow["5"] == "o" and slownik_ruchow["7"] == "o":
       print( "Gratulację WYGRAŁEŚ!!")
       return nowe_ropoczecie()

   elif all(wartosc != "0" for wartosc in slownik_ruchow.values()):
        print("Gra zakończyła się REMISEM!")
        return nowe_ropoczecie()

   else:
       return None


def resetuj_gre():
    global slownik_ruchow
    slownik_ruchow = {
    '1': '0',
    '2': '0',
    '3': '0',
    '4': '0',
    '5': '0',
    '6': '0',
    '7': '0',
    '8': '0',
    '9': '0'   }
    return losowanie_pola_BOT()


def nowe_ropoczecie():
    print(" ")
    print("Czy chcesz zagrać jeszcze raz?")
    print("t-tak")
    print('n-nie')
    print("")
    wybor_wyboru=input()
    wybor_wyboru=str(wybor_wyboru)
    if wybor_wyboru == "t":
        return resetuj_gre()
    elif wybor_wyboru =="n":
        print("Miło było z tobą zagrać!")
        exit()
    else:
        print("Nie właściwy format!")
        print("Spróbuj ponownie!")
        return nowe_ropoczecie()

losowanie_pola_BOT()
        
    







     
    

   
   

    



    
   


    
        

    


    









    







