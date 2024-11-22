import random  
import time
import os


car_models = ["Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Malibu", "Nissan Altima"]
body_types = ["sedan", "coupe", "hatchback", "SUV", "wagon"]
colors = ["blue", "black", "red", "white", "gray"]
car_stores = ["Tbilisi", "Batumi"]


clients_names = [
    {"id": 1, "name": "Giorgi"},  {"id": 2, "name": "Nino"},    {"id": 3, "name": "Levan"},
    {"id": 4, "name": "Tamara"},  {"id": 5, "name": "Irakli"},  {"id": 6, "name": "Mariam"},
    {"id": 7, "name": "David"},   {"id": 8, "name": "Anna"},    {"id": 9, "name": "Zurab"},
    {"id": 10, "name": "Keti"},    {"id": 11, "name": "Sandro"}, {"id": 12, "name": "Eka"},
    {"id": 13, "name": "Vano"},   {"id": 14, "name": "Teimuraz"},{"id": 15, "name": "Marina"}
]


class Client:
    def __init__(self, id, name):
        self.id = id  
        self.name = name  

    @staticmethod
    def random_client(client_data):
        
        return Client(client_data["id"], client_data["name"])


def print_purchase_info(client, car_model, car_color, car_body_type, store):
    delay = random.uniform(0.1, 2)
    time.sleep(delay)
    output = f'{client.name} - {client.id}, {car_model}, {car_color}, {car_body_type}, {store}\n'
    file.write(output)
    print(f'{client.name} - {client.id}, daazakaza {car_model}, peri {car_color}, kuzao {car_body_type} - galaqi {store}')

if __name__ == "__main__":
    with open('sia.py', 'w', encoding='utf-8') as file:
       
        random_clients = random.sample(clients_names, 10)  
        for client_data in random_clients:
            client = Client.random_client(client_data)  
            car_model = random.choice(car_models)  
            car_color = random.choice(colors)  
            car_body_type = random.choice(body_types)  
            store_location = random.choice(car_stores)  

           
            print_purchase_info(client, car_model, car_color, car_body_type, store_location)

os.system('python ganawileba.py')
