# Learning Progress

Last reviewed: **16 October 2026**. Progress levels here describe the study session, not job-readiness or model-training capability.

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
| Partial derivatives of prediction loss | Derived `dw = 2*(pred_y-y)*x` and `db = 2*(pred_y-y)`; explained why x appears | [Gradient lesson](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/02-gradient-descent-single-sample.md) |
| Learning rate and overshooting | Compared alpha 0.1 (loss 4→36) with alpha 0.01 (loss 4→1.44) for a separate example | [Math worked example](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/02-gradient-descent-single-sample.md) |
| First gradient descent training loop | Personally coded a 5-iteration pure-Python loop for one x=2, y=10 example; updated both w and b; prediction 7→9.90625, squared loss 9→0.0087890625 | [Notes and verification](https://github.com/Vaibh37/Neural-Network/blob/main/notes/06-first-gradient-descent-training-loop.md) |
| Python for-loop reassignment | Explained why the updated w/b values persist across iterations and why an outside print shows the last result | [Python loop trace](https://github.com/Vaibh37/Python-cheat_sheet/blob/main/FOR_LOOP_TRACE.md) |

## Current checkpoint — done vs not done

**Implemented (16 October):** forward prediction, single-example squared loss, chain-rule gradients for one weight and bias, update formulas and five repeats in **plain Python**. The example has verified expected results. The implementation doesn't require NumPy.

**Introduced:** PyTorch automatic differentiation as a concept; understanding that hidden-layer backpropagation extends the chain rule.

**Not implemented:** vectorized training over multiple examples, full-dataset MSE gradients, activation derivatives for training, backpropagation through a hidden layer, trained XOR classifier, or validation on unseen examples.

## Upcoming lessons (not completed)

1. Move the one-example Python training loop into **NumPy arrays** and compare with equivalent scalar code.
2. Learn vectorized gradients of **mean** squared error over several training examples.
3. Derive activation derivatives and backpropagation through a hidden layer.
4. Aim by **20 October 2026** to train a **2→3→1 XOR network**, verify all four XOR input combinations, store editable diagrams and PNG/SVG exports, and draft a technical Medium article. This is a target, not a completed milestone.
5. Later: pandas, scikit-learn workflow, evaluation, PyTorch, broader deep learning, transformers/LLMs, RAG, deployment and MLOps. Continue manageable Python DSA practice in parallel.

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
