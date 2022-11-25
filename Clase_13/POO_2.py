class My_list():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value

var = [1,2,3,4,5]
lista = list(var)
mi_lista = My_list(var)

print('----------------------------------------------------\n\n')


print('Lista de Python: ', lista[0])
lista[0] = 10
print('Lista de Python: ', lista[0])


print('\n\n----------------------------------------------------\n\n')


print('Mi lista: ', mi_lista[0])
mi_lista[0] = 10
print('Mi lista: ', mi_lista[0])


print('\n\n----------------------------------------------------')

class Menu():
    def __init__(self, name, price, ingredients , secret_ingredient = None):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.__secret_ingredient = secret_ingredient
    
    def __str__(self):
        return self.name

    def description(self):
        message = f'La comida es un {self.name} y tiene estos ingredientes: '
        for ingredient in self.ingredients:
            message += f'{ingredient}, '
        return message[:-2]

    def full_description(self):
        message = f'La comida es un {self.name} y tiene estos ingredientes: \n'
        for ingredient in self.ingredients:
            message += f'\n{ingredient.descripcion()}'
        return message

    def has_secret_ingredient(self):
        if self.__secret_ingredient is not None:
            return True
        return False

    def is_ingredient(self, ingredient):
        if ingredient == self.__secret_ingredient or ingredient in self.ingredients :
            return True
        return False

class Ingredient():
    def __init__(self, name, expiration, is_natural):
        self.name = name
        self.expiration = expiration
        self.is_natural = is_natural

    def __str__(self):
        return self.name

    def descripcion(self):
        return f'{self.name} vence el {self.expiration} y {self.is_natural} es natural'

ingrediente_1 = Ingredient('Pimiento', '15/12/2022', 'si')
ingrediente_2 = Ingredient('Cebolla', '30/11/2022', 'si')
ingrediente_3 = Ingredient('Pollo', '/07/2022', 'si')
ingrediente_4 = Ingredient('Saborizante alicante', '20/19/2024', 'no')
ingrediente_5 = Ingredient('Lechuga', '30/11/2022', 'si')
ingrediente_6 = Ingredient('Harina', '8/07/2023', 'no')

comida_1 = Menu('Wok de verduras', '10', [ingrediente_1, ingrediente_2, ingrediente_3], ingrediente_4)


print('----------------------------------------------------\n\n')
print(comida_1.is_ingredient(ingrediente_4))
print(comida_1.__secret_ingredient)
print('\n\n----------------------------------------------------')
