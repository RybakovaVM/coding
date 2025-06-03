class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
if __name__ == "__main__":
    my_animal = Animal(name ="Шарик", species="собака", age=1)
print(f"Имя: {my_animal.name}")
print(f"Вид: {my_animal.species}")
print(f"Возраст: {my_animal.age}")
