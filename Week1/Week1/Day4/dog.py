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