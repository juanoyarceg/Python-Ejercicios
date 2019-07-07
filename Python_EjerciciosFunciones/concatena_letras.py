import string
nletras = int(input('Ingrese el numero de letras:\n'))
def gen(nletras):
    if nletras<= 26: 
        alfabeto= string.ascii_lowercase[:nletras]
    else:
        alfabeto=(string.ascii_lowercase*nletras)[:nletras]
    return alfabeto 

 

 