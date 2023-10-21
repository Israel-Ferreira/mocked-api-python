from utils.has_keys import dict_has_keys

class Car:

    def __init__(self, id, model, manufacturer, year, color):
        self.id = id
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.color = color



    @staticmethod
    def convert_dict_to_car_model(dct: dict):
        keys =  ["id", "model", "manufacturer", "color", "year"]

        if not dict_has_keys(dct, keys):
            raise RuntimeError()
        
        return Car(dct["id"], dct["model"], dct["manufacturer"], dct["year"], dct["color"])

        


    def to_json_dict(self):
        return  {
            "id": self.id, 
            "model": self.model,
            "manufacturer": self.manufacturer,
            "year": self.year,
            "color": self.color
        }