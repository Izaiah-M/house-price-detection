import json
import pickle

__locations = None
___data_colums = None
___model = None

def get_locations():
    return __locations

def load_saved_artifacts(): 
    print("loading artifacts...")

    global ___locations
    global ___data_colums 

    with open("./artifacts/columns.json", "r") as f:
        ___data_colums = json.load(f)['data_columns']
        __locations = ___data_colums[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        ___model = pickle.load(f)

    print("loading artifacts is done...")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_locations())
    