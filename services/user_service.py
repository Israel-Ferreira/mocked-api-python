from utils.has_keys import load_json_content

from models.car import Car


def get_all_data_from_jsonf():
    cars_data =  load_json_content("cars.json")

    try:
        return [Car.convert_dict_to_car_model(car_dct) for car_dct in cars_data]
    except RuntimeError as _:
        return []
    
