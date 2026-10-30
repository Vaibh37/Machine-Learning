from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = [[1], [2], [3], [4], [5]]
y = [100, 200, 300, 400, 500]

model = LinearRegression()
model.fit(X, y)

print("slope", model.coef_)
print("intercept", model.intercept_)
print("new value", model.predict([[6]]))

predicted = model.predict(X)
print("mae", mean_absolute_error(y, predicted))
print("mse", mean_squared_error(y, predicted))
print("r2", r2_score(y, predicted))
