recibo=float(input('Digite el valor de su factura '))
estrato=input('Digite a que estrato pertenece ')
match estrato :
    case '1':
        print(recibo-recibo*10/100)
    case '2':
        print(recibo-recibo*8/100)
    case '3':
        print(recibo-recibo*6/100)
    case '4':
        print(recibo-recibo*4/100)
    case _: 
        print('error')
