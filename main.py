##DEVON##
##THIS IS ANOTHER TEST##
import numpy as np
import inquirer
from sympy import *

np.set_printoptions(precision=4, suppress=True)

print("Gram-Schmidt Orthonormalization Process")
print
print("---------------------------------------")
print

questions = [
    inquirer.List('type',
                    message="What form is your basis in?",
                    choices=['Vectors', 'Matrices'],
                    ),
]

answers = inquirer.prompt(questions)

for key in answers:
    choice = answers[key]
    if choice is 'Vectors':
        x = input("Please specify a space in R^n: ")
        print
        b = [ ]
        for i in xrange(x):
            vector = [int(x) for x in raw_input("Enter basis vector " + str(i+1) + ": ").split()]
            b.append(vector)
        basis = np.array(b)
    if choice is 'Matrices':
        x = input("Please specify your matrix dimension: ")
        dimension = int(x)
        print
        mtemp = [ ]
        zeroes = zeros(int(x), 1)
        for i in xrange(x):
            temp = [int(x) for x in raw_input("Enter row " + str(i+1) + ": ").split()]
            length = len(temp)
            mtemp.append(temp)
        zerotest = zeros(1, length+1)
        pprint(zerotest)
        matrix = Matrix(mtemp)
        matrix = matrix.col_insert(length+1, zeroes)
        print
        pprint(matrix)
        rref_matrix = matrix.rref()
        matrix = rref_matrix[0]
        print
        pprint(matrix)
        print
        for i in xrange(dimension):
            zero = 0
            for j in xrange(length+1):
                temp = matrix[i, j]
                zero = zero + temp
            if zero!=0:
                pprint(matrix[i, :])

print
print("Your basis is:")
print(basis)
print

def proj(v, w):
    c = float(np.inner(v, w))/np.inner(w, w)
    return map((lambda x: x * c), w)

def orthonormal(w):
    orthon_b = [ ]
    for i in xrange(len(w)):
        c = float(np.linalg.norm(w[i]))
        temp = (1/c) * w[i]
        orthon_b.append(temp)
    return orthon_b

def orthogonal(b):
    orthog_b = [ ]
    for i in xrange(len(b)):
        temp = b[i]
        for w in orthog_b:
            projection = proj(b[i], w)
            temp = map(lambda v, w: v - w, temp, projection)
        orthog_b.append(temp)
    return orthog_b
orthog_basis = np.array(orthogonal(basis))

print("Your orthogonal basis is:")
print(orthog_basis)
print

orthon_basis = np.array(orthonormal(orthog_basis))
print("Your orthonormal basis is:")
print(orthon_basis)
