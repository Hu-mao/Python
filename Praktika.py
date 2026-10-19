#1----------------------------------
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_new(self):
        return self.year >= 2020


book1 = Book("К", "Тарас Сарат", 10)
book2 = Book("Вітер", "Стейсы Хтось", 2030)
book3 = Book("Одного разу", "Никита Орлик", 2010)

print(book1.is_new())
print(book2.is_new())
print(book3.is_new())
#2-----------------------------------------

class PositiveNumber:
    def __new__(cls, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Потрібно ціле число")

        if value < 0:
            print("Від'ємне число заборонено")
            return None

        return super().__new__(cls)

    def __init__(self, value):
        self.value = value


a = PositiveNumber(10)
b = PositiveNumber(-5)
с = PositiveNumber(-5.6)
print(a.value)
print(b)
print(с)