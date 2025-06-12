#Exercise 1: Pets

# Base Classes

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Cat Breeds

class Bengal(Cat):
    def sing(self, sounds):
        return f'{self.name} sings: {sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{self.name} sings: {sounds}'

# ✅ Step 1: Create the Siamese Class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{self.name} sings: {sounds}'
    
    def talk(self):
        return f'{self.name} says "meow" in a loud Siamese voice'

# ✅ Step 2: Create a list of cat instances
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Luna", 4)
siamese_cat = Siamese("Milo", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# ✅ Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# ✅ Step 4: Take cats for a walk
sara_pets.walk()

#Exercise 2: Dogs
# class Dog():
#     def __init__(self, name, age, weight):
#         self.name=name
#         self.age=age
#         self.weight=weight 
#     def bark(self):
#         return("is barking")
#     def run_speed(self):#weight / age * 10
#             return self.weight/self.age*10
#     def fight(self, other_dog):
#         #run_speed * weight
#         winner = self if self.run_speed()* self.weight>other_dog.run_speed()* other_dog.weight else other_dog
#         print(f"the winner is {winner.name}")
#         return winner.name   
# dog1 = Dog("Rockey", 7, 30)
# dog2 = Dog("Milou", 2, 15)
   
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))

#Step 1: Create the Dog class

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}!"
        elif other_power > self_power:
            return f"{other_dog.name} wins the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"
# Step 2: Create Dog Instances

dog1 = Dog("Rex", 5, 25)
dog2 = Dog("Bella", 3, 20)
dog3 = Dog("Max", 4, 30)
# Step 3: Test Dog Methods

print(dog1.bark())
print(f"{dog2.name}'s run speed is {dog2.run_speed():.2f}")
print(dog1.fight(dog3))
print(dog2.fight(dog3))    
#Exercice 