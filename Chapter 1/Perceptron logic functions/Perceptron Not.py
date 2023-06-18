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

# NOT Logic Function
# weight NOT = -1, bias NOT = 0.5
def not_logic_function(x):
	wNOT = -1
	bNOT = 0.5
	return perceptron_model(x, wNOT, bNOT)

# testing the Perceptron Model
test1 = np.array([0])
test2 = np.array([1])

print("NOT({}) = {}".format(0, not_logic_function(test1)))
print("NOT({}) = {}".format(1, not_logic_function(test2)))