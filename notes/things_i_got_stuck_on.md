# things i got stuck on

## knn

i was thinking that knn looks only left or only right

no

it measures the distance to all training points

then it takes the closest k points

in a one number example the distance from 3 to 8 is 5

## countvectorizer

the numbers looked random at first

the words have fixed columns

the vocabulary is in alphabetical order by default

every message uses that same column order

the number in a cell is the count of that word

## fit and transform

fit learns from training data

transform uses what was learned to change data

fit_transform does both jobs for the training text

for a new email i use only transform

## new email variable error

this caused a NameError

```python
new_X = vectorizer.transform(new_X)
```

new_X did not exist yet

this is the correct line

```python
new_X = vectorizer.transform(new_email)
```

## double square brackets

```python
model.predict([[3]])
```

outer brackets hold samples

inner brackets hold the features for one sample

## naive bayes probabilities

predict returns the selected class

predict_proba returns one estimated probability for each class

classes_ tells me the order

i can use the model without doing Laplace smoothing maths by hand

later i can study why the maths works
