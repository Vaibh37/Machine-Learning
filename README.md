# machine learning

these are my notes while i learn machine learning with python

i use small data so i can see what the model does

the notebooks have code with short notes

the python folder has scripts i can run

the notes folder helps me revise

## what i have learned so far

### linear regression

[notebook](notebooks/01_linear_regression.ipynb) and [python practice](python/linear_regression.py)

predict a number and measure the error

### logistic regression

[notebook](notebooks/02_logistic_regression.ipynb) and [python practice](python/logistic_regression.py)

predict a class and read its estimated probability

### data preparation

[notebook](notebooks/03_preprocessing.ipynb) and [python practice](python/preprocessing_practice.py)

basic practice with StandardScaler and OneHotEncoder

### classification metrics

[notebook](notebooks/04_classification_metrics.ipynb) and [python practice](python/metrics_practice.py)

confusion matrix and the meaning of precision recall and F1

i need more code practice with F1 and classification report

### knn

[notebook](notebooks/05_knn.ipynb) and [python practice](python/knn_practice.py)

find close training points and use their classes to vote

### countvectorizer

[notebook](notebooks/06_count_vectorizer.ipynb) and [python practice](python/count_vectorizer_practice.py)

turn words into numbers by counting them

### naive bayes

[notebook](notebooks/07_naive_bayes.ipynb) and [python practice](python/naive_bayes_spam.py)

learn word patterns and predict spam or not spam

### decision tree

[notebook](notebooks/08_decision_tree.ipynb) and [python practice](python/decision_tree_practice.py)

learn questions that divide the training data

use gini to check how mixed a group is

use weighted gini to compare splits

learn why the tree can split between two values

check depth and the minimum number of samples for a split or a leaf

read the tree rules and feature importance

train on 50 practice students

test the model on data it did not use for learning

enter study hours and predict pass or fail

this example uses made up data

it is not a real exam prediction tool

## revision

[quick cheat sheet](notes/quick_cheatsheet.md)

[things i got confused about](notes/things_i_got_stuck_on.md)

[learning status](notes/learning_status.md)

## run this on my laptop

install the needed packages

```bash
python -m pip install -r requirements.txt
```

open the notebooks in VS Code with the Jupyter extension

or run the decision tree script

```bash
python python/decision_tree_practice.py
```

## next

learn entropy for decision trees

learn how to choose tree settings

learn cross validation

build a larger classification project

random forest and other models are still ahead

these are practice lessons and not production models
