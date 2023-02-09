'''x=int(input('DIGITE SU EDAD: '))
while x>0:
    x=int(input('DIGITE SU EDAD: '))
print('Fin del ciclo')
num1=int(input('Digite un numero: '))
num2=int(input('Digite un numero: '))
if num1>num2:
    while num1<=num2:
        if num2%2==0:
            print(num2)
            num2+=num1
        
elif num1<num2:
    while num2>num1:
        if num1%2==0:
            print(num1)
            num2+=num1
else:
    print('Los números son iguales')

i=0
suma=0
while i!=9999:
    i=int(input('Digite un número: '))
    if i!=9999:
        suma+=i
        if suma>0:
            print('mayor a 0')
        elif suma<0:
            print('menor a 0')
        else:
            print('es igual a 0')

    print('la suma es: ',suma)
i=1
suma=0
s=0
while i!=0:
    i=int(input('Digite un número: '))
    suma+=i
    print('la media es: ',suma)
y=0
x=2
while x<=2 and x>=0:
     clave=int(input('Digite su clave:'))
     if clave!=123456:
         y+=1
         print(f'Su clave es incorrecta lleva {y} intento(s) fallido(s), le queda {x} intento(s)')
         x-=1
     elif clave==123456:
         print('La clave es correcta')
         break
     '''

for i in range(1,101):
    cont=0
    for l in range (1,i+1):
        j=i%l
        if j==0:
            cont+=1
    if cont==2:
        print('es primo',i)
    


  