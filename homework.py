class House:
    def __init__(self, number_of_floors=0):
        self.number_of_floors = number_of_floors

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print(self.number_of_floors)


floor = House()
floor.set_new_number_of_floors(10)
