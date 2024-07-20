class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def go_to(self, new_floor):
        if new_floor > self.floor:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floor}"

    def __eq__(self, other):
        return self.floor == other.floor

    def __lt__(self, other):
        return self.floor < other.floor

    def __gt__(self, other):
        return self.floor > other.floor

    def __ge__(self, other):
        return self.floor >= other.floor

    def __le__(self, other):
        return self.floor <= other.floor

    def __ne__(self, other):
        return self.floor != other.floor

    def __iadd__(self, value):
        self.floor += value
        return self

    def __add__(self, value):
        return House(self.name, self.floor + value)

    def __radd__(self, value):
        return House(self.name, self.floor + value)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
