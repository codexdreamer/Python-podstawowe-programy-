   
#ciąg finobaciego

liczba_ciagu_ostatnia = 0
liczba_ciagu_przed_ostatnia = 0

print("0")
#while True: bedzie w nieskonczonosc pokazywac
while liczba_ciagu_ostatnia <2000:  #to pokaze tylko pare wartosci 
    if liczba_ciagu_ostatnia == 0:
        liczba_fb = 1
        liczba_ciagu_ostatnia = liczba_fb
        liczba_ciagu_przed_ostatnia = 0
    else:
        liczba_fb = liczba_ciagu_ostatnia + liczba_ciagu_przed_ostatnia
        
        temp = liczba_ciagu_ostatnia
        liczba_ciagu_ostatnia = liczba_fb
        liczba_ciagu_przed_ostatnia = temp

    print(liczba_fb)

