# #<----------------------------------------------------------------------------------------------------->


# diccionario_vacio = {}
# print('Diccionario vacio:', diccionario_vacio)
# print(type(diccionario_vacio))

# diccionario_profe = {'nombre':'Luca', 'apellido':'Citta Giordano', 'edad':23}
# print(diccionario_profe)


# diccionario_profe = {
#     'nombre':'Luca', 
#     'apellido':'Citta Giordano', 
#     'edad':23,
#     'alumnos':[{'nombre':'Carlos'}, {'nombre':'Matias'}]
#     }
# print(diccionario_profe)








# #<----------------------------------------------------------------------------------------------------->






# diccionario_trabalenguas = {'nombre':'Pablito', 'accion':'Clavar clavito', 'cuantos': 1, 'donde':'En la calva de un calvito'}

# print('Diccionario trabalenguas:', diccionario_trabalenguas)

# print('Diccionario clave nombre:', diccionario_trabalenguas['nombre'])





# #<----------------------------------------------------------------------------------------------------->



# diccionario_trabalenguas['donde'] = 'En la pared...'
# print('Diccionario un poco mas responsable:', diccionario_trabalenguas)







# #<----------------------------------------------------------------------------------------------------->






# diccionario_trabalenguas['nueva_clave'] = 'Esto es legal?'
# print('Diccionario con nueva clave?: ', diccionario_trabalenguas)







# #<----------------------------------------------------------------------------------------------------->




diccionario_colores = {}

diccionario_colores.update({'rojo':'red', 'azul':'blue','amarillo':'yellow', 'morado':''})

print('Diccionario re colorido y divertido:', diccionario_colores)

print(len(diccionario_colores))



# #<----------------------------------------------------------------------------------------------------->




#del diccionario_colores['dorado']
del diccionario_colores['morado']
print('Diccionaro post del:', diccionario_colores)






# #<----------------------------------------------------------------------------------------------------->





print('Esta el dorado en el diccionario?', 'dorado' in diccionario_colores)
print('Esta el blue en el diccionario?', 'blue' in diccionario_colores)
print('Esta el azul en el diccionario?', 'azul' in diccionario_colores)







# #<----------------------------------------------------------------------------------------------------->