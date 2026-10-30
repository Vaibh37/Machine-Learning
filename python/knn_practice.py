from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [4], [8]]
y = [0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("prediction for 3", model.predict([[3]]))
print("prediction for 7", model.predict([[7]]))

point = 3
distances = [(x[0], abs(x[0] - point)) for x in X]
distances = sorted(distances, key=lambda pair: pair[1])

print("sorted point and distance", distances)
print("nearest three", distances[:3])
