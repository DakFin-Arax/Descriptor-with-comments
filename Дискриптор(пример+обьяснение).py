"""Дескриптор (descriptor)
Дискрипторы данных (`data descriptor`) и
дискрипторы не данных (`non-data descriptor`). """


class Integer:
    """Дискриптор для координат класса Point"""
    def __set_name__(self, owner, name):
        """
        Назначает имя свойство ЭК класса Integer
        :param owner: ссылка на класс Point
        :param name: локальное свойство в ЭК класса Integer
        :return: возвращает имя локального свойства '_х '
        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        """
        self - ссылка на ЭК класса Integer
        :param instance: ссылка на ЭК класса Point (из которого он вызывается a, b, c)
        :param owner: ссылка на класс Point
        :return: значение атрибута ЭК Point
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        :param instance: ссылка на ЭК класса Point (из которого он вызывается a, b, c)
        :param value: числовое значение которое мы присваиваем
        """
        instance.__dict__[self.name] = value


class Point:
    """Класс где используеться дискриптор"""
    x = Integer()  # дискриптор координаты x
    y = Integer()  # дискриптор координаты y
    z = Integer()  # дискриптор координаты z

    def __init__(self, x, y, z):
        """Тут идет обращение x, y, z - дискрипторам класса Point. И создаються локальные свойства ЭК (_x, _y, _z)
        это происходит в момент присваивания числового значения путём срабытывания метода __set__ из класса Integer"""
        self.x = x
        self.y = y
        self.z = z

a = Point(4, 5, 6)
b = Point(3, 4, 5)
c = Point(7, 8, 9)



print(a.__dict__, b.__dict__, c.__dict__, sep='\n')

