# gramschmidt
Basic Gram-Schmidt program for Math 254 Class (Linear Algebra)

Gram-Schmidt
Orthonormalization Program
 

Devon Rojas

Linear Algebra
Math 254


January 25, 2018



Summary

> The objective was to create a simple program to demonstrate the Gram-Schmidt Orthonormalization Process. I created my program in Python. It takes a user-defined space in Rn, with various vector input, calculates the necessary projection vectors and norms, and displays each part of the Gram-Schmidt algorithm. The example output below shows the process in R2 and R3. 


Example Output

Gram-Schmidt Orthonormalization Process

---------------------------------------

Please specify a space in R^n: 2

Enter basis vector 1: 1 3
Enter basis vector 2: 4 5

Your basis is:
[[1 3]
[4 5]]

Your orthogonal basis is:
[[ 1.   3. ]
 [ 2.1 -0.7]]

Your orthonormal basis is:
[[ 0.316  0.949]
 [ 0.949 -0.316]]

Would you like to enter another set? Press y to continue: y

Gram-Schmidt Orthonormalization Process

---------------------------------------

Please specify a space in R^n: 3

Enter basis vector 1: 2 4 6
Enter basis vector 2: 8 7 9
Enter basis vector 3: 3 4 7

Your basis is:
[[2 4 6]
 [8 7 9]
 [3 4 7]]

Your orthogonal basis is:
[[ 2.     4.     6.   ]
 [ 4.5    0.    -1.5  ]
 [ 0.114 -0.571  0.343]]

Your orthonormal basis is:
[[ 0.267  0.535  0.802]
 [ 0.949  0.    -0.316]
 [ 0.169 -0.845  0.507]]
