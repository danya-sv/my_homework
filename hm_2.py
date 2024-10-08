class Figure:
    unit = 'cm'

    def calculate_area(self):
        pass
    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        return f'Square side Length: {self.__side_length}{self.unit}, Area: {self.calculate_area()}{self.unit}'


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__wight = width

    def calculate_area(self):
        return self.__length * self.__wight

    def info(self):
        return f'Rectangle Length: {self.__length}{self.unit}, Wight: {self.__wight}{self.unit}, Area: {self.calculate_area()}{self.unit}'

figures = [
    Square(5),
    Square(4),
    Rectangle(5, 4),
    Rectangle(3, 3),
    Rectangle(10, 4)
]
for figure in figures:
    print(figure.info())


