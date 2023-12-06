import tkinter as tk

# Класс 2D движка
class Engine2D:
    def __init__(self, width=800, height=600, color='black'):
        self.width = width              # Ширина окна
        self.height = height            # Высота окна
        self.figure_list = []           # Список примитивов
        self.current_color = color      # Текущий цвет отрисовки
    
    # Метод добалвения примитивов в список
    def add_figure(self, figure):
        if type(figure) is Circle or type(figure) is Triangle or type(figure) is Rectangle:
            self.figure_list.append((figure, self.current_color))
        else:
            print('Error: added figure is not Circle or Triangle or Rectangle class')

    # Метод отрисовки всех примитивов из списка
    def draw(self):
        app = tk.Tk()                                                  # Основное окно приложения движка
        app.title('Engine2D {}x{}'.format(self.width, self.height))    # Заоголовок окна приложения
        
        # Холст для отрисовки примитивов
        canvas = tk.Canvas(app, width=self.width, height=self.height)
        canvas.pack()

        for figure in self.figure_list:
            figure[0].draw(canvas, figure[1])
        self.figure_list = []

        app.mainloop()

    # Метод изменения цвета отрисовки
    def change_color(self, color='black'):
        self.current_color = color

# Класс примитива: Круг
class Circle:
    def __init__(self, x, y, radius):
        self.x = x              # Координата начальной точки по x
        self.y = y              # Координата начальной точки по y
        self.radius = radius    # Радиус круга

    # Метод отрисовки примитива
    def draw(self, canvas, color):
        canvas.create_oval(self.x, self.y, self.x+self.radius*2, self.y+self.radius*2, fill=color, outline=color)
        print('Drawing Circle:({}, {}) with radius {} and color {}'.format(self.x, self.y, self.radius, color))

# Класс примитива: Треугольник
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1    # Координата 1-ой точки по x
        self.y1 = y1    # Координата 1-ой точки по y
        self.x2 = x2    # Координата 2-ой точки по x
        self.y2 = y2    # Координата 2-ой точки по y
        self.x3 = x3    # Координата 3-ой точки по x
        self.y3 = y3    # Координата 3-ой точки по y

    # Метод отрисовки примитива
    def draw(self, canvas, color):
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill=color, outline=color)
        print('Drawing Triangle:({}, {}) ({}, {}) ({}, {}) and color {}'.format(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, color))

# Класс примитива: Прямоугольник
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x              # Координата начальной точки по x
        self.y = y              # Координата начальной точки по y
        self.width = width      # Ширина прямоугольника
        self.height = height    # Высота прямоугольника

    # Метод отрисовки примитива
    def draw(self, canvas, color):
        canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill=color, outline=color)
        print('Drawing Rectangle:({}, {}) with width {} height {} and color {}'.format(self.x, self.y, self.width, self.height, color))

# Функция для тестирования добавления примитива
def test_add_figure():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    assert len(engine_2D.figure_list) == 1

# Функция для проверки примитива на Круг
def test_add_figure_is_Cirle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    assert type(engine_2D.figure_list[0][0]) is Circle

# Функция для проверки примитива на Треугольник
def test_add_figure_is_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert type(engine_2D.figure_list[0][0]) is Triangle

# Функция для проверки примитива на Прямоугольник
def test_add_figure_is_Rectangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Rectangle(10,10,100,100))
    assert type(engine_2D.figure_list[0][0]) is Rectangle

# Функция для проверки изменения цвета отрисовки
def test_change_color():
    engine_2D = Engine2D()
    engine_2D.change_color('red')
    assert engine_2D.current_color == 'red'

# Функция для проверки изменения цвета отрисовки для примитива
def test_change_color_for_figure():
    engine_2D = Engine2D()
    engine_2D.change_color('red')
    engine_2D.add_figure(Circle(10,10,100))
    assert engine_2D.figure_list[0][1] == 'red'

# Функция для проверки отрисовки и очистки списка примитивов
def test_draw():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    engine_2D.draw()
    assert engine_2D.figure_list == []

# Функции для проверки параметров примитива: Круг
def test_coordinates_x_of_Circle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    assert engine_2D.figure_list[0][0].x == 10

def test_coordinates_y_of_Circle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    assert engine_2D.figure_list[0][0].y == 10

def test_radius_of_Circle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Circle(10,10,100))
    assert engine_2D.figure_list[0][0].radius == 100

# Функции для проверки параметров примитива: Треугольник
def test_coordinates_x1_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].x1 == 10

def test_coordinates_y1_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].y1 == 10

def test_coordinates_x2_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].x2 == 60

def test_coordinates_y2_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].y2 == 60

def test_coordinates_x3_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].x3 == 10

def test_coordinates_y3_of_Triangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Triangle(10,10,60,60,10,60))
    assert engine_2D.figure_list[0][0].y3 == 60

# Функции для проверки параметров примитива: Прямоугольник
def test_coordinates_x_of_Rectangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Rectangle(10,10,100,100))
    assert engine_2D.figure_list[0][0].x == 10

def test_coordinates_y_of_Rectangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Rectangle(10,10,100,100))
    assert engine_2D.figure_list[0][0].y == 10

def test_width_of_Rectangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Rectangle(10,10,100,100))
    assert engine_2D.figure_list[0][0].width == 100

def test_height_of_Rectangle():
    engine_2D = Engine2D()
    engine_2D.add_figure(Rectangle(10,10,100,100))
    assert engine_2D.figure_list[0][0].height == 100