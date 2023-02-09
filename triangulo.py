dividendo=int(input('Digite el dividendo: '))
divisor=int(input('Digite el divisor: '))
if divisor!=0:
    r=0
    while dividendo>=divisor:
        dividendo-=divisor
        r+=1
    print('el residuo es:',dividendo)
    print('el cociente es:',r)
else:
    print('error')

