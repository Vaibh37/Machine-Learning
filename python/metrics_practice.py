from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)

y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 0, 1, 1, 1]

print("accuracy", accuracy_score(y_true, y_pred))
print("confusion matrix")
print(confusion_matrix(y_true, y_pred))
print("precision", precision_score(y_true, y_pred))
print("recall", recall_score(y_true, y_pred))
