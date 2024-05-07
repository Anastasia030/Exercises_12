import math


class GeometricObject:
    """
    A class that reads information from a file
    """
    __x = 0.0
    __y = 0.0
    color = 'black'
    filled = False

    def __init__(self, x=None, y=None, color=None, filled=None):
        """
        Initializes the basic parameters for each shape
        :param x: int or float, the x-axis coordinate
        :param y: int or float,the y-axis coordinate
        :param color: str, shape color
        :param filled: bool, is there a fill
        """
        self.color = GeometricObject.color
        self.filled = GeometricObject.filled
        if color is not None and isinstance(color, str):
            self.color = color
        if filled is not None and isinstance(filled, bool):
            self.filled = filled

        if x is not None:
            self.__x = x
        else:
            self.__x = 0.0

        if y is not None:
            self.__y = y
        else:
            self.__y = 0.0

    def set_coordinate(self, other_x, other_y):
        """
        Sets new valid coordinates
        :param other_x: int, the new coordinate on the x-axis
        :param other_y: int, the new coordinate on the y-axis
        """
        if isinstance(other_x, int) or isinstance(other_x, float):
            self.__x = other_x
        if isinstance(other_y, int) or isinstance(other_y, float):
            self.__y = other_y

    def set_color(self, other):
        """
        Sets the color of the shape
        :param other: str, new color
        """
        if isinstance(other, str):
            self.color = other

    def set_filled(self, other):
        """
        Establishes the existence of the fill
        :param other: bool, enabling or disabling the fill
        """
        if isinstance(other, bool):
            self.filled = other

    def get_x(self):
        """
        Allows to get a coordinate on the x-axis
        :return: int, the x-axis coordinate
        """
        return float(self.__x)

    def get_y(self):
        """
        Allows to get a coordinate on the y-axis
        :return: int, the y-axis coordinate
        """
        return float(self.__y)

    def get_color(self):
        """
        Allows to get the color coordinates
        :return: str, Allows you to get the color coordinates
        """
        return self.color

    def is_filled(self):
        """
        Allows know if the shape is filled in
        :return:
        """
        return self.filled

    def __str__(self):
        """
        String representation of information about a shape
        :return: str, in a readable format
        """
        return f'({float(self.__x)}, {float(self.__y)})\ncolor: {self.color}\nfilled: {self.filled}'

    def __repr__(self):
        """
        String representation of information about a shape
        :return: str
        """
        if self.filled is True:
            return f'({self.__x}, {self.__y}) {self.color} filled'
        else:
            return f'({self.__x}, {self.__y}) {self.color} no filled'


class Rectangle(GeometricObject):
    """
    The shape class is rectangular
    """
    width = 0.0
    height = 0.0

    def __init__(self, x=None, y=None, width=None, height=None, color=None, filled=None):
        """
        Initializes the shape parameters
        :param x: int or float, the x-axis coordinate
        :param y: int or float, the y-axis coordinate
        :param width: int or float, the width of the figure
        :param height: int or float, height of the figure
        :param color: str, shape color
        :param filled: bool, is there a fill
        """
        super().__init__(x, y, color, filled)

        self.width = Rectangle.width
        self.height = Rectangle.height
        if width is not None and 0 < width:
            self.width = width
        if height is not None and 0 < height:
            self.height = height

    def set_width(self, other):
        """
        Sets the width of the shape
        :param other: int, width of the shape
        """
        if (isinstance(other, int) or isinstance(other, float)) and 0 < other:
            self.width = other

    def set_height(self, other):
        """
        Sets the height of the shape
        :param other: int, height of the shape
        """
        if (isinstance(other, int) or isinstance(other, float)) and 0 < other:
            self.height = other

    def get_width(self):
        """
        Allows to get the width of the shape
        :return: int, the width of the shape
        """
        return float(self.width)

    def get_height(self):
        """
        Allows to get the height of the shape
        :return: int, the height of the shape
        """
        return float(self.height)

    def get_area(self):
        """
        Allows to get the square of the shape
        :return: int, the square of the shape
        """
        return float(self.width * self.height)

    def get_perimetr(self):
        """
        Allows to get the perimetr of the shape
        :return: int, the perimetr of the shape
        """
        return float(self.width * 2 + self.height * 2)

    def __str__(self):
        """
        String representation of rectangle information
        :return: str, in a readable format
        """
        return f'width: {self.width}\nheight: {self.height}\n({float(self.get_x())}, {float(self.get_y())})\n' \
               f'color: {self.color}\nfilled: {self.filled}'

    def __repr__(self):
        """
        String representation of rectangle information
        :return: str
        """
        if self.filled is True:
            return f'width: {self.width} height: {self.height} ({self.get_x()}, {self.get_y()}) {self.color} filled'
        else:
            return f'width: {self.width} height: {self.height} ({self.get_x()}, {self.get_y()}) {self.color} no filled'


class Circle(GeometricObject):
    """
    The class of the circle shape
    """
    _radius = 0.0

    def __init__(self, x=None, y=None, radius=None, color=None, filled=None):
        """
        Initializes the shape parameters
        :param x: int or float, the x-axis coordinate
        :param y: int or float,the y-axis coordinate
        :param radius: int or float, the radius of the circle
        :param color: str, shape color
        :param filled: bool, is there a fill
        """
        super().__init__(x, y, color, filled)

        self._radius = Circle._radius
        if (isinstance(radius, int) or isinstance(radius, float)) and 0 < radius:
            self._radius = radius

    @property
    def radius(self):
        """
        Allows to create managed attributes (features)
        :return: int or float, the value of the instance attribute
        """
        return self._radius

    @radius.setter
    def radius(self, other):
        """
        Sets the valid value of the instance attribute
        :param other: int or float, the radius of the circle
        """
        if (isinstance(other, int) or isinstance(other, float)) and 0 < other:
            self._radius = other

    @radius.getter
    def radius(self):
        """
        Sets the form in which the value of the instance attribute is returned
        :return: str, a string containing the date in the specified format
        """
        return float(self._radius)

    def get_area(self):
        """
        Allows to get the square of the shape
        :return: int, the square of the shape
        """
        return math.pi * self._radius ** 2

    def get_perimetr(self):
        """
        Allows to get the perimetr of the shape
        :return: int, the perimetr of the shape
        """
        return 2 * math.pi * self._radius

    def get_diametr(self):
        """
        Allows to get the diametr of the shape
        :return: int, the diametr of the shape
        """
        return float(self._radius * 2)

    def __str__(self):
        """
        String representation of rectangle information
        :return: str, in a readable format
        """
        return f'radius: {self._radius}\n({float(self.get_x())}, {float(self.get_y())})\ncolor: {self.color}\n' \
               f'filled: {self.filled}'

    def __repr__(self):
        """
        String representation of rectangle information
        :return: str
        """
        if self.filled is True:
            return f'radius: {self._radius} ({self.get_x()}, {self.get_y()}) {self.color} filled'
        else:
            return f'radius: {self._radius} ({self.get_x()}, {self.get_y()}) {self.color} no filled'
