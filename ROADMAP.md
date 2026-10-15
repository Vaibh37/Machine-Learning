# Roadmap: ML Engineer Foundations to Practical Projects

This is a learning sequence, not a fixed completion guarantee. Do not mark a module as mastered because a formula was calculated once.

![Learning map](assets/foundations-to-models.svg)

## Phase 1 — Programming and numeric foundations (in progress)

- Python core and DSA practice.
- NumPy arrays, shapes, slicing, matrix operations and broadcasting.
- Vectors, matrix multiplication, transpose, angles.
- Refresh calculus and probability when needed.

**Evidence:** [Python-cheat_sheet](https://github.com/Vaibh37/Python-cheat_sheet) and [ML-MATH](https://github.com/Vaibh37/ML-MATH).

## Phase 2 — First predictive models (upcoming)

- Input features, targets, predictions and datasets.
- Linear regression; squared error and mean squared error.
- Gradient descent using a small numeric example.
- Train a simple model, inspect predictions, explain its failure cases.
- pandas and scikit-learn workflows, data splits and evaluation.

## Phase 3 — Neural network training (upcoming)

- Dense layers and activation functions (forward pass practiced).
- Loss functions for regression and classification.
- Derivatives, chain rule, gradients, backpropagation.
- Learnable weights and biases, optimizer steps and a training loop.
- PyTorch implementation and a documented end-to-end experiment.

**Evidence so far:** [Neural-Network](https://github.com/Vaibh37/Neural-Network) contains forward-pass calculations, *not* a trained classifier.

## Phase 4 — Applied systems (future)

- Transformer foundations, tokenization, attention and embeddings.
- LLM application basics and RAG.
- Supervised fine-tuning (SFT), then preference training such as DPO as appropriate.
- Serving, evaluation, deployment and MLOps.

## Milestone requirements before publishing a model project

A project should include the dataset source, preprocessing, reproducible run commands, metric definitions, baseline, results, limitations, and what was actually implemented. Avoid calling inference-only code a trained model.
