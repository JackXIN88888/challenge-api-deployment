from fastapi import FastAPI, HTTPException

app = FastAPI()

# items = {"foo": "The foo W"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=444, detail="Item not found")
#     return {"item": items[item_id]}


@app.get("/")
async def root():
    """Route that return 'Alive!' if the server runs."""
    return {"Status": "Alive!"}


@app.get("/predict")
async def s():
    pass


@app.post("/predict")
async def s():
    pass
