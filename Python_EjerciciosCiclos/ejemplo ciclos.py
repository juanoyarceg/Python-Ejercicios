"""
for i in range(10):
    for j in range(10):
        print("{}*{}={}".format(i,j,(j*i)))
"""
n= int(input("ingresa un numero"))

contain=""

for i in range(n+1):
    for j in range (i):
        contain +='*'
    contain+='\n'
print (contain)

contain=''
for i in range(n):
    for j in range(n-i):
        contain += '*'
    contain += '\n'

print(contain)



     
