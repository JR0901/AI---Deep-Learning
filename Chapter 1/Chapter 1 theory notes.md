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

Difference between neural networks and logic gates:
- Perceptron inputs aren't limited to boolen values. Perceptrons can only output 1 of 2 values - other neuron models can output range of real numbers
- Neurons can take significantly more inputs than logic gates and perform more complex functions
- Learning algorithms can be used to automatically design neural networks by learning from example.

## The Perceptron Learning Algorithm

[Code snippet 2](https://github.com/JR0901/AI---Deep-Learning/blob/main/Chapter%201/Code%20snippet%202.py)

How do we determine the weights that affect the z values? -> Use the perceptron learning algorithm
Perceptron learning algorithm is a supervised learning algorithm
-> implies that the model is given inputs and desired output data (ground truth).
-> with the expectation that the model will learn the relationship between the input and output

unsupervised learning - learning algorithm that finds patterns in the data itself with no ground truth.
Example - natural language text

Model = network
Training a model -> figuring out/calculating weights for a network consisting of one or more neurons

The algorithm in code snip 1
- Randomly initialise the weights
- Select one I/O pair at random
- Present the values x1,..., xn to the perceptron to compute output y
- If the output y is different from the ground truth for the I/O pair, adjust the weights as following:
  - if y<0, add ηxi to each wi
  - if y>0, subtract ηxi from each wi
- Repeat until perceptron predicts all examples correctly.

For some sets of I/O values the algorithm will not converge.
If there is a set of weights that lets the perceptron represent the I/O pairs then the algorithm will converge.

Learning rate = η -> arbitrary constant -> hyperparameter - parameter not adjusted by the learning algorithm but can still be adjusted.

Setting the learning rate to != 1 can lead to a faster convergance.
Weight adjustments may vary because inputs vary (not only 1 & -1 like in previous example)

The above code shows learning of the NAND function.

Any real number input will produce either a 1 or -1 output. 

![alt text](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9780137470198/files/graphics/pg40_Image_16.jpg)

The output is shown as a function of two inputs *x1* and *x2*
The perceptron divides the 2D space into 2 regions. 1 region is +1, the other -1. The line represents the boundary where weighted sum of inputs = 0 -> sign function will change value when input is 0:

*w0x0* + *w1x1* + *w2x2* = 0

x2 is the y axis, so make x2 a function of x1:

*x2* = -(*w1*/*w2*)*x1* -(*w0*/*w2*)

So the gradient = -(*w1*/*w2*) and *y* intercept = -(*w0*/*w2*)

[code snippet 3](https://github.com/JR0901/AI---Deep-Learning/blob/main/Chapter%201/Code%20snippet%203.py)

In this codde, learning progress in the order - red, magenta, yellow, cyan, blue.

## Limitations of the Perceptron

