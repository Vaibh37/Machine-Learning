# Learning Progress

Last reviewed: **18 October 2026**. Progress levels describe demonstrated exercises, not job-readiness. Historical 16 October checkpoints remain below.

## New completed milestone — 18 October 2026

**Full XOR 2 → 3 → 1 NumPy neural network** implemented with ReLU hidden activation, sigmoid output, dataset MSE, manual backpropagation for all 13 trainable parameters, randomized initialization, and 5,000 full-batch gradient descent updates. Final MSE: **0.00471529585312808**; all four XOR training rows classified correctly. Not a separate held-out evaluation. [Experiment and limitations](notes/04-xor-multilayer-network-experiment.md) · [Runnable code](https://github.com/Vaibh37/Neural-Network/blob/main/examples/xor_network.py) · [12 high-resolution diagrams and Excalidraw sources](https://github.com/Vaibh37/Neural-Network/tree/main/assets/xor).

Full numerical gradient checking was deferred by choice. Gradio deployment is skipped; documentation is the focus before writing an article.


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
| Vectorized multiple-example predictions | Used one shared linear neuron on x=[1,2,3,4] and checked (4,) NumPy output shape | [Batch training implementation](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_batch_neuron_numpy.py) |
| Dataset MSE and batch gradients | Independently corrected averaging order; obtained initial MSE 21, ∂L/∂w=-25, ∂L/∂b=-8 | [Dataset gradient lesson](https://github.com/Vaibh37/Neural-Network/blob/main/notes/07-vectorized-batch-gradient-descent.md) |
| Full-batch training loop | Personally coded NumPy loop over 4 examples for 5 epochs; MSE 21→approximately 0.325768 | [Runnable code](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_batch_neuron_numpy.py) |
| ReLU derivative in NumPy | Practiced elementwise mask (z > 0).astype(float); learned what .astype(float) does | [Activation derivative example](https://github.com/Vaibh37/Neural-Network/blob/main/examples/relu_derivative_numpy.py) |
| Chain rule through activation (introduced) | Explained z→a→L and ∂L/∂z = (∂L/∂a)(∂a/∂z); not yet extended through all model parameters | [Chain-rule introduction](https://github.com/Vaibh37/Neural-Network/blob/main/notes/08-relu-derivative-and-chain-rule-intro.md) |
| Python for-loop reassignment | Explained why the updated w/b values persist across iterations and why an outside print shows the last result | [Python loop trace](https://github.com/Vaibh37/Python-cheat_sheet/blob/main/FOR_LOOP_TRACE.md) |

## Historical checkpoint — 16 October (done vs not done)

**Implemented (16 October):** single-example training in plain Python and four-example NumPy full-batch gradient descent. Used one shared linear neuron, vectorized predictions, dataset MSE, correct averaged weight and bias gradients, parameter updates, and a five-epoch loop. Dataset MSE changed **21.0 -> 0.325768**.

**Practiced:** ReLU derivative in NumPy using Boolean comparisons and .astype(float).

**Introduced but not yet fully implemented:** chain-rule backward step through ReLU: ∂L/∂z = (∂L/∂a)(∂a/∂z). Understanding of the connection is progressing; the full chain to w and b is still next.

**Not implemented:** training a multi-neuron hidden layer, full hidden-layer backpropagation, XOR classifier, or validation on unseen examples. The existing hidden-layer forward pass still uses hand-picked parameters.

## Upcoming lessons (not completed)

1. Complete ∂L/∂w and ∂L/∂b through an activated neuron using the chain rule.
2. Apply backward propagation across a hidden layer, with explicit shapes and notation.
3. Train a **2 -> 3 -> 1** NumPy XOR network; verify all four XOR input combinations and training behavior.
4. Target around **20 October 2026** for XOR and editable Excalidraw diagrams with image exports, subject to understanding.
5. Draft a complete technical article after verification for **Medium and X Articles**, pointing to GitHub source.
6. Later: pandas, scikit-learn, evaluation, PyTorch, LLM internals, RAG, LangChain, LangGraph, ML deployment and MLOps. Continue Python DSA in parallel.

See [training-workflow checkpoint](notes/03-first-dataset-training-workflow.md).

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
