from sklearn.feature_extraction.text import CountVectorizer

messages = [
    "python is fun",
    "python is powerful",
    "machine learning is fun",
]

messages.append("python python learning")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

print("vocabulary", vectorizer.get_feature_names_out())
print("training matrix")
print(X.toarray())

new_message = ["python is python"]
new_X = vectorizer.transform(new_message)

print("new row")
print(new_X.toarray())
