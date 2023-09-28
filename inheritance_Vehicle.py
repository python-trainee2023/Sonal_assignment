class Vehicle:
    def __init__(self, v_name, v_model, v_year):
        self.v_name = v_name
        self.v_model = v_model
        self.v_year = v_year

    def display(self):
        print("Car Details:", self.v_name, self.v_model, self.v_year)


class Person(Vehicle):
    def __init__(self, v_name, v_model, v_year, p_name):
        Vehicle.__init__(self, v_name, v_model, v_year)
        self.p_name = p_name

    def display_person(self):
        print("Owner:", self.p_name)


person_vehicle = Person("Hyundai", "Creta", 2022, "Sonal")
person_vehicle.display()
person_vehicle.display_person()
