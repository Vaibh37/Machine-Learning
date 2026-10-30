from sklearn.preprocessing import OneHotEncoder, StandardScaler

numbers = [[10, 100], [20, 200], [30, 300]]

scaler = StandardScaler()
print("scaled numbers")
print(scaler.fit_transform(numbers))

colors = [["red"], ["blue"], ["red"], ["green"]]

encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(colors)

print("columns", encoder.get_feature_names_out())
print(encoded)

print("new colors")
print(encoder.transform([["green"]]))
