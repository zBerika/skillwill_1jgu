import random  # Импортируем модуль random для генерации случайных значений
import time
import os

# Списки данных
car_models = ["Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Malibu", "Nissan Altima"]
body_types = ["sedan", "coupe", "hatchback", "SUV", "wagon"]
colors = ["blue", "black", "red", "white", "gray"]
car_stores = ["Tbilisi", "Batumi"]

# Список клиентов
clients_names = [
    {"id": 1, "name": "Giorgi"},  {"id": 2, "name": "Nino"},    {"id": 3, "name": "Levan"},
    {"id": 4, "name": "Tamara"},  {"id": 5, "name": "Irakli"},  {"id": 6, "name": "Mariam"},
    {"id": 7, "name": "David"},   {"id": 8, "name": "Anna"},    {"id": 9, "name": "Zurab"},
    {"id": 10, "name": "Keti"},    {"id": 11, "name": "Sandro"}, {"id": 12, "name": "Eka"},
    {"id": 13, "name": "Vano"},   {"id": 14, "name": "Teimuraz"},{"id": 15, "name": "Marina"}
]

# Класс для клиента
class Client:
    def __init__(self, id, name):
        self.id = id  # Инициализация идентификатора клиента
        self.name = name  # Инициализация имени клиента

    @staticmethod
    def random_client(client_data):
        # Выбор случайного клиента из списка
        return Client(client_data["id"], client_data["name"])

# Метод для вывода информации о покупке
def print_purchase_info(client, car_model, car_color, car_body_type, store):
    delay = random.uniform(0.1, 2)
    time.sleep(delay)
    output = f'{client.name} - {client.id}, {car_model}, {car_color}, {car_body_type}, {store}\n'
    file.write(output)
    print(f'{client.name} - {client.id}, daazakaza {car_model}, peri {car_color}, kuzao {car_body_type} - galaqi {store}')

if __name__ == "__main__":
    with open('sia.py', 'w', encoding='utf-8') as file:
        # Генерируем информацию о покупке для 10 клиентов
        random_clients = random.sample(clients_names, 10)  # Случайный выбор 10 клиентов
        for client_data in random_clients:
            client = Client.random_client(client_data)  # Генерация клиента
            car_model = random.choice(car_models)  # Выбор случайной модели автомобиля
            car_color = random.choice(colors)  # Выбор случайного цвета
            car_body_type = random.choice(body_types)  # Выбор случайного типа кузова
            store_location = random.choice(car_stores)  # Выбор случайного магазина

            # Вывод информации о покупке
            print_purchase_info(client, car_model, car_color, car_body_type, store_location)

os.system('python ganawileba.py')