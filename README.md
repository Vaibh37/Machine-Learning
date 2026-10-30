# machine learning

these are my notes while i learn machine learning with python

i use small data so i can see what the model does

the notebooks have code and short notes together
the python folder has the same kind of practice in normal scripts
the notes folder is for quick revision and mistakes i want to remember

## what i have learned so far

### linear regression

[notebook](notebooks/01_linear_regression.ipynb) and [python practice](python/linear_regression.py)

predict a number and check the error

### logistic regression

[notebook](notebooks/02_logistic_regression.ipynb) and [python practice](python/logistic_regression.py)

predict a class and read its estimated probability

### data preparation

[notebook](notebooks/03_preprocessing.ipynb) and [python practice](python/preprocessing_practice.py)

basic StandardScaler and OneHotEncoder practice

### classification metrics

[notebook](notebooks/04_classification_metrics.ipynb) and [python practice](python/metrics_practice.py)

confusion matrix and the meaning of precision recall and F1

i still need to practise the F1 function and classification report

### knn

[notebook](notebooks/05_knn.ipynb) and [python practice](python/knn_practice.py)

find the nearest training points then vote

### countvectorizer

[notebook](notebooks/06_count_vectorizer.ipynb) and [python practice](python/count_vectorizer_practice.py)

turn words into numbers by counting them

### naive bayes

[notebook](notebooks/07_naive_bayes.ipynb) and [python practice](python/naive_bayes_spam.py)

learn from labelled text and predict spam or not spam

## revision

[quick cheat sheet](notes/quick_cheatsheet.md)

[things i got confused about](notes/things_i_got_stuck_on.md)

[learning status](notes/learning_status.md)

## run this on my laptop

install packages from requirements.txt

```bash
python -m pip install -r requirements.txt
```

open the notebooks in VS Code with the Jupyter extension

or run a script

```bash
python python/naive_bayes_spam.py
```

## next

practise f1_score and classification_report

then start decision trees

i have not marked decision trees random forests svm or k means as completed

these are small learning examples and not real production models
