# Machine Learning — Learning Hub

Practical notes and project milestones for learning machine learning from first principles. This repository is the **index and connecting layer** between math, NumPy, neural networks, and future model training. It does not duplicate every detailed note.

> Status: foundations in progress. Nothing here claims that a trained production model has been built.

## Start here

1. [Current study progress](STUDY_PROGRESS.md) — what was practiced and what is next.
2. [Core concepts and terminology](notes/01-ml-foundations-overview.md) — reference and learning preview.
3. [From arrays to neural networks](notes/02-math-to-neural-networks.md) — how today's math and NumPy exercises connect to a forward pass.
4. [First dataset training workflow](notes/03-first-dataset-training-workflow.md) — what full-batch training now demonstrates and does not demonstrate.
5. [Learning roadmap](ROADMAP.md) — ordered topics and planned hands-on projects.

## Related repositories

| Repository | What belongs there |
|---|---|
| [ML-MATH](https://github.com/Vaibh37/ML-MATH) | Vectors, angles, matrices, broadcasting, formulas and math diagrams |
| [Neural-Network](https://github.com/Vaibh37/Neural-Network) | Neurons, activations, forward passes, loss, training and backpropagation notes as studied |
| [Python-cheat_sheet](https://github.com/Vaibh37/Python-cheat_sheet) | Python and NumPy syntax, runnable snippets, DSA reference |
| **Machine-Learning (here)** | Learning index, ML workflow concepts, models, experiments and future evaluations |

## Documentation conventions

- **Practiced** means an example was solved, not that a full topic is mastered.
- **Introduced** means studied conceptually without a complete implementation.
- **Planned** means not covered or implemented yet.
- A **forward pass** is not a trained model.
- Use small worked examples with exact expected output and correct array shapes.
- Keep repository-specific notes in their proper repo and cross-link them here.

## Technology

Python and NumPy now. pandas, scikit-learn, PyTorch, model evaluation, deployment, and MLOps will be added only as they are studied.

**Last study checkpoint:** 16 October 2026 — implemented the original single-example training loop and then a **four-example, five-epoch NumPy full-batch loop** (MSE **21→~0.325768**). ReLU derivative practiced; chain rule through activation introduced. **Hidden-layer backpropagation and XOR training remain planned.** See [study progress](STUDY_PROGRESS.md) and [runnable batch training](https://github.com/Vaibh37/Neural-Network/blob/main/examples/train_batch_neuron_numpy.py).
