from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = LogisticRegression()
model.fit(X_train, y_train)

print("test labels", y_test)
print("test guesses", model.predict(X_test))
print("accuracy", accuracy_score(y_test, model.predict(X_test)))
print("classes", model.classes_)
print("new guesses", model.predict([[9], [10]]))
print("probabilities", model.predict_proba([[9], [10]]))
