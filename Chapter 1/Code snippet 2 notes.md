Line 26 highlights the input. The first value is always 1 because it is the bias input.

Line 12 is the perceptron loop. Nested loop with inner loop that goes through each training example in random oreder. Computes the output and adjustst and prints the weights if output is wrong. 

In this code, the adjustment value is multiplied by y (Line 45)

the y_train (line 27 is the ground truth)