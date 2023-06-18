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

# OR Logic Function
# w1 = 1, w2 = 1, bOR = -0.5
def or_logic_function(x):
	w = np.array([1, 1])
	bOR = -0.5
	return perceptron_model(x, w, bOR)

# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("OR({}, {}) = {}".format(0, 1, or_logic_function(test1)))
print("OR({}, {}) = {}".format(1, 1, or_logic_function(test2)))
print("OR({}, {}) = {}".format(0, 0, or_logic_function(test3)))
print("OR({}, {}) = {}".format(1, 0, or_logic_function(test4)))