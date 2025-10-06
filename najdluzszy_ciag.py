dane = [2,1,2,2,2,1,2,2,2,3,1,1,1,1,1,1,1,1,1,0]


ile_razy = 1

nowe = 0


for i in range(1,len(dane)-1 ):
    if dane[i] == dane[i+1]:
        ile_razy += 1
    else:
        if ile_razy > nowe:
            nowe = ile_razy
        ile_razy = 1
            
        
if ile_razy > nowe:
    nowe = ile_razy


print(nowe)
        
        


  

    
