nombres,curso,genero,promedio1=[],[],[],[]
c,g=0,0
opcion,f,m=1,0,0
while opcion!=0:
    print('BIENVENIDO AL SISTEMA DE LA ESCUELA PequeñosGamberos')
    nombres.append(input('Digite nombre del estudiante: '))
    c=int(input('Digite su curso: '))
    while c>=1 and c<=11:
        curso.append(c)
        g=str(input('Digite (f) si es femenino o (m) si es masculino: ').lower())
        if g=='f' or g=='m':
            genero.append(g)
            for i in range(3):
                notas=float(input(f'Digite nota {i+1}:'))
            if notas>=0 and notas<=5:
                notas+=notas
                promedio1=notas/3
                if promedio1>=3.5 and promedio1<=5:
                    promedio1.append(promedio1)

        else:
            print('error')
else:
    print('Su nota esta fuera del rango vuelva a intentarlo')
    opcion=int(input('''
Digite 0 para no ingresar más: 
Digite 1 para ingresar más:
Digite su opción: '''))
print(nombres)
print(curso)
print(genero)
print(promedio1)



