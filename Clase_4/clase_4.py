# edad = int(input('Ingrese su edad: '))
# if edad >= 18:
#     print('Es un adulto')
#     print('Es un adulto')
#     print('Es un adulto')
#     print('Es un adulto')

# print('fin del programa')

# entendieron = input('Entendiste? (si/no): ')
# if entendieron == 'si':
#     print('Excelente')
# else:
#     print('En donde te perdiste??')


# print('final del programa')


# a = 25
# b = 50
# if b > a:
#     print("b es más grande que a")

# llega_factura_luz = input('llego la factura? (si/no): ')
# tenes_plata = input('Tenes dinero para pagar? (si/no): ')

# if llega_factura_luz == 'si' and tenes_plata == 'si':
#     print('Entonces, a pagar la factura')
# else:
#     print('En otro momento sera...')


# llega_factura_luz = input('llego la factura? (si/no): ')

# if llega_factura_luz == 'si':
#     print('llego la factura')
#     tenes_plata = input('Tenes dinero para pagar? (si/no): ')
#     if tenes_plata == 'si':
#         print('podemos pagarla, la pagamos')
#     else:
#         print('pero no la podemos pagar')
# else:
#     print('No llego la factura')


# mascota = input('Que mascota tenes?: ')

# if mascota == 'perro': #si se cumple
#     print('Guaw Guaw')      #haces esto
# elif mascota == 'gato':#sino se cumplio lo anterior y esto se cumple
#     print('Miau Miau')      #haces esto
# elif mascota == 'pez':#sino se cumplio lo anterior y esto se cumple
#     print('...')            #haces esto
# else:          #si no se cumplio nada de lo anterior
#     print('no se que mascota tenes') #haces esto


# numero = int(input('ingresa un numero: '))

# if numero > 10:
#     print('es mayor a 10')
# elif numero > 8:
#     print('es mayor a 8')  
# elif numero > 6:
#     print('es mayor a 6')



#<-------------ESTOS 3 BLOQUES HACEN EXACTAMENTE LO MISMO--------------->

# edad = int(input('ingrese su edad: '))

# if edad > 21:
#     print('podes tomar y votar')
# elif edad > 18:
#     print('podes votar')
# else:
#     print('podes tomar y votar')


# if edad > 21:
#     print('podes tomar y votar')
# if edad > 18 and edad < 21:
#     print('podes votar')
# else:
#     print('podes tomar y votar')

# if edad < 21:
#     if edad < 18:
#         print('no podes hacer nada')
#     else:
#         print('Podes votar')
# else:
#     print('podes tomar y votar')

#<-------------ESTOS 3 BLOQUES HACEN EXACTAMENTE LO MISMO--------------->



#<-------------ACTIVIDAD 1--------------->

# edad = int(input())

# if edad >= 1920 and edad <= 1940:
#     print("Generación Silenciosa")

# elif edad >= 1946 and edad <= 1964:
#     print("Baby Boomer")

# elif edad >= 1965 and edad <= 1979:
#     print("Generación X")

# elif edad >= 1980 and edad <= 2000:
#     print("Generación Y")

# elif edad >= 2001 and edad <= 2010:
#     print("Generación Z")

# else:
#     print("No pertenece a ninguna generación")

#<-------------ACTIVIDAD 1--------------->



#<-------------ACTIVIDAD 2--------------->

# '''
# Para aprobar el credito debe ser mayor, tener 3 años de antiguedad como minimo y ganar 2500 dolares o mas
# En caso de no tener la antiguedad suficiente debe ganar 4000 como minimo
# '''

# edad = 15
# antigüedad = 10
# ingreso = 1500

# if edad > 18:
#     if antigüedad >= 3:
#         if ingreso >= 2500:
#             print('El credito esta aprobado')
#         else:
#             print('El credito no esta aprobado')
#     else:
#         if ingreso >= 4000:
#             print('El credito esta aprobado')
#         else:
#             print('El credito no esta aprobado')
# else:
#     print('El credito no esta aprobado')

# if edad > 18:
#     if antigüedad >= 3 and ingreso >= 2500:
#         print('El credito esta aprobado')
#     elif ingreso >= 4000:
#         print('El credito esta aprobado')
#     else:
#         print('El credito no esta aprobado')
# else:
#     print('El credito no esta aprobado')


# if edad > 18 and antigüedad >= 3 or ingreso >= 2500:  ESTA NO ESTA TERMINADA
#     print('El credito esta aprobado')



#<-------------ACTIVIDAD 2--------------->
