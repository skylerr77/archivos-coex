b1,b2,b3=False,False,False
menu=0
estudiantes=[]
nota=[]
matriz=[[estudiantes],[nota]]
suma=0
opcion=0
while opcion!=5:
    opcion=int(input('''--Digite una de las siguientes opciones--
1=Ingresar 5 estudiantes(lista)
2=Ingresar notas de cada estudiantes(lista)
3=Mostrar mayor nota y de que estudiante es
4=Mostrar estudiantes y notas
5.Salir
Digite su opción: '''))
    match opcion:
        case 1:
            for i in range(5):
                estudiantes.append((input('Digite su nombre: '))) 
        case 2:
            for j in range(5):
                nota.append(float(input('Digite su nota: ')))
        case 3:
            mayor=nota[0]
            for i in range(5):
                if nota[i]>mayor:
                        mayor=nota[i]
                        for i in range(5):
                            if nota[i]==mayor:
                                print(estudiantes[i],nota[i])
        case 4:
            for i in range(2):
                    for j in range(1): 
                        print(matriz[i])
                        print('')
        case _:
            break
print('Fin')











'''lista=[]
for i in range(10):
    lista.append(int(input('Digita un número: ')))
print(lista)

suma=0
import random
lista=[]
for i in range(1,10):
    lista.append((random.randint(1,10)))
    for j in range(1,10):
        suma+=lista[i]
print(lista)

lista=[10,0,3,61,9,20,17,8,2,1]
mayor=lista[0]
for i in range(1,10):
    if lista[i]>=mayor:
        mayor=lista[i]
print(mayor)

lista=[10,0,3,61,9,20,17,8,2,1]
menor=lista[0]
for i in range(1,10):
    if lista[i]<=menor:
        menor=lista[i]
print(menor)

        '''