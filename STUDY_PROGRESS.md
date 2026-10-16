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
| MSE in NumPy | Independently wrote vectorized error, square, `np.mean`; verified MSE 6.5 | [Loss lesson](https://github.com/Vaibh37/Neural-Network/blob/main/notes/05-linear-regression-loss-and-gradients.md) |
| Linear regression predictions | Implemented `y_pred = w * x + b` and evaluated MSE at hand-picked weights: 750 at w=10, 187.5 at w=15 | [Prediction example](https://github.com/Vaibh37/Neural-Network/blob/main/examples/linear_regression_and_mse.py) |
| Introductory derivatives | Power rule, constants, sum rule, nested chain rule, notation and simple partials practiced | [Calculus lessons](https://github.com/Vaibh37/ML-MATH/tree/main/calculus) |
| Deriving a one-sample loss | Connected `x=4, y=10` to `L(w,b)=(4w+b-10)^2` | [Math loss derivation](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/01-derivatives-and-loss.md) |

## Introduced (not yet implemented)

- Training as repeated forward pass → loss → parameter update.
- Gradient descent direction from positive/negative slopes and the learning-rate update formula.
- A single-example squared-error gradient; no full-dataset gradient code yet.

## Upcoming lessons (not completed)

1. **16 October:** review derivative notation and apply the chain rule to loss; implement weight **and** bias updates in NumPy.
2. Implement and verify a linear-regression training loop (not done).
3. Derive sigmoid/ReLU gradients and backpropagation through a hidden layer (not done).
4. Aim by **20 October 2026** to train a **2→3→1 XOR network**, verify all four XOR input combinations, store diagrams and draft a technical Medium article. Target, not guarantee.
5. Then: pandas, scikit-learn workflow, evaluation, PyTorch, broader deep learning, transformers/LLMs, RAG, deployment and MLOps. Continue manageable Python DSA practice in parallel.

## Completed worked result: three-neuron hidden layer

```math
x=\begin{bmatrix}2\\-1\end{bmatrix},\quad
W=\begin{bmatrix}2&1\\-1&3\\1&-2\end{bmatrix},\quad
b=\begin{bmatrix}1\\2\\-3\end{bmatrix}.
```

```math
Z=Wx+b=\begin{bmatrix}4\\-3\\1\end{bmatrix},
\quad
A=\mathrm{ReLU}(Z)=\begin{bmatrix}4\\0\\1\end{bmatrix}.
```

Final shape: **(3, 1)**. These are hand-picked weights, not trained parameters.
