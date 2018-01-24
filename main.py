##DEVON##
##THIS IS ANOTHER TEST##
import numpy as np

np.set_printoptions(precision=4, suppress=True)

print("Gram-Schmidt Orthonormalization Process")
print
print("---------------------------------------")
print
x = input("Please specify a space in R^n: ")
print

b = [ ]

for i in xrange(x):
    vector = [int(x) for x in raw_input("Enter basis vector " + str(i+1) + ": ").split()]
    b.append(vector)
basis = np.array(b)

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
