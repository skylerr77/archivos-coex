factura=float(input('Digite el valor de su factura: '))
cantidad=int(input('Digite la cantidad facturada: '))
if cantidad>=1000 :
    t1=(cantidad*factura)-((cantidad*factura)*0.1)
    print('Tienes un descuento del 10%')
    print('Su valor total a pagar es: ',t1)
elif cantidad>=500 and cantidad<=999:
    t2=(cantidad*factura)-((cantidad*factura)*0.08)
    print('Tienes un descuento del 8%')
    print('Su valor total a pagar es: ',t2)
elif cantidad>=200 and cantidad<=499:
    t3=(cantidad*factura)-((cantidad*factura)*0.05)
    print('Tienes un descuento del 5%')
    print('Su valor total a pagar es: ',t3)
elif cantidad>200:
    print('No tienes un descuento')
    print('Su valor total a pagar es: ',factura)
else :
    print('error')


