# Дорога - хранит расстояния между объектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс Машина
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#     емкость кузова, скорость движения, расход топлива за час поездки
# может
#     стоять под погрузкой-разгрузкой
#     ехать со скоростью по дороге
#
# Погрузчик (производный от Машина)
# имеет
#     скорость погрузки, расход топлива в час при работе
# может
#     загружать-разгружать грузовик
#     ждать грузовик

from termcolor import cprint


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return 'Склад {}, объем хранения = {} кг'.format(self.name, self.content)

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        truck.location = self
        print('Грузовик {} прибыл в {}'.format(truck, self.name))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('Грузовик {} готов выезжать из {}'.format(truck, self.name))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{}, топливо = {} л'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        print('{} заправился'.format(self.model))


class Truck(Vehicle):
    fuel_rate = 50

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.location = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + ', груз = {} кг'.format(self.cargo)

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось {} км'.format(self.model, self.distance_to_target))
        else:
            self.location.end.truck_arrived(self)
            print('{} прибыл в {}'.format(self.model, self.location.name))

    def go_to(self, road):
        self.location = road
        self.distance_to_target = road.distance
        print('{} выехал в сторону {}'.format(self.model, self.location.end.name))

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif isinstance(self.location, Road):
            self.ride()


class AutoLoader(Vehicle):
    fuel_rate = 30

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + ', грузит {}'.format(self.truck)

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif self.truck is None:
            self.truck = self.warehouse.get_next_truck()
            print('{} начал работать с {}'.format(self.model, self.truck))
        elif self.role == 'loader':
            self.load()
        else:
            self.unload()

    def load(self):
        self.fuel -= self.fuel_rate
        truck_to_load = self.truck.body_space - self.truck.cargo
        if truck_to_load >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_to_load
            self.truck.cargo += truck_to_load
        print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.truck.cargo
            self.warehouse.content += self.truck.cargo
        print('{} разгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Санкт-Петербург', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

truck_1 = Truck(model='КАМАЗ', body_space=5000)
truck_2 = Truck(model='ГАЗ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    print()
    cprint('---------- Час {} ----------'.format(hour), color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    print()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='green')
    cprint(loader_2, color='green')
    cprint(moscow, color='yellow')
    cprint(piter, color='yellow')
