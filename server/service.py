import json
import pickle

__locations = None
__data_colums = None
__model = None

def get_locations():
    return __locations

def load_saved_artifacts(): 
    # print("loading artifacts...")

    global __locations
    global __data_colums 

    with open("C:/Users/HP/OneDrive/Desktop/HousePricePrediction/server/artifacts/columns.json", "r") as f:
        __data_colums = json.load(f)['data_columns']
        __locations = __data_colums[3:]

    with open("C:/Users/HP/OneDrive/Desktop/HousePricePrediction/server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    # print("loading artifacts is done...")
