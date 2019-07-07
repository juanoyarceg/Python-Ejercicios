# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:39:36 2019

@author: JUAN
"""
numero = int(input("Ingrese el numero de pares que quiere obtener \n"))

for i in range (numero):
    par = numero -i*2
    print("Iteracion {}".format(par ))
    i+=1
