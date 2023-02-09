acumulador=0
opcion=0
nota=-1
bandera1=False
bandera2=False
bandera3=False
bandera4=False
while opcion!=6:
    opcion=int(input('''
1.Ingresar el nombre de un estudiante 
2.Ingrear las notas de un estudiante
3.Mostrar la nota definitiva de un estudiante
4.Mostrar si el estudiante aprueba o no la materia 
5.Mostrar el nombre del estudiante, la nota definitiva, la nota definitiva y si aprobó o no la materia 
6.Salir
Digita una opción: '''))
    match opcion:
        case 1:
            nombre=input('Digita el nombre de un estudiante: ')
            bandera1=True
        case 2:
            if bandera1==True:
                for i in range(5):
                    
                    while nota<0 or nota>5:
                        nota=float(input(f'Digita la nota: {i+1} '))
                    acumulador+=nota
                definitiva=acumulador/5
                bandera2=True
            else:
                print('Aún te flata el paso 1 ')
        case 3:
            if bandera1==True and bandera2==True:
                print(definitiva)
                bandera3=True
            else:
                print('Aún te flata el paso 1 y 2')
        case 4:
            if bandera2==True and bandera2==True and bandera3==True:
                if definitiva>3.5:
                    print('Aprobó') 
                    estado='aprobo'
                else:
                    print('Reprobó')
                    estado='reprobo'
                    bandera4==True
        case 5:
            if bandera1==True and bandera2==True and bandera3==True and bandera4==True:
                print(f'Nombre: {nombre} Definitiva: {definitiva} y {estado}')
        case 6:
            break

