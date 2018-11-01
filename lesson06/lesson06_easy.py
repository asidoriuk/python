import math

__author__: str = 'Алексей Сидорюк'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    # Длины сторон треугольника
    def __init__(self, tops):
        self.a = math.sqrt((tops[0][0] - tops[1][0])**2 + (tops[0][1] - tops[1][1])**2)
        self.b = math.sqrt((tops[1][0] - tops[2][0])**2 + (tops[1][1] - tops[2][1])**2)
        self.c = math.sqrt((tops[0][0] - tops[2][0])**2 + (tops[0][1] - tops[2][1])**2)

    def square(self):
        return math.sqrt((self.a + self.b + self.c)*(self.b + self.c - self.a)*(self.a + self.c - self.b)*(self.a + self.b - self.c))/4

    def perimeter(self):
        return self.a + self.b + self.c

    # Высота из противолежащей вершины к стороне (задается)
    def height(self, side):
        if side == 'a':
            return 2*self.square()/self.a
        elif side == 'b':
            return 2*self.square()/self.b
        elif side == 'c':
            return 2*self.square()/self.c
        else:
            return 'Сторона треугольника указана неправильно.'


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium(Triangle):
    def __init__(self, tops):
        # Длины сторон трапеции в общем-то не нужны, достаточно диагоналей
        self.diag1 = math.sqrt((tops[0][0] - tops[2][0]) ** 2 + (tops[0][1] - tops[2][1]) ** 2)
        self.diag2 = math.sqrt((tops[1][0] - tops[3][0]) ** 2 + (tops[1][1] - tops[3][1]) ** 2)

        if self.diag1 != self.diag2:
            print('Это не равнобедренная трапеция')

        self.tr1 = Triangle(tops[:3])
        self.tr2 = Triangle(tops[:1] + tops[2:])

    @property
    def square(self):
        return self.tr1.square() + self.tr2.square()

    @property
    def perimeter(self):
        return self.tr1.perimeter() + self.tr2.perimeter() - self.diag1*2


if __name__ == '__main__':

    triangle1 = Triangle(((0, 3), (4, 0), (0, 0)))
    print(triangle1.a, triangle1.b, triangle1.c, triangle1.square(), triangle1.perimeter(), triangle1.height('d'))

    trapezium1 = Trapezium(((0, 0), (3, 4), (4, 4), (7, 0)))
    print(trapezium1.diag1, trapezium1.perimeter, trapezium1.square)
