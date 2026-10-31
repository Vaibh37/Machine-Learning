# things i got stuck on

## knn

i thought knn looks only left or only right

it does not

it measures distance to all training points

then it takes the closest k points

## countvectorizer

the numbers looked random at first

the words have fixed columns

the vocabulary is in alphabetical order by default

every message uses that same column order

each number is a word count

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

the outside list holds samples

the inside list holds features for one sample

## naive bayes probabilities

predict returns the selected class

predict_proba returns one estimated probability for each class

classes_ tells me the order

## decision tree gini

i mixed up group size and class purity

gini 0 means every sample in that group has one class

two groups do not need equal sample counts to be pure

gini 0 point 5 means two classes have equal shares

## decision tree split

the model chose hours instead of attendance

hours gave two pure groups in the small example

the split value was 3 point 5 because it was between 3 and 4

## feature importance

an importance score of 1 means a feature caused all the impurity reduction in that tree

it does not mean the model has perfect accuracy

attendance was not used in the small example

## leaf size

min_samples_leaf sets the minimum number in each leaf

a node with 6 samples cannot split into two leaves of at least 4 samples

the tree has depth 0 in that case

## one feature has two dimensions

this gives a one dimensional list

```python
X = [row[0] for row in data]
```

this gives the two dimensional data the model needs

```python
X = [[row[0]] for row in data]
```

## feature names

i gave two names to a model with one feature

export_text needs one name for each feature column

## accuracy check

the model does not have a method named accuracy_score

for a classifier i can use model.score on X and y

## predict output

predict returns an array

prediction at position 0 is the first result

the if statement only turns the class into a word

it does not make the model learn
