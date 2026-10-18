# Roadmap: ML Engineer Foundations to Practical Projects

This is a learning sequence, not a fixed completion guarantee. Do not mark a module as mastered because a formula was calculated once.

![Learning map](assets/foundations-to-models.svg)

## Phase 1 — Programming and numeric foundations (in progress)

- Python core and DSA practice.
- NumPy arrays, shapes, slicing, matrix operations and broadcasting.
- Vectors, matrix multiplication, transpose, angles.
- Refresh calculus and probability when needed.

**Evidence:** [Python-cheat_sheet](https://github.com/Vaibh37/Python-cheat_sheet) and [ML-MATH](https://github.com/Vaibh37/ML-MATH).

## Phase 2 — First predictive models (in progress)

- Input features, targets, predictions and datasets.
- **Practiced:** linear regression predictions `y_pred = w * x + b`, squared error, NumPy MSE, manual comparison of losses at different weights.
- **Practiced:** introductory differentiation (power, chain and partial derivative rules; loss notation).
- **Implemented 16 October:** manual single-example gradients, weight and bias updates, and a five-epoch loop in plain Python; prediction 7→9.90625, squared loss 9→0.0087890625.
- **Implemented 16 October:** vectorized NumPy predictions, dataset MSE, full-batch ∂L/∂w and ∂L/∂b, and five epochs with four examples; MSE 21→~0.325768.
- **Completed 18 October:** trained a 2→3→1 XOR network with analytical gradients through sigmoid, ReLU and both parameterized layers; next examine model limitations and evaluation.
- pandas and scikit-learn workflows, data splits and evaluation.

## Phase 3 — Neural network training (first project completed)

- Dense layers and activation functions (forward pass practiced).
- Loss functions for regression and classification.
- Power rule, chain rule and partial derivatives practiced; ReLU derivative and local chain rule through activation introduced. Hidden-layer backpropagation implemented for the XOR network on 18 October.
- Learnable weights and biases, optimizer steps and training loops (**single neuron and full 2→3→1 multilayer XOR training implemented in NumPy**).
- PyTorch implementation and a documented end-to-end experiment.

**Evidence as of 18 October:** [Neural-Network](https://github.com/Vaibh37/Neural-Network) includes a fully trained [XOR classifier](https://github.com/Vaibh37/Neural-Network/blob/main/examples/xor_network.py), [complete backpropagation lessons](https://github.com/Vaibh37/Neural-Network/tree/main/notes), and [12 editable diagrams with PNG exports](https://github.com/Vaibh37/Neural-Network/tree/main/assets/xor).

## Phase 4 — Deep learning and modern ML (future)

- pandas, scikit-learn, data preparation, train/validation/test split, baselines, regression/classification and metrics.
- PyTorch, automatic differentiation, training loops, CNN/RNN context where useful, and deep learning practice.
- Transformer foundations, tokenization, attention, embeddings and LLM internals.

## Phase 5 — LLM engineering and applied AI (future)

- Embeddings, vector stores, retrieval, RAG, reranking, evaluation and grounded generation.
- **LangChain and LangGraph**, tool use, state, agentic workflows, reliability, and evaluation.
- Supervised fine-tuning (SFT) and later preference optimization (DPO), when foundations are ready.
- Inference and serving, experiment tracking, deployment and MLOps.

## Immediate milestone: first from-scratch neural network

**Implementation completed ahead of the 20 October 2026 target:** The NumPy **2-input → 3-hidden → 1-output** XOR network trains for 5,000 epochs with 100% classification on its four training examples. Forward pass, MSE, manual gradients for all 13 parameters, updates, reproducible random initialization, 12 editable Excalidraw diagrams, SVGs, and high-resolution PNGs are in [Neural-Network](https://github.com/Vaibh37/Neural-Network). A technical article for Medium/X is **not yet drafted for publication**; thorough notes and diagrams take priority. Full numerical gradient checking is postponed.

**Long-term employment-preparation target: 31 May 2027.** Alongside ML projects, practice Python DSA/LeetCode, deployment and portfolio documentation. No unrelated backend or Rust detours in this active study plan.

## Milestone requirements before publishing a model project

A project should include the dataset source, preprocessing, reproducible run commands, metric definitions, baseline, results, limitations, and what was actually implemented. Avoid calling inference-only code a trained model.
