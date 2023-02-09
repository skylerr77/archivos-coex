'''1.Sumar una cantidad N números MAYORES a 0 utilizando MIENTRAS.
i=int(input('Digite un número: '))
suma=0
while (i!=0 and i>0):
    suma+=i
    print(suma)
    i=int(input('Digite un número: '))
else:
    print('error')

2.Imprimir números aleatorios en el rango de 0 a 10 mientras el número no sea igual a cero.
import random
x=random.randint(0,10)
while x!=0:
        print(x,end=' ')
        x=random.randint(0,10)
        
3.Imprimir 20 números aleatorios en el rango de 1 a 1000.
import random
for i in range (1,21):
    while i>=1:
        print(random.randint(1,1000))
        break

4.Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números impares desde 1 hasta ese número.
x=int(input('Digite un número entero positivo: '))
for i in range (1,x+1):
    if i%2==1:
        print('Los números impares son: ',i)

5. Una persona debe realizar un muestreo con 20 personas para determinar el promedio de peso
de los niños, jóvenes, adultos y viejos que existen en su zona habitacional. Se determinan las
categorías con base en la sig., tabla:

6.Diseñen un algoritmo que imprima la siguiente secuencia:
1.1.1 - 1.1.2 - 1.1.3 - 1.1.4
1.2.1 - 1.2.2 - 1.2.3 - 1.2.4
1.3.1 - 1.3.2 - 1.3.3 - 1.3.4
1.4.1 - 1.4.2 - 1.4.3 - 1.4.4
1.5.1 - 1.5.2 - 1.5.3 - 1.5.4
for i in range(1,6):
    print(f'1.{i}.1 - 1.{i}.2 - 1.{i}.3 - 1.{i}.4')

7. Un Zoólogo pretende determinar el porcentaje de animales que hay en las siguientes tres
categorías de edades: de 0 a 1 año, de más de 1 año y menos de 3 y de 3 o más años. El
zoológico todavía no está seguro del animal que va a estudiar. Si se decide por elefantes solo
tomara una muestra de 20 de ellos; si se decide por las jirafas, tomara 15 muestras, y si son
chimpancés tomara 40.'''
edad=int(input('Digite la edad del animal: '))
opcion=int(input('''
Digite 1:Elefantes
Digite 2:Jirafas
Digite 3:Chimpancés
: '''))
cont,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8=0,0,0,0,0,0,0,0,0
suma,suma2,suma3=0,0,0
veces=0
if opcion==1:
    while veces<=20:
        if edad>=0 and edad<=1:
            cont+=1
        elif edad>1 and edad<3:
            cont1+=1
        elif edad>=3:
            cont2+=1
elif opcion==2:
    while veces<=15:
        if edad>=0 and edad<=1:
            cont3+=1
        elif edad>1 and edad<3:
            cont4+=1
        elif edad>=3:
            cont5+=1
elif opcion==3:
    while veces<=40:
        if edad>=0 and edad<=1:
            cont6+=1
        elif edad>1 and edad<3:
            cont7+=1
        elif edad>=3:
            cont8+=1
suma=cont+cont1+cont2
suma2=suma/cont




