import time


class TrafficLight:
    def __init__(self, color1, color2, color3):
        self.__color = {color1: 7, color2: 2, color3: 4}

    def running(self):
        if list(self.__color.keys()) != ['красный', 'желтый', 'зеленый']:
            raise ValueError('Неверный порядок цветов!')
        while True:
            for color, t in self.__color.items():
                print(color)
                time.sleep(t)


a = TrafficLight('красный', 'желтый', 'зеленый')
a.running()
