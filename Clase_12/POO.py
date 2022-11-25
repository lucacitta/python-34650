print('\n\n')





def descripcion(material, fluido, color):
    print(f'Esta botella es de {material}, tiene {fluido} y es de color {color}')







botella_1 = {'color':'transparente', 'fluido':'agua', 'material':'metal', 'tapa':True, 'reci':True}
botella_2 = {'color':'negra', 'fluido':'agua', 'material':'plastico', 'tapa':True, 'reci':True}
botella_3 = {'color':'verde', 'fluido':'te', 'material':'plastico', 'tapa':True, 'reci':True}
# def mostrar_color_botella(color):
#     print(f'la botella es de color {color}')


# auto_1 = {'color':'verde', 'puertas':4}


# mostrar_color_botella(auto_1['color'])




class Botella():
    def __init__(self, color, fluido='agua', material='plastico'):
        self.color = color
        self.fluido = fluido
        self.material = material


    def descripcion(self):
        print(f'Esta botella es de {self.material}, tiene {self.fluido} y es de color {self.color}')

botella_de_sefita = Botella('transparente', 'agua')
botella_de_contigo = Botella('gris', 'te', 'metal')
tetrabric = Botella('violeta', 'juguito de uva', 'carton')

botella_de_sefita.descripcion()

# mas_botellas = 'si'
# lista_botellas=[]
# while mas_botellas == 'si':
#     color = input('ingrese el color: ')
#     fluido = input('ingrese el fluido: ')
#     material = input('ingrese el material: ')
    
#     lista_botellas.append(Botella(color=color, fluido=fluido, material=material))
    
#     mas_botellas = input('Hay mas botellas?: ')

# print(lista_botellas)



























print('\n\n')