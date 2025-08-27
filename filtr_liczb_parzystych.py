
  
# program filtruje liczby z listy i wypisuje tylko parzyste 


liczby = [3, 8, 15, 22, 4, 7, 10, 13, 6]

a =list(filter(lambda x: x%2 == 0 , liczby))

print(a)