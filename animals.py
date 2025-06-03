class Shelter:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def show_animals(self):
        if not self.animals:
            print("Приют пуст.")
        else:
            for animal in self.animals:
                animal.display_info()
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
    shelter = Shelter()
    print(shelter.animals)
    shelter.add_animal(my_animal)
    
print(f"В приюте сейчас {len(shelter.animals)} животных.")
for animal in shelter.animals:
    animal.display_info()
