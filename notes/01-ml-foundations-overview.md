# 01 — ML Foundations: Concept Map

**Status: learning preview.** This overview defines terms needed for upcoming study; it does **not** mean model training has been completed.

## What is machine learning?

A machine-learning system learns parameter values from examples so that its predictions generalize to new inputs.

| Term | Meaning | Small example |
|---|---|---|
| Feature | An input measurement | Number of rooms |
| Target / label | Desired answer | House price |
| Sample | One data record | One house |
| Dataset | Collection of samples | Many houses |
| Model | Function producing a prediction | Predicted price from features |
| Parameter | Trainable quantity | Weight or bias |
| Prediction | Output for an input | Estimated price |
| Loss | Numeric penalty for predictions | Squared error |
| Training | Adjusting model parameters using data | Update weights |
| Inference | Computing predictions with current parameters | Predict a new price |

A typical supervised learning sequence is **collect data → split data → fit a model → evaluate on held-out examples → use the model**. This is an overview of upcoming work, not a completed pipeline.

## Linear model preview

For one feature:

$$
\hat y=wx+b
$$

For several features:

$$
\hat y=\mathbf w\cdot\mathbf x+b.
$$

A dense neural network layer generalizes this computation to multiple neurons with **Z = WX + b**, then applies an activation such as ReLU.

## Loss preview

For a numeric target y and prediction ŷ:

$$
\text{squared error}=(y-\hat y)^2.
$$

For many samples, mean squared error (MSE) averages their squared errors. Smaller training loss is not automatically better performance on unseen samples.

## Connection to current practice

- Vectors and matrices encode data and parameter collections.
- Matrix multiplication calculates weighted sums efficiently.
- Broadcasting adds biases to multiple predictions.
- ReLU introduces nonlinearity into dense networks.

These concepts have been practiced numerically; choosing loss functions, training, validation, and deployment remain future lessons.

**Links:** [matrix arithmetic](https://github.com/Vaibh37/ML-MATH/tree/main/linear-algebra/matrices), [dense-layer forward pass](https://github.com/Vaibh37/Neural-Network/blob/main/notes/04-hidden-layer-forward-pass.md).
