

#Program wyświetla średnią,minimum,maksimum dla
#  5 pomiarów biegu na dystans 100m użytkownika


print("Podaj pierwszy pomiar w sekundach")
pomiar_1=float(input())

print("Podaj drugi pomiar w sekundach")
pomiar_2=float(input())
print("Podaj trzeci pomiar w sekundach")
pomiar_3=float(input())
print("Podaj czwarty pomiar w sekundach")
pomiar_4=float(input())
print("Podaj piąty pomiar w sekundach")
pomiar_5=float(input())

srednia =( pomiar_1 + pomiar_2 + pomiar_3 + pomiar_4 + pomiar_5) /5

maksimum = max(pomiar_1,pomiar_2,pomiar_3,pomiar_4,pomiar_5)

minimum = min(pomiar_1,pomiar_2,pomiar_3,pomiar_4,pomiar_5)

print("Średnia czasu wynosi:",srednia,"s")
print("Czas najdłuższy wynosi:",maksimum,"s")
print("Czas najkrótszy wynosi:",minimum,"s")