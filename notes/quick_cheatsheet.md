# quick cheat sheet

short notes for revision

## common steps

make X and y

X contains features

y contains the correct answers

fit is for learning

predict is for a new guess

## linear regression

use it to predict a number

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
print(model.predict([[6]]))
```

mae is average absolute error

mse is average squared error

r2 tells me how much of the target change the model explains compared with a baseline

## logistic regression

use it to predict a class

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
print(model.predict([[9]]))
print(model.predict_proba([[9]]))
```

classes_ tells me which column belongs to which class

## train and test

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

train with train data

check with test data

## preprocessing

StandardScaler changes the scale of numeric features

OneHotEncoder makes columns from categories

fit preprocessing only on training data in a real train and test workflow

## classification metrics

confusion matrix compares real labels with predictions

precision asks how many predicted positives were correct

recall asks how many actual positives were found

f1 combines precision and recall

i still need more code practice with f1_score and classification_report

## knn

measure distance to the training points

sort from nearest to farthest

use the closest k points to vote

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print(model.predict([[3]]))
```

## naive bayes and text

CountVectorizer makes word count features

MultinomialNB learns class probabilities from those counts

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, y)

new_X = vectorizer.transform(["free gift"])
print(model.predict(new_X))
```

do not fit the vectorizer again on a new email

this is a small practice example

## decision tree

a tree learns questions that split the data

it tries to make groups with less class mixing

gini is 0 when a group has only one class

gini is 0 point 5 for two equal classes

weighted gini gives larger groups more weight

the tree can pick the midpoint between two values

max_depth limits how deep the tree can grow

min_samples_split sets the minimum samples needed before a node can split

min_samples_leaf sets the minimum samples needed in each final leaf

```python
from sklearn.tree import DecisionTreeClassifier, export_text

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

print(export_text(model, feature_names=["hours"]))
print(model.predict([[7]]))
print(model.feature_importances_)
```

feature importance shows which features helped reduce impurity

it is not a measure of accuracy

use model.score on train data and test data to compare accuracy

the model can fit training data well but still fail on new data

use two square brackets for one student with one feature
