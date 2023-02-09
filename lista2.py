'''arreglo=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
opcion=0
while opcion!=2:
    opcion=int(input('
---MENÚ---
Digite 1: Indique el número a buscar y mostrar la posición en la que se encuentra
Digite 2: salir
opción: '))
    match opcion:
        case 1:
            buscar=(int(input('Digite el número a buscar: ')))
            if buscar in arreglo:
                print(arreglo.index(buscar))
                for i in range(0,len(arreglo)):
                    if arreglo[i]==buscar:
                        print(arreglo[i].index(buscar))
                        
        case _:
            break
else:
    print('Fin')
           
suma=0
numeros=[33,55,77,81,48]
for i in range(0,len(numeros)):
    suma+=numeros[i]
print(f' Los números son: {numeros} y la suma es: {suma}')

usuario=['pepito89','supermogui','espernancacion']
con=['12345','password','qwerty123']
for i in range(len(usuario)):
    for j in range(len(con)):
        usuario=(input('Digite su usuario:'))
        con=(input('Digite su contraseña: '))
        if usuario in usuario and con in con:
            print('Bienvenido')
        else:
            print('Inconrrecto, le quedan dos intentos')
            usuario=(input('Digite su usuario:'))
            con=(input('Digite su contraseña: '))
            if usuario in usuario and con in con:
                print('Bienvenido')
                break
            else:
                print('Inconrrecto, le queda un intento')
                usuario=(input('Digite su usuario:'))
                con=(input('Digite su contraseña: '))
                if usuario in usuario and con in con:
                    print('Bienvenido')
                else:
                    print('Se acabaron sus intentos, adios')
                    break

cont=0
matriz=[]
sumaf=[]
sumac=[]
for fila in range(4):
    matriz.append([])
    for columna in range(6):
        matriz[fila].append((columna+1)+(fila*6))
        matriz[columna].append(matriz[fila])
        cont+=columna+1
        sumaf=sum(matriz[fila])
        sumac=sum(matriz[columna])
    print(sumaf)
    print(sumac)
print(end='')
print(matriz)


matriz=[1,2,3,4,5,6,7,8,9]
for fila in range(5):#Recorremos la lista con el tamaño de la misma
     print('[',end='') #imprimimos [ sin saltar de línea
     for columna in range(len(matriz[fila])):#Recorremos el tamaño de la lista en cada fila
         if columna<len(matriz[fila])-1: #Evaluamos si la posición es antes de la última
             print(matriz[fila][columna],end='\t ')#imprimimos el elemento en la posición fila y columna de la lista con tabulación
         else:
            print(matriz[fila][columna],end='') #imprimimos el elemento en la posición fila y columna de la lista sin tabulación
     print(']',end='') #imprimos el ] sin saltar
     print('') #imprimimos en blanco (salta de línea)
      matriz[fila].append((columna+1)+(fila*10))
     

listado=[]
f=1
while f!=0:   
    listado.append(input('Digite los nombres: '))
    f=int(input(''
    Digite 0 para no ingresar más: 
    Digite 1 para ingresar más:
    Digite su opción: ''))
print(listado)
copia=listado
copia.sort()
print(copia)


datos=[]
datos2=[]
for d in range(5):
    datos=input('Digite los datos: ')
for d2 in range(5):
    datos2=(input('Digite los datos 2: '))
    if datos2[d2] not in datos[d]:
         print(datos2)'''

import statistics

bogota='19,19,17,18,20' 
bucaramanga='27,26,26,26,27'
medellin='27,26,26,27,29'
opcion=0
while opcion!=4:
    opcion=int(input('''
Digite las siguientes opciones para saber la temperatura promedio, mayor 
y menor de la que elijas.
Digite 1: Bogota
Digite 2: Bucaramanga
Digite 3: Medellin
Digite 4:salir
Digite su opción: '''))
    match opcion:
        case 1:
            for x in bogota.split():
                if bogota.isdigit():
                    print('La temperatura promedio es: ',statistics.mean(bogota))
                    print('La mayor temperatura es: ',max(bogota))
                    print('La menor temperatura es: ',min(bogota))
        case 2:
                bucaramanga[:]
                print('La temperatura promedio es: ',statistics.mean(bucaramanga))
                print('La mayor temperatura es: ',max(bucaramanga))
                print('La menor temperatura es: ',min(bucaramanga))
        case 3:
                medellin[:]
                print('La temperatura promedio es: ',statistics.mean(medellin))
                print('La mayor temperatura es: ',max(medellin))
                print('La menor temperatura es: ',min(medellin))
        case 4:
            print('Hasta pronto')
            break
        case _:
            print('Este valor no se encuentra dentro del rango')

