import numpy
import pandas as pd
import json


with open("./challenge-api-deployment/input.json", "r") as file:
    data = json.load(file)
print(data)
print(data["data"])


def preprocessing(data):

    state_of_building = data["data"]["building-state"]
    bedrooms = data["data"]["rooms-number"]
    area = data["data"]["area"]
    swimming_pool = data["data"]["swimming-pool"]
    list1 = [state_of_building, bedrooms, area, swimming_pool]
    df = pd.DataFrame(list1)

    df = df.replace("HOUSE", 1)
    df = df.replace("APARTMENT", 0)
    df = df.replace("TO_RESTORE", 1)
    df = df.replace("TO REBUILD", 2)
    df = df.replace("TO_RENOVATE", 3)
    df = df.replace("JUST_RENOVATED", 4)
    df = df.replace("GOOD", 5)
    df = df.replace("AS_NEW", 6)
    df = df.replace(True, 1)
    df = df.replace(False, 0)

    df_no_Nan = df.dropna(axis=0, how="any")

    ndarray_immoElisa = df_no_Nan.values

    X_predict = ndarray_immoElisa.reshape(1, 4)
    print(X_predict)
    return X_predict


preprocessing(data)
