# 03 — First Dataset Training Workflow (16 October 2026)

## What was actually implemented

A **linear neuron with one shared weight and one bias** was trained on **four examples** using NumPy **full-batch gradient descent**. This extends the previous one-example plain-Python training loop; it is not a trained deep neural network.

| Item | Result |
| --- | --- |
| Input and target arrays | Four examples, shape (4,) |
| Initial prediction | [4, 7, 10, 13] |
| Initial dataset MSE | 21.0 |
| Initial weight gradient (∂L/∂w) | -25.0 |
| Initial bias gradient (∂L/∂b) | -8.0 |
| Learning rate | 0.05 |
| MSE after first batch update | 0.92875 |
| MSE after five epochs | ~0.325768 |

One **epoch** here means computing predictions and gradients over **all four examples**, updating the shared weight/bias once, and measuring post-update loss. Gradients are recalculated each epoch.

## ML significance

- **Vectorization** applies the same model to every input without a Python loop over samples.
- **Dataset MSE** averages per-example squared prediction errors.
- **Gradient descent** uses the average per-example gradients to change parameters so as to *try* to decrease loss.
- **Batch** means the examples used for an update. This run used the *entire dataset*, so it is **full-batch**, not mini-batch or stochastic gradient descent.
- A decreasing **training loss** proves only that the model fits this training dataset better during the run. This exercise does **not** evaluate generalization or held-out data.

## First activation derivative

ReLU derivative with a NumPy Boolean mask and .astype(float) has been practiced. The chain-rule relation **∂L/∂z = (∂L/∂a)(∂a/∂z)** for z -> a -> L has been introduced with a worked negative-ReLU example. No hidden-layer weight-gradient computation or trained XOR implementation yet.

## Implementation and math sources

- [Runnable four-example training loop](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_batch_neuron_numpy.py)
- [Full lesson and loss trace](https://github.com/Vaibh37/Neural-Network/blob/main/notes/07-vectorized-batch-gradient-descent.md)
- [Dataset MSE derivation](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/03-batch-mse-and-relu-chain-rule.md)
- [ReLU derivative and activation chain rule](https://github.com/Vaibh37/Neural-Network/blob/main/notes/08-relu-derivative-and-chain-rule-intro.md)

## Next

Derive parameter gradients through ReLU; understand the local backward flow through a hidden layer; implement, train and verify the **2 -> 3 -> 1 XOR** network with NumPy. Aim around **20 October 2026** if understanding supports it. Prepare editable Excalidraw diagrams and an accurate technical article for Medium and X Articles **after** the implementation is verified.
