class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if any((new_floor < 1, new_floor > self.number_of_floors)):
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

"""
houses = []
houses.append(House('Ленина20', 5))
houses[0].go_to(6)
"""

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)