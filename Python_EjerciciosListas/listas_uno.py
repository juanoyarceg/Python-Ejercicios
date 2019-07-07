auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

autofull= (auto1+auto2+auto3+auto4+auto5+auto6)


autos  = []
campo2 = []
campo3 = []
campo4 = []
campo5 = []


 
for index, elemento in enumerate(autofull):
    if index == 0 or index % 5 == 0:
        autos =  elemento
    if index == 1 or index % 3 == 0:
        autos =  elemento
    if index == 2 or index % 2 == 0:
        autos =  elemento
    if index == 3 or index % 5 == 0:
        autos =  elemento
    if index == 4 or index % 5 == 0:
        autos =  elemento

print(autos)
