# ----------------------------------------------------------------
# Inheritance of the methods with the constructor methods

class Mammal :
    def __init__(self,animal, sound):
        self.name = animal
        self.sound = sound

    def sounds(self):
        print(f"{self.name} will sound like {self.sound}")

class Dog(Mammal) :
    def bark(self):
        print(f"{self.name} is very caring and barks all the time")

class Cat (Mammal):
    def rubbing(self) :
        print(f'{self.name} is very affectionate and rubbing my legs all the time')

print("Cat")
sony = Cat('sony', "Meow, Meow")
sony.rubbing()
sony.sounds()

print('----------------------------------------------------------------')
print("Dog")
snoopy = Dog('snoopy', "Bow Bow")
snoopy.bark()
snoopy.sounds()
