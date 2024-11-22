class Qarxana:
    def __init__(self, name, location, distance_to_Georgia = 700):
        self.name = name
        self.location = location

    def display_info(self):
        return f"{self.name} - {self.location}"

class Engine:
    def __init__(self, volume, h_p):
        self.volume = volume
        self.h_p=h_p
    def display_info(self):
        return f"{self.volume}L, {self.h_p} h.p."

class Car(Qarxana):
    def __init__(self, qarxana, color, model, year, engine):
        super().__init__(qarxana.name, qarxana.location)
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color

    def display_info(self):
        engine_info = self.engine.display_info()
        return f"{self.year} {self.color} {self.model} with {engine_info}"

class Ford(Car):
    def __init__(self, qarxana, model, color, year, engine):
        super().__init__(qarxana, model, color, year, engine)

class Toyota(Car):
    def __init__(self, qarxana, model, color, year, engine):
        super().__init__(qarxana, model, color, year, engine)

class Nissan(Car):
    def __init__(self, qarxana, model, color, year, engine):
        super().__init__(qarxana, model, color, year, engine)

class Chevrole(Car):
    def __init__(self, qarxana, model, color, year, engine):
        super().__init__(qarxana, model, color, year, engine)

class Honda(Car):
    def __init__(self, qarxana, model, color, year, engine):
        super().__init__(qarxana, model, color, year, engine)

