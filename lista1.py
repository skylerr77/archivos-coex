'''b1=False
animales=[]
opcion=0
while opcion!=4:
    opcion=int(input(''
---MENÚ---
Digite 1: Ingresar 10 nombres de animales.
Digite 2: Ingresar un número de 1 a 10 para ver el rango entre estos.
Digite 3: Nombre de un animal para verificar si esta en la lista.
Digite 4: Salir.
opción: ''))
    match opcion:
        case 1:
            for i in range (5):
                animales.append(input('Digite el nombre del animal: '))
            animales.sort()
            print(animales[:])
            b1=True
        case 2:
            if b1==True:
                numero=int(input('Digite un número del 1 al 10: '))
                print(animales[numero-1:])
            else:
                print('Te falta el paso 1')
        case 3:
            if b1==True:
                nombre=str(input('Digite el nombre de un animal: '))
                if nombre in animales:
                    print(f'El animal {nombre}, si se encuentra en la lista de animales')
                else:
                    print(f'El animal {nombre}, no se encuentra en la lista de animales')
            else:
                print('Te falta el punto 1')
        case 4:
            print('Fin del programa')
            break
        case _:
            print('No se encuentra dentro del rango')
else:
    print('No se encuentra dentro del rango')
'''
temp_string = "Hi my age is 32 years and 250 days12"
print(temp_string)

numbers = [int(temp)for temp in temp_string.split() if temp.isdigit()]

print(numbers)