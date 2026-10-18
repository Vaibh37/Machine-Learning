# 04 — XOR: First Fully Trained Multilayer NumPy Network

**Checkpoint: 18 October 2026**

## What was actually implemented

- An XOR dataset with **four examples**, each with two binary input features.
- A **2 → 3 → 1 neural network** with three ReLU hidden neurons and one sigmoid output.
- Random weights with NumPy's `default_rng(42)`; zero biases.
- A vectorized forward pass, mean squared error, analytically derived backpropagation, and full-batch gradient descent.
- A 5,000-epoch training loop with learning rate `0.05`.
- Final predictions evaluated for all four XOR training cases.

**This implementation uses NumPy only** — no PyTorch, TensorFlow, or automatic differentiation.

## Why it matters

XOR is not linearly separable: a single linear decision boundary cannot separate the four output labels. A nonlinear hidden layer provides enough representational capacity to learn the dataset. This is a small **learning demonstration**, not a deployed production system or evidence that all model-evaluation topics have been mastered.

## Reproducible experiment

**Source:** [Neural-Network/examples/xor_network.py](https://github.com/Vaibh37/Neural-Network/blob/main/examples/xor_network.py)

```bash
python -m pip install numpy
python examples/xor_network.py
```

| Input | Target | Final probability | Class |
| --- | ---: | ---: | ---: |
| (0,0) | 0 | 0.08389788 | 0 |
| (0,1) | 1 | 0.95051648 | 1 |
| (1,0) | 1 | 0.95173893 | 1 |
| (1,1) | 0 | 0.08393200 | 0 |

- **Initial MSE at epoch 0:** 0.25023636000202243.
- **Final MSE after 5,000 updates:** 0.00471529585312808.
- **Correct classifications:** 4/4 on the *same training examples*; this is not held-out accuracy.
- **Random seed:** 42; different initializations may perform differently.

## The key mechanics

1. **Forward propagation:** `z_h = X @ W_h + b_h`; `h = ReLU(z_h)`; `z_o = h @ W_o + b_o`; `a_o = sigmoid(z_o)`.
2. **Loss:** `mean((a_o - y)**2)`.
3. **Backpropagation:** first the output-layer derivatives, then hidden-layer gradients through `W_o.T` and the ReLU mask.
4. **Gradient descent:** update `W_h`, `b_h`, `W_o`, and `b_o` together *after* calculating all gradients.
5. **Evaluate:** rerun the forward pass using updated parameters, apply a 0.5 classification threshold, and compute MSE.

## Visual documentation and math

- [Illustrated XOR lessons 11–16](https://github.com/Vaibh37/Neural-Network/tree/main/notes)
- [12 editable Excalidraw diagrams and high-resolution PNG exports](https://github.com/Vaibh37/Neural-Network/tree/main/assets/xor)
- [Complete backpropagation calculus](https://github.com/Vaibh37/ML-MATH/blob/main/calculus/04-xor-backpropagation-chain-rule.md)
- [NumPy syntax reference](https://github.com/Vaibh37/Python-Cheat_sheet/blob/main/NUMPY_NEURAL_NETWORK_PATTERNS.md)

## Honest limitations and follow-up

- 100% on four training samples is **not** an independent measure of model generalization.
- A tiny ReLU model can get stuck under other random seeds.
- Numerical finite-difference verification of **all** gradients was **postponed**.
- The Gradio interface was prototyped locally but **deployment to Hugging Face is not part of this project's current scope**.
- Repository documentation and detailed visuals come **before** drafting a technical article; no publication has been made.

**Next study topics:** model evaluation basics, scikit-learn, proper splits for datasets where they make sense, PyTorch/automatic differentiation, and eventually deployment/MLOps.
