from array import array
import numpy
import joblib


def predict(X_predict: array):

    with open("/home/jack/challenge-api-deployment/model/immoElisa.pkl", "rb") as f:
        model = joblib.load(f)

    y_predict = model.predict(X_predict)
    y_predict = y_predict[0]
    y_predict = y_predict[0]
    return y_predict


x = predict([[2, 3, 100, 1]])
print(x)
print(type(x))
