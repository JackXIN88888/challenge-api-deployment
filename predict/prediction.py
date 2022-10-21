from array import array
import numpy
import joblib

# with open("immoElisa.pkl", "rb") as f:  # working for python and fastAPI
with open("predict/immoElisa.pkl", "rb") as f:  # working for render with dockerfile
    model = joblib.load(f)


def predict(X_predict: array):

    y_predict = model.predict(X_predict)[0][0]
    return y_predict


# x = predict([[2, 3, 100, 1]])
# print(x)
# print(type(x))
