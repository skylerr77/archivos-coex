deposito=float(input('Digite el valor del depósito: '))
tiempo=float(input('Digite el tiempo: '))
if tiempo>24:
    interes=18/12
elif tiempo<=19:
    interes=15/12
elif tiempo<=13:
    interes=10/12
elif tiempo==0 and tiempo<=6:
    interes=8/12
mes=deposito/tiempo
print('Su ganancia mensual es de:',mes)
t=(mes*tiempo)
print('Su valor por todos los meses: ',t)
descuento=((t*interes/100)*12)
print('Su ganancia total con los intereses es: ',descuento)
