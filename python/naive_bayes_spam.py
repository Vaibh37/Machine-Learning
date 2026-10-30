from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "free prize now",
    "claim your free gift",
    "team meeting today",
    "project meeting tomorrow",
]

y = [1, 1, 0, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, y)

new_email = ["free gift"]
new_X = vectorizer.transform(new_email)

print("vocabulary", vectorizer.get_feature_names_out())
print("new word counts", new_X.toarray())
print("prediction", model.predict(new_X))
print("class order", model.classes_)
print("probabilities", model.predict_proba(new_X))

another_email = ["team meeting"]
another_X = vectorizer.transform(another_email)
print("team meeting", model.predict(another_X))
