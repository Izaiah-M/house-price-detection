import json
import pickle
import numpy as np

__locations = None
__data_colums = None
__model = None

# A function to return the price prediction based on the inputs
def get_estimated_price(location: str, sqft: int, bhk: int, bath: int):
    # Because we saved our model, it has the predict method, which takes in the input that it expects
    # Which in reality will be our Xvalues
    # Input needs to be a 2D array
    try:
        loc_index = __data_colums.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_colums)) # we need to have a np arr with all zeros
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)

# Function to return the locations
def get_locations():
    return __locations

# Function to load our model, locations and data columns
def load_saved_artifacts(): 
    # print("loading artifacts...")

    global __locations
    global __data_colums 

    with open("C:/Users/HP/OneDrive/Desktop/HousePricePrediction/server/artifacts/columns.json", "r") as f:
        __data_colums = json.load(f)['data_columns']
        __locations = __data_colums[3:]

    global __model 
    with open("C:/Users/HP/OneDrive/Desktop/HousePricePrediction/server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

# if __name__ == "__main__":
#     load_saved_artifacts()
#     print(get_estimated_price("1st Phase JP Nagar", 12333, 3, 3))
#     print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 3))
