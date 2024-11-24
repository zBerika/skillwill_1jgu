import random
import string

# Функция для чтения заказов из текстового файла
def read_orders_from_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

class VINGenerator:
    @staticmethod
    def generate_vin():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))

class Qarxana:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return f"{self.name} - {self.location}"

class Engine:
    def __init__(self, engine_type, volume, h_p):
        self.engine_type = engine_type
        self.volume = volume
        self.h_p = h_p

    def display_info(self):
        return f"{self.engine_type}-{self.volume}L, {self.h_p} h.p."

class Car:
    def __init__(self, qarxana, color, model, year, engine: Engine, customer_info, car_type):
        self.qarxana = qarxana
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.customer_info = customer_info
        self.car_type = car_type
        self.vin = None

    def display_info(self):
        return f"{self.year} {self.color} {self.model}, Qarxana: {self.qarxana.display_info()}, Engine: {self.engine.display_info()}"

class Ford(Car):
    def __init__(self, qarxana, model, color, year, engine: Engine, customer_info, car_type):
        super().__init__(qarxana, model, color, year, engine, customer_info, car_type)

class Toyota(Ford):
    pass

class Nissan(Ford):
    pass

class Chevrolet(Ford):
    pass

class Honda(Ford):
    pass

def create_cars_from_orders(orders):
    cars = []
    vin_generator = VINGenerator()

    factories = {
        "Ford": Qarxana(name="Ford Factory", location="USA"),
        "Toyota": Qarxana(name="Toyota Factory", location="Japan"),
        "Nissan": Qarxana(name="Nissan Factory", location="Japan"),
        "Chevrolet": Qarxana(name="Chevrolet Factory", location="USA"),
        "Honda": Qarxana(name="Honda Factory", location="Japan")
    }

    for order in orders:
        parts = order.strip().split(', ')

        if len(parts) != 8:
            print(f"Неверный формат заказа: {order}")
            continue

        customer_info, order_number, model_info, color, car_type, engine_type, engine_volume, engine_hp = parts

        # Преобразуем объем и лошадиные силы в float
        engine_volume = float(engine_volume)
        engine_hp = float(engine_hp)

        engine = Engine(engine_type=engine_type, volume=engine_volume, h_p=engine_hp)

        brand = model_info.split()[0]

        qarxana = factories.get(brand, None)
        if not qarxana:
            print(f"Неизвестная марка: {brand}")
            continue

        # Создание объекта автомобиля в зависимости от марки
        if "Ford" in model_info:
            car = Ford(qarxana, model_info, color, 2023, engine, customer_info, car_type)
        elif "Honda" in model_info:
            car = Honda(qarxana, model_info, color, 2023, engine, customer_info, car_type)
        elif "Toyota" in model_info:
            car = Toyota(qarxana, model_info, color, 2023, engine, customer_info, car_type)
        elif "Chevrolet" in model_info:
            car = Chevrolet(qarxana, model_info, color, 2023, engine, customer_info, car_type)
        elif "Nissan" in model_info:
            car = Nissan(qarxana, model_info, color, 2023, engine, customer_info, car_type)
        else:
            print(f"Неизвестная марка: {model_info}")
            continue

        car.vin = vin_generator.generate_vin()
        cars.append(car)

    return cars


def print_purchase_info(car):
    print(f"VIN: {car.vin}, Клиент: {car.customer_info}, Модель: {car.model}, Цвет: {car.color}, "
          f"Тип кузова: {car.car_type}, Объем двигателя: {car.engine.volume}L, Лошадиные силы: {car.engine.h_p}HP")

if __name__ == "__main__":
    try:
        orders = read_orders_from_file('sia.txt')
        created_cars = create_cars_from_orders(orders)

        for car in created_cars:
            print_purchase_info(car)
    except FileNotFoundError:
        print("Файл 'sia.txt' не найден. Убедитесь, что он находится в той же директории, что и скрипт.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
