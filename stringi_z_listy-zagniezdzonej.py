

#program ten wypisuje wszystkie obiekty string w liscie zagniezdzonej

lista = [
    ['1', 2, 3],
    ['a', 'b', 'c'],
    [True, 'False', True]
]


for klucz in lista:
    for element in klucz:
        if isinstance(element, str):
            print(element)
        else:
            continue

