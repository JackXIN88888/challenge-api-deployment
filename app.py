from fastapi import FastAPI, HTTPException
import uvicorn
from predict.prediction import predict
from preprocessing.cleaning_data import preprocessing
from pydantic import BaseModel

# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder

app = FastAPI()

# items = {"foo": "The foo W"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=444, detail="Item not found")
#     return {"item": items[item_id]}


class Data1(BaseModel):

    area: int | None = 0
    property_type: str
    rooms_number: int | None = 0
    zip_code: int | None = 0
    land_area: int | None = 0
    garden: bool | None = False
    garden_area: int | None = 0
    equipped_kitchen: bool | None = False
    full_address: str | None = False
    swimming_pool: bool | None = False
    furnished: bool | None = False
    open_fire: bool | None = False
    terrace: bool | None = False
    terrace_area: int | None = 0
    facades_number: int | None = 0
    building_state: str | None = 0


# x = predict([[2, 3, 100, 1]])
# print(x)
# print(type(x))


@app.get("/")
async def root():
    """Route that return 'Alive!' if the server runs."""
    return {"Status": "Alive!"}


@app.get("/predict")
async def showing():
    return "please send a json format house data"


@app.post("/predict", status_code=201)
async def predicting(data: Data1):
    print(data)
    print(type(data))
    data = data.dict()
    data = preprocessing(data)

    final_predict = predict(data)
    print(final_predict)
    return {"prediction": final_predict}

    # json_compatible_item_data = jsonable_encoder(data)
    # return JSONResponse(content=json_compatible_item_data)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
