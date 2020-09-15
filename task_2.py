class Road:
    weight = 5
    thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calculation(self):
        return self.__length * self.__width * self.weight * self.thickness


a = Road(40000, 20)
print(a.mass_calculation())
