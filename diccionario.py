# import statistics

# estudiantes=[]
# alumnos={}
# nota=[]

# cant=int(input('Ingrese la cantidad de estudiantes: '))
# for i in range(cant):
#     alumnos['nombre']=input('nombre')
#     c=int(input('Curso'))
#     while c < 1 or c > 11:
#         c=int(input('Curso'))
#     else:
#         alumnos['curso'] = c
#     alumnos={}
#     g=str(input('Digite (f) si es femenino o (m) si es masculino: ').lower())
#     while g !='f' and g !='m':
#         print('vuelva a ingresar el genero')
#         g=input('Digite (f) si es femenino o (m) si es masculino: ').lower()
#     else:
#         alumnos['genero']=g
#     alumnos={}
#     for i in range(3):
#         notas=float(input(f'Digite nota {i+1}:'))
#         while notas<0 or notas>5:
#             notas=float(input(f'Digite nota {i+1}:'))
#             nota.append(notas)
#             statistics.mean(nota)
#             print(nota)
#         """ if promedio1>=3.5 and promedio1<=5:
#                 alumnos['promedio']=promedio1 """



# numeros = [1,2,3,45,6,"juanjose"] #Lista
# cielo = {
#     "nombre": "cielo",
#     "edad": 23
# } #diccionario

# leidy = {
#     "nombre": ""
# }
# print(leidy)
# leidy["nombre"] = input('Digite su nombre: ')
# leidy["edad"] = input('Edad ')
# print(leidy)
# estudiantes = [cielo, leidy]
'''
alumno = {}
alumnos = []
for i in range(3):
    alumno["nombre"] = input('Nombre ')
    alumno["edad"] = input('edad ')
    print(alumno)
    alumnos.append(alumno)
    alumno = {}
print(alumnos)
# print(numeros[3])
# print(estudiantes)

empleado={}
cantidad=int(input('Digite la cantidad de empleados: '))
for i in range (cantidad):
    empleado["nombre"] = str(input('Digite su nombre: '))
    empleado["antiguedad"]= int(input('Digite ¿cuantos años lleva en la empresa?: '))
    cantidadhora = float(input('Digite la cantidad de horas trabajadas en el mes: '))
    empleado["valorh"]=float(input('Digite el valor de la hora: '))
    trabajados = empleado["antiguedad"]*30 
    empleado["total"]=(empleado["valorh"]*cantidad)+trabajados
    empleado["descuento"]=empleado["total"]*0.13
    empleado["importe"] = empleado["total"]-empleado["descuento"]
    print(f''
---RECIBO---
Nombre: {empleado["nombre"]}
Antiguedad: {empleado["antiguedad"]}
Valor de la hora: {empleado["valorh"]}
Total a cobrar en bruto: {empleado["total"]}
Total de descuento: {empleado["descuento"]}
Valor neto a cobrar: {empleado["importe"]}
'')
    empleado={}

alumnos,l=[],[]
alumno={}
mayor=0
cantidad=int(input('Digite la cantidad de estudiantes a ingresar: '))
for i in range (cantidad):
    alumno["codigo"] = str(input('Digite el código del estudiante: '))
    alumno["nombre"] = str(input('Digite el nombre del estudiante: '))
    alumno["promedio"] = float(input('Digite el promedio del estudiante: '))
    alumnos.append(alumno)
    alumno={}
opcion=0
while opcion!=5:
    opcion=int(input(''
---Materia de Matemáticas---
Digite 1: Nombre y promedio.
Digite 2: Alumnos que aprobaron.
Digite 3: Alumnos que habilitan.
Digite 4: Alumnos con mejor promedio.
Digite 5: Salir.
Digite una opción: ''))
    match opcion:
        case 1:
            print(alumnos)
        case 2:
            for j in alumnos:
                if j["promedio"]>=7:
                    print(f'El alumno {j["nombre"]} aprobó')
        case 3:
            for j in alumnos:
                if j["promedio"]<7 and j["promedio"]>=4:
                    print(f'El alumno {j["nombre"]} Habilita en Diciembre')
                elif j["promedio"]<4:
                    print(f'El alumno {j["nombre"]} Habilita en Marzo')
        case 4:
            for j in range(cantidad):
                if alumnos[j]["promedio"]>=7:
                    l.append(alumnos[j]["promedio"])
                    if max(l):
                        print(f'El alumno {alumnos[j]["nombre"]} tiene el mayor promedio')
        case 5:
            print('Fin')
            break
        case _:
            print('Valor fuera del rango')
print('Valor fuera del rango')

'''

c=[1,2,3,3]
l=input('digite')
print(c.count(c))

        












 






















