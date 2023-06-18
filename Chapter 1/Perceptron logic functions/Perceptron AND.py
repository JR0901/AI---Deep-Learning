# importing Python library
import numpy as np

# define Unit Step Function - this is similar 
def unit_step(v):
	if v >= 0:
		return 1
	else:
		return 0

# design Perceptron Model
def perceptron_model(x, w, b):
	v = np.dot(w, x) + b
	y = unit_step(v)
	return y

# AND Logic Function
# here weight1  = 1,
# weight2 = 1, bias AND = -1.5
def and_logic_function(x):
	w = np.array([1, 1])
	bAND = -1.5
	return perceptron_model(x, w, bAND)

# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("AND({}, {}) = {}".format(0, 1, and_logic_function(test1)))
print("AND({}, {}) = {}".format(1, 1, and_logic_function(test2)))
print("AND({}, {}) = {}".format(0, 0, and_logic_function(test3)))
print("AND({}, {}) = {}".format(1, 0, and_logic_function(test4)))