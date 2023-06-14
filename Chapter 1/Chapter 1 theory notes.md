# **Chapter 1 theory notes**

Perceptron - artificial neuron that uses the Signum function.

Neurons have cell bodies, dendrites, a single axon and connected through synapses.
Perceptrons have computational units, a numbmer of inputs with weights, and an output

Neuron receives stimuli on the dendrites -> neuron activates -> ouputs stimulus on its axon -> transmitted through synapses to other neurons.
Perceptron receives inputs (*x0,x1,...,xn*) -> perceptron applies some activation function that does computations on the sum of weights *z* -> perceptron outputs *y* -> *y* passed as input to next perceptron

Signum function - if input > 0, *y* = 1, else *y* = -1

Bias input - *x0* always equals 1

## Example of a Two-Input Perceptron
[Code snippet 1](https://github.com/JR0901/AI---Deep-Learning/blob/main/Chapter%201/Code%20snippet%201.py)

[Code snippet 1 notes](https://github.com/JR0901/AI---Deep-Learning/blob/main/Chapter%201/Code%20snippet%201%20notes.md)

Difference between neural networks and logic gates:
- Perceptron inputs aren't limited to boolen values. Perceptrons can only output 1 of 2 values - other neuron models can output range of real numbers
- Neurons can take significantly more inputs than logic gates and perform more complex functions
- Learning algorithms can be used to automatically design neural networks by learning from example.

## The Perceptron Learning Algorithm
