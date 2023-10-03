class Dog:
    def __init__(self, d_sound):
        self.d_sound = d_sound

    def d_display(self):
        print("Dog makes", self.d_sound)


class Cat:
    def __init__(self, c_sound):
        self.c_sound = c_sound

    def c_display(self):
        print("Cat makes", self.c_sound)


class Animal(Dog, Cat):
    def __init__(self, d_sound, c_sound, category):
        # super().__init__(d_sound)
        # super().__init__(c_sound)
        Dog.__init__(self, d_sound)
        Cat.__init__(self, c_sound)
        self.category = category

    def all_animals(self):
        print(f"cat and dogs are {self.category}")


a = Animal("woof", "meoww", "mammals")
a.d_display()
a.c_display()
a.all_animals()
