class Farm:
    def __init__(self, farm_name):
         
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        lines = [f"{self.name}'s farm\n"]
        for animal, count in self.animals.items():
            lines.append(f"{animal} : {count}")
        lines.append("\n    E-I-E-I-0!")
        print("debug")
        return "\n".join(lines)

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        pluralized = []

        for animal in animal_types:
            if self.animals[animal] > 1:
                if animal.endswith('y') and not animal.endswith('ey'):
                    plural = animal[:-1] + "ies"
                elif animal.endswith('s'):
                    plural = animal + "es"
                else:
                    plural = animal + "s"
            else:
                plural = animal
            pluralized.append(plural)

        if len(pluralized) == 1:
            animals_str = pluralized[0]
        else:
            animals_str = ", ".join(pluralized[:-1]) + " and " + pluralized[-1]

        return f"{self.name}'s farm has {animals_str}."

# Création de la ferme
macdonald = Farm("McDonald")


#  Step 5: Test Your Code 
# Ajout d'animaux
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Affichage des infos
print(macdonald.get_info())
print()
print(macdonald.get_short_info())