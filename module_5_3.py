class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def eq(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __eq__(self, other):
        return self.eq(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def add(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __add__(self, value):
        return self.add(value)

    def __radd__(self, value):
        return self.add(value)

    def __iadd__(self, value):
        return self.add(value)

# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # False

h1 = h1 + 10  # добавление 10 этажей
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # добавление еще 10 этажей
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # увеличиваем этажи в h2
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False
