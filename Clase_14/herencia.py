print('\n\n')






class Vehiculo():

    def __init__(self, color, marca, modelo, año):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def print_data(self):
        print('Color: ', self.color)
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Año: ', self.año)

    def prender(self):
        print('El vehiculo esta corriendo')

class Auto(Vehiculo):

    def __init__(self, color, marca, modelo, año, puertas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.puertas = puertas

    def prender(self):
        print('El auto esta corriendo')

    def andar_para_atrass(self):
        print('El auto esta andando para atrass')

class Moto(Vehiculo):

    def __init__(self, color, marca, modelo, año, casco):
        super().__init__(color, marca, modelo, año)
        self.casco = casco

    def prender(self):
        print('La moto esta corriendo')

    def hacer_willy(self):
        print('La moto esta haciendo willy')

    def print_data(self):
        super().print_data()
        print('Casco: ', self.casco)



# vehiculo_1 = Vehiculo('blanco', 'Ford', 'Fiesta', 2018)
auto_1 = Auto('Rojo', 'vw', 'Fiesta', 2019, 4)
moto_1 = Moto('verde', 'honda', 'Fiesta', 2020, 'b52')

# vehiculo_1.prender()
# auto_1.andar_para_atrass()
# print(type(moto_1).__name__)
print(auto_1.andar_para_atrass())
























print('\n\n')