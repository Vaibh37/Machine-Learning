from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# one feature for each student
# 0 means fail
# 1 means pass

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

print("first tree")
print(export_text(model, feature_names=["hours"]))
print("new student", model.predict([[7]]))
print("tree depth", model.get_depth())

# gini measures how mixed the classes are
# this group has 3 of each class
p0 = 3 / 6
p1 = 3 / 6
gini = 1 - (p0 ** 2 + p1 ** 2)
print("gini before split", gini)
print("gini after pure split", 0)

# a larger group affects weighted gini more
left_gini = 1 - ((6 / 8) ** 2 + (2 / 8) ** 2)
right_gini = 1 - ((1 / 2) ** 2 + (1 / 2) ** 2)
weighted_gini = (8 / 10) * left_gini + (2 / 10) * right_gini
print("weighted gini", weighted_gini)

# a node needs enough samples to split
small_X = [[1], [2], [3]]
small_y = [0, 0, 1]
no_small_split = DecisionTreeClassifier(min_samples_split=5, random_state=42)
no_small_split.fit(small_X, small_y)
print("depth with large split limit", no_small_split.get_depth())

# a leaf must have at least 4 samples
# six samples cannot make two leaves of 4
no_split = DecisionTreeClassifier(min_samples_leaf=4, random_state=42)
no_split.fit(X, y)
print("depth with large leaf size", no_split.get_depth())
print("class scores in a tie", no_split.predict_proba([[7]]))
print("class chosen in a tie", no_split.predict([[7]]))

# the tree may need two splits
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 1, 1, 0, 0]
model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)
print("tree with two splits")
print(export_text(model, feature_names=["hours"]))
print("class for 4", model.predict([[4]]))
print("class for 5", model.predict([[5]]))

# a tree can use more than one feature
# the first value is hours
# the second value is attendance
X = [[1, 80], [2, 50], [3, 90], [4, 55], [5, 70], [6, 60]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)
print("tree with two features")
print(export_text(model, feature_names=["hours", "attendance"]))
print("feature importance", model.feature_importances_)
print("class for 5 hours and 40 attendance", model.predict([[5, 40]]))

# now use 50 students
# each row has hours and the result
data = [
    [1,0],
    [2,0],
    [3,0],
    [4,0],
    [5,0],
    [2,0],
    [3,0],
    [4,0],
    [5,1],
    [6,1],
    [1,0],
    [2,0],
    [3,0],
    [4,1],
    [5,0],
    [3,0],
    [4,0],
    [5,1],
    [6,1],
    [7,1],
    [2,0],
    [3,0],
    [4,0],
    [5,0],
    [6,1],
    [4,0],
    [5,1],
    [6,1],
    [7,1],
    [8,1],
    [3,0],
    [4,0],
    [5,0],
    [6,1],
    [7,1],
    [5,1],
    [6,1],
    [7,1],
    [8,1],
    [9,1],
    [4,0],
    [5,0],
    [6,1],
    [7,1],
    [8,1],
    [6,0],
    [7,1],
    [8,1],
    [9,1],
    [10,1]
]

X = [[row[0]] for row in data]
y = [row[1] for row in data]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

print("training samples", len(X_train))
print("testing samples", len(X_test))
print("training accuracy", model.score(X_train, y_train))
print("testing accuracy", model.score(X_test, y_test))
print("rules for 50 students")
print(export_text(model, feature_names=["hours"]))

# enter a new value
hours = float(input("Enter hours studied: "))
prediction = model.predict([[hours]])

print("class number", prediction[0])

if prediction[0] == 1:
    print("pass")
else:
    print("fail")

# this is only practice data
# it cannot tell whether a real student will pass
