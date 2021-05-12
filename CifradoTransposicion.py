# PROGRAMA REALIZADO POR CHRISTOPHER OCAÑA AMEZCUA 
# EN EL CUÁL EL TAMAÑO DE LA MATRIZ ES FIJO A 7, PERO SE PUEDE CAMBIAR DESDE EL CÓDIGO.

import numpy as np
import random

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mensajeEncriptado = ""
tamaño = 7
mensajeParaEncriptar = input("Ingresa el mensaje a encriptar: ").upper()
matriz = np.array([['A']*tamaño,
                   ['A']*tamaño,
                   ['A']*tamaño,
                   ['A']*tamaño,
                   ['A']*tamaño,
                   ['A']*tamaño,
                   ['A']*tamaño])


k = 0
i = 0
while i < tamaño:
    j = 0
    while j < tamaño:
        
        if k < len(mensajeParaEncriptar):
            matriz[i][j] = mensajeParaEncriptar[k]
            k += 1
        else:
            index = random.randint(1,len(abc)) % len(abc)
            matriz[i][j] = abc[index]

        j += 1
    i += 1


# Obtener el texto cifrado
i = 0
while i < tamaño:
    j = 0 
    while j < tamaño:
        mensajeEncriptado += matriz[j][i]
        j += 1
    mensajeEncriptado += " "
    i += 1


print(matriz)
print("\n\nTEXTO CIFRADO: ",mensajeEncriptado)

# JUVENTUDDIVINOTESOROYAQUETEVASPARANOVOLVER
