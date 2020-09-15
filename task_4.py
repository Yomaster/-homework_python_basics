class Car:
    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print(f'{self.color} {self.name} поехал со скоростью {speed} км/ч')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        if direction == 'left':
            print('Автомобиль повернул налево')
        if direction == 'right':
            print('Автомобиль повернул направо')

    def show_speed(self):
        print('Скорость равна', self.speed, 'км/ч')


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print('Скорость равна', self.speed, 'км/ч')
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print('Скорость равна', self.speed, 'км/ч')


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print('Скорость равна', self.speed, 'км/ч')
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print('Скорость равна', self.speed, 'км/ч')


car1 = TownCar('Зеленый', 'Субару')
print(car1.color, car1.name, car1.speed, car1.is_police)
car1.go(61)
car1.show_speed()
car1.speed = 50
car1.show_speed()
car1.stop()
