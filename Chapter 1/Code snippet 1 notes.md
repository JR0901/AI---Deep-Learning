Notes and trace table for code snippet 1

Basic implementation of a signum function

Trace table:
W0	W1	W2					
0.2	-0.6	0.25					
							
X0 |	X1 |	X2 | W0*X0 | W1*X1 | W2*X2 |   Z   | Y
1	 | -1	 | -1	 |  0.2	|   0.6	 | -0.25 | 1.05  |	1
1	 | -1	 | 1	 |  0.2	|   0.6	 |  0.25 | 0.55  |	1
1	 |  1	 | -1  |	0.2	|  -0.6  | -0.25 | -0.15 | -1
1	 |  1  |	1	 |  0.2	|  -0.6	 | 0.25 |	-0.65 | -1
