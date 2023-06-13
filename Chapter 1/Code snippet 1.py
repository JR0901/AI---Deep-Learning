def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i]
    print(z)# Compute sum of weighted inputs
    if z < 0: # Apply sign function
        return -1
    else:
        return 1
        
#x = [(1, -1, -1), (1, 1, -1), (1, -1, 1), (1, 1, 1)]
x = [1, -1, -1]
w = [0.2, -0.6, -0.25]

compute_output(w, x)
