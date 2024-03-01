# ООП - обьекто орииентированное прогаммирование

class Car:
    # переменные внутри класса - свойство класса
    fars = 'True'
    def __init__(self, model, year, color): # конструктор класса
        self.model = model
        self.year = year
        self.color = color

    #функция внутри класса - метод
    def Fars(self):
        print(self.fars)

    def __str__(self):
        return f'model : {self.model}\n year : {self.year}\n color : {self.color}'

    def __len__(self):
        return len(self.fars) * 2
    
car1 = Car('Ford', 200, 'red')
car2 = Car('Toyota', 2020, 'black')
car3 = Car('bmw', 2024, 'red')

print(car1)
print(len(car1))
print(car1.model)
