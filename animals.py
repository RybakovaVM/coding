class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def display_info(self):
        print(f"Имя: {my_animal.name}, Вид: {my_animal.species}, Возраст: {my_animal.age}")
if __name__ == "__main__":
    my_animal = Animal("Шарик", "собака", 1)
    my_animal.display_info()
