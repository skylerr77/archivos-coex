print('***CALCULADORA***')
val1=float(input('Digite el primer valor '))
val2=float(input('Digita el segundo valor '))
print('***INGRESA 1: SUMA***')
print('***INGRESA 2: RESTA***')
print('***INGRESA 3: MULTIPLICACIÓN***')
print('***INGRESA 4: DIVISIÓN***')
opcion=int(input("Digite que operación desea realizar "))
match opcion:
    case 1:
        r1=val1+val2
        print(r1)
    case 2:
        r2=val1-val2
        print(r2)
    case 3:
        r3=val1*val2
        print(r3)
    case 4:
        if val2==0 :
            print('No es posible dividir entre cero')
        else :
            print(val1/val2)
    case _:
        print("Operación no encontrada")