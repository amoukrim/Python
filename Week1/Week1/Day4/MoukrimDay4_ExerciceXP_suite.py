# Step 1: Import the Dog Class
from dog import Dog  # import du fichier  dog.py
import random
# Step 2: Create the PetDog Class
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)# Call the parent constructor and set self.trained to False
        

        self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + [dogname for dogname in args]
        print(f"{', '.join(names)} all play together")


    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet.")
# Test PetDog Methods
dog1 = PetDog("Buddy", 3, 15)
dog2 = PetDog("Max", 2, 10)
dog3 = PetDog("Rocky", 4, 20)

# Train one dog
dog1.train()

# Make them all play
dog1.play(dog2.name, dog3.name)

# Try doing a trick
dog1.do_a_trick()

 #Exercise 4: Family and Person Classes
#Step 1 : Classe Person
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  # Initialisé à une chaîne vide

    def is_18(self):
        return self.age >= 18
#Step 2 : Classe Family
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # Liste d'objets Person

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No member with the first name '{first_name}' found.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        print("Family members:")
        for member in self.members:
            print(f"- {member.first_name}, {member.age} years old")
 #Test complet du comportement attendu

# Création d'une famille
my_family = Family("Dupont")

# Ajout de membres
my_family.born("Alice", 17)
my_family.born("Bob", 20)
my_family.born("Charlie", 12)

# Vérification de majorité
my_family.check_majority("Alice")    # Trop jeune
my_family.check_majority("Bob")      # Autorisé
my_family.check_majority("Zoe")      # Inexistant

# Présentation de la famille
my_family.family_presentation()