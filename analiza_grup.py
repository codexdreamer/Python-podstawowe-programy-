
grupa_a = {'Anna', 'Bartek', 'Tomek'}
grupa_b = {'Tomek', 'Ela'}


osoby_jednoczesne_AB = grupa_a & grupa_b

osobyA_lub_B = grupa_a ^ grupa_b

osobyAB = grupa_a | grupa_b

print("")
print("Osoby,które jednocześnie występują w grupie A i B:\n ")
for osoba in osoby_jednoczesne_AB:
    print(osoba)
print("")

print("Osoby,które występują tylko w jednej grupie A lub B:\n ")
for osoba in osobyA_lub_B:
    print(osoba)

print("")


print("Wszystkie osoby z grupy A i B:\n ")

for osoba in osobyAB:
    print(osoba)