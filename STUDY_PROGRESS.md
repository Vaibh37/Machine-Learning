# Learning Progress

Last reviewed: **15 October 2026**. Progress levels here describe the study session, not job-readiness or model-training capability.

## Practiced

| Topic | Evidence | Source |
|---|---|---|
| NumPy basics | 2D arrays, indexing, broadcasting and shapes | [Python/NumPy cheat sheet](https://github.com/Vaibh37/Python-cheat_sheet/blob/main/NUMPY_CHEATSHEET.md) |
| Vectors | Dot products, magnitude, unit vectors, angles | [Math vector lessons](https://github.com/Vaibh37/ML-MATH/tree/main/linear-algebra/vectors) |
| Matrix arithmetic | Addition, subtraction, scaling, multiplication, transpose | [Matrix lessons](https://github.com/Vaibh37/ML-MATH/tree/main/linear-algebra/matrices) |
| Matrix and vector dimensions | Inner dimensions match; output shapes | [Matrix cheatsheet](https://github.com/Vaibh37/ML-MATH/blob/main/linear-algebra/matrices/00-formula-cheatsheet.md) |
| Hidden-layer forward pass | 2-neuron and 3-neuron worked examples; A = ReLU(Wx+b) | [Neural-Network forward pass](https://github.com/Vaibh37/Neural-Network/blob/main/notes/04-hidden-layer-forward-pass.md) |
| ReLU and sigmoid | Meaning, numeric behavior, basic use | [Activation notes](https://github.com/Vaibh37/Neural-Network/blob/main/notes/03-activation-functions.md) |

## Introduced

- Squared-error loss and the general goal of minimizing loss.
- Training as repeated forward pass → loss → parameter update, without implementing those updates yet.

## Upcoming lessons (not completed)

1. Trainable parameters, model predictions and scalar loss functions.
2. Linear regression with a small dataset and a real parameter update.
3. Derivatives, gradients, and gradient descent in the context of training.
4. Backpropagation and a first small **trained** neural network.
5. scikit-learn workflow, splitting datasets and model evaluation.
6. PyTorch, deep learning, transformers and LLM fundamentals.

## Completed worked result: three-neuron hidden layer

$$
x=\begin{bmatrix}2\\-1\end{bmatrix},\quad
W=\begin{bmatrix}2&1\\-1&3\\1&-2\end{bmatrix},\quad
b=\begin{bmatrix}1\\2\\-3\end{bmatrix}.
$$

$$
Z=Wx+b=\begin{bmatrix}4\\-3\\1\end{bmatrix},
\quad
A=\operatorname{ReLU}(Z)=\begin{bmatrix}4\\0\\1\end{bmatrix}.
$$

Final shape: **(3, 1)**. These are hand-picked weights, not trained parameters.
