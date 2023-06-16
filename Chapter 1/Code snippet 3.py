import matplotlib.pyplot as plt
import random
import numpy as np

#define variables for plotting
colour_list = ['r-', 'm-', 'y-', 'c-', 'b-', 'g-']
colour_index = 0

def compute_output_vector(w, x):
    z = np.dot(w, x)
    return np.sign(z)

def show_learning(w):
    global colour_index
    print('w0 =', '%5.2f' % w[0], ', w1 =', '%5.2f' % w[1], ', w2 =', '%5.2f' % w[2])
    if colour_index == 0:
        plt.plot([1.0], [1.0], 'b_', markersize=12)
        plt.plot([-1.0, 1.0, -1.0], [1.0, -1.0, -1.0], 'r+', markersize=12)
        plt.axis([-2, 2, -2, 2])
        plt.xlabel('x1')
        plt.ylabel('x2')
    x = [-2.0, 2.0]
    if abs(w[2]) < 1e-5:
        y = [-w[1]/(1e-5)*(-2.0)+(-w[0]/(1e-5)),
             -w[1]/(1e-5)*(2.0)+(-w[0]/(1e-5))]
    else:
        y = [-w[1]/w[2]*(-2.0)+(-w[0]/w[2]),
             -w[1]/w[2]*(2.0)+(-w[0]/w[2])]
    plt.plot(x, y, colour_list[colour_index])
    if colour_index < (len(colour_list) - 1):
        colour_index += 1
    
random.seed(7)
LEARNING_RATE = 0.1
index_list = [0, 1, 2, 3]

# x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 2.0), (1.0, 2.0, -1.0), (1.0, 2.0, 2.0)]
y_train = [1.0, 1.0, 1.0, -1.0]

w = [0.2, -0.6, 0.25]
show_learning(w)
all_correct = False
while not all_correct:
    all_correct = True
    random.shuffle(index_list)
    for i in index_list:
        x = x_train[i]
        y = y_train[i]

        p_out = compute_output_vector(w, x)

        if y != p_out:
            for j in range(0, len(w)):
                w[j] += (y * LEARNING_RATE * x[j])

            all_correct = False
            show_learning(w)
plt.show()

#The four inputs in the are shown as 3 plus signs and one minus sign (y train)
#Red line - initial set of weights that don't correctly divide the chart
#Magenta - shifts slightly, then yellow, cyan and then blue
#Blue - correctly divides the chart with + on one side and - on the other