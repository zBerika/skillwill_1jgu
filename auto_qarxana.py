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
        self.h_p=h_p
    def display_info(self):
        return f"{self.engine_type}-{self.volume}L, {self.h_p} h.p."

class Car():
    def __init__(self, qarxana, color, model, year, engine: Engine):
        self.qarxana  = qarxana
        self.model = model
        self.year = year
        self.color = color
        self.engine=engine

    def display_info(self):
        return f"{self.year} {self.color} {self.model}, Qawxana: {self.qarxana.display_info()}, Dzravi: {self.engine.display_info()}"

class Ford(Car):
    def __init__(self, qarxana, model, color, year,engine):
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

