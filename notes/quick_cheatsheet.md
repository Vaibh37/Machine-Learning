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

train with train data and check with test data

## preprocessing

StandardScaler changes the scale of numeric features

OneHotEncoder makes columns from categories

fit preprocessing only on training data in a real train and test workflow

## classification metrics

confusion matrix compares real labels with predictions

precision asks how many predicted positives were correct

recall asks how many actual positives were found

f1 combines precision and recall

we have not practiced f1_score or classification_report yet

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

this is a small toy example so do not trust it on real mail
