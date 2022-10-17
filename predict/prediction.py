import numpy
import joblib


def predict(X_predict):

    with open("/home/jack/challenge-api-deployment/model/immoElisa.pkl", "rb") as f:
        model = joblib.load(f)

    y_predict = model.predict(X_predict)
    return y_predict
