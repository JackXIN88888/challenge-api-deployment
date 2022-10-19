import pandas as pd

# from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

# import seaborn as sns

df = pd.read_csv("all_data_cleaned.csv")

df = df.replace("HOUSE", 1)
df = df.replace("APARTMENT", 0)
df = df.replace("TO_RESTORE", 1)
df = df.replace("TO_BE_DONE_UP", 2)
df = df.replace("TO_RENOVATE", 3)
df = df.replace("JUST_RENOVATED", 4)
df = df.replace("GOOD", 5)
df = df.replace("AS_NEW", 6)
df["state"].value_counts()


# plt.figure(figsize=(15, 8))
# sns.set_theme(style="white")
# corr = df.corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".1g")


df = df.drop(["garden_area"], axis=1)
df = df.drop(["terrace_area"], axis=1)
df = df.drop(["land_area"], axis=1)


df = df.dropna(subset=["price"])
df = df.dropna(subset=["habitable_surface"])

z_scores_price = stats.zscore(df["price"])
z_scores_hab_surf = stats.zscore(df["habitable_surface"])


abs_z_scores_price = np.abs(z_scores_price)
abs_z_scores_hab_surf = np.abs(z_scores_hab_surf)

filtered_entries_price = abs_z_scores_price < 2
filtered_entries_hab_surf = abs_z_scores_hab_surf < 2


temp_df = df[filtered_entries_price]
df = temp_df[filtered_entries_hab_surf]


df_no_Nan = df.dropna(axis=0, how="any")
# print(df)

# df_house = df_no_Nan.replace("HOUSE", 1)

ndarray_immoElisa = df_no_Nan.values
# ndarray_immoElisa.dropna(axis=0,how='any')
print(ndarray_immoElisa[1])

x_ndarray_immoElisa = ndarray_immoElisa[:, [7, 9, 10, 17]]
# state of building, bedrooms, area, swimming pool
y_ndarray_immoElisa = ndarray_immoElisa[:, 5]
print(x_ndarray_immoElisa)
print(y_ndarray_immoElisa)
print(len(df))
print(len(df_no_Nan))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x_ndarray_immoElisa, y_ndarray_immoElisa, test_size=0.2
)

print(x_train)
print(y_train)

from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import math

score_list = []
score1_list = []
r2_list = []
price_error_list = []
price_error_list_train = []

reg = linear_model.LinearRegression()
reg.fit(x_train, y_train.reshape(-1, 1))

score = reg.score(x_train, y_train.reshape(-1, 1))
print(score)


y_predict_train = reg.predict(x_train)
price_error_train_sqr = mean_squared_error(y_train, y_predict_train)
price_error_train = math.sqrt(price_error_train_sqr)
print(price_error_train)

y_predict = reg.predict(x_test)
price_error_sqr = mean_squared_error(y_test, y_predict)
price_error = math.sqrt(price_error_sqr)
print(price_error)

score1 = reg.score(x_test, y_test.reshape(-1, 1))
print(score)

score1_list.append(score)
score_list.append(score)
price_error_list.append(price_error)
price_error_list_train.append(price_error_train)
r2 = r2_score(y_test, y_predict)
r2_list.append(r2)

print(r2)

from cmath import exp
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import math


for i in range(4):
    degree = i + 2

    polyreg = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression(),
    )

    polyreg.fit(x_train, y_train.reshape(-1, 1))

    score = polyreg.score(x_train, y_train.reshape(-1, 1))
    print(score)

    y_predict_train = polyreg.predict(x_train)
    price_error_train_sqr = mean_squared_error(y_train, y_predict_train)
    price_error_train = math.sqrt(price_error_train_sqr)
    print(price_error_train)

    y_predict = polyreg.predict(x_test)
    price_error_sqr = mean_squared_error(y_test, y_predict)
    price_error = math.sqrt(price_error_sqr)
    print(price_error)

    score1 = reg.score(x_test, y_test.reshape(-1, 1))
    print(score)

    score1_list.append(score)

    score_list.append(score)
    price_error_list.append(price_error)
    price_error_list_train.append(price_error_train)
    r2 = r2_score(y_test, y_predict)
    r2_list.append(r2)
    print(r2)

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mticker

# plt.title("Polynominal Error show")
# plt.ylabel("Price_error (sqr(MSE))")
# plt.xlabel("degree")
# plt.yscale("log")
# plt.plot(
#     [1, 2, 3, 4, 5],
#     price_error_list,
#     label="price error for test set",
#     marker="o",
#     markersize=10,
# )
# plt.plot(
#     [1, 2, 3, 4, 5],
#     price_error_list_train,
#     label="price error for train set",
#     marker="x",
#     markersize=8,
# )
# plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
# print(price_error_list)
# print(price_error_list_train)
# print(score_list)
# print(r2_list)
# print(score1_list)
# plt.legend()
# plt.grid()
# plt.show()

import joblib

filename_model = "/home/jack/challenge-api-deployment/model/immoElisa.pkl"
joblib.dump(polyreg, filename_model)
