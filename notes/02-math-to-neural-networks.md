# 02 — From Matrix Arithmetic to a Neural Network Layer

**Purpose:** Explain where the maths fits in an actual neural network. This is a **forward computation**, not learning.

## Step 1: Store inputs as a vector

```math
x=\begin{bmatrix}3\\4\end{bmatrix}
```

## Step 2: Give each hidden neuron its own weight row and bias

```math
W=\begin{bmatrix}2&-1\\-1&1\end{bmatrix},
\quad
b=\begin{bmatrix}1\\-2\end{bmatrix}.
```

- Neuron 1 weights: [2, -1], bias: 1.
- Neuron 2 weights: [-1, 1], bias: -2.

## Step 3: Weighted sums plus bias

```math
Z=Wx+b=
\begin{bmatrix}
2\cdot3-1\cdot4+1\\
-1\cdot3+1\cdot4-2
\end{bmatrix}
=
\begin{bmatrix}3\\-1\end{bmatrix}.
```

## Step 4: Apply ReLU inside the same hidden layer

```math
A=\mathrm{ReLU}(Z)=\begin{bmatrix}3\\0\end{bmatrix}.
```

This output is the **input to the next layer** if one exists.

![A dense-layer flowchart](../assets/foundations-to-models.svg)

## Shapes

- W:(2,2)
- x:(2,1)
- b:(2,1)
- Z and A:(2,1).

With s input samples in **columns**, X:(2,s), bias b:(2,1) broadcasts over all s columns to produce A:(2,s).

## Important distinction

An affine operation and an activation may be separate functions or modules in code. They are **not automatically separate groups of neurons**. A dense hidden layer is often described as their combination.

For reusable code and detailed reasoning, see the [Neural-Network repo](https://github.com/Vaibh37/Neural-Network/blob/main/notes/04-hidden-layer-forward-pass.md). For the matrix multiplication and bias rules, see [ML-MATH](https://github.com/Vaibh37/ML-MATH/blob/main/linear-algebra/matrices/04-broadcasting-and-bias.md).
