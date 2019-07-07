import statistics 
from functools import reduce

def Promedio(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

suma=0
i=0
rango=len(velocidad)
sumatoria=sum(velocidad)
promedio = sumatoria/rango 
print(promedio)

promedio2= statistics.mean(velocidad) 
print(promedio2)

promedio3=Promedio(velocidad) 
print(promedio3)  



