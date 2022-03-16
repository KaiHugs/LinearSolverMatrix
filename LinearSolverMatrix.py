import math
def gaussian(x):
    for i in range(len(x)):
        if x[i][i] == 0:
            for j in range(i+1, len(x)):
                if x[i][j] != 0:
                    x[i], x[j] = x[j], x[i]
                    break
            else:
                raise ValueError("Not Invertible") # if inverse == matrix
        for j in range(i+1, len(x)):
            elim(x[i], x[j], i)
    for i in range(len(x)-1, -1, -1):
        for j in range(i-1, -1, -1):
            elim(x[i], x[j], i)
    for i in range(len(x)):
        elim(x[i], x[i], i, target=1)
    return x

def elim(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def inverse(x):
    tmp = [[] for _ in a]
    for i,row in enumerate(x):
        assert len(row) == len(x)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(x)-i-1))
    gaussian(tmp)
    mat = []
    for i in range(len(tmp)):
        mat.append(tmp[i][len(tmp[i])//2:])
    return mat

R = int(input("Enter the number of Equations:"))
  
# Initialize matrix
matrix = []
print("Enter X & Y coeffcients respectively.")
  
# For user input
for i in range(R):          # First Equation
    a =[]
    for j in range(R): 
         a.append(float(input("Enter First: ")))
    matrix.append(a)
    break
Bmatrix = []
for i in range(R):          # Second Equation
    a =[]
    for j in range(R):  
         a.append(float(input("Enter Second: ")))
    matrix.append(a)
    break
Bmatrix = []

for i in range(R): # A for loop for row entries
    value = float(input("Enter the value of the Equations: "))
    Bmatrix.append([value])

A = inverse(matrix)

result = [[0, 0],[0, 0]]
for i in range(len(Bmatrix)):
 
    # iterating by column 
    for j in range(len(Bmatrix[0])):
 
        # iterating by rows 
        for k in range(len(Bmatrix)):
            result[i][j] += A[i][k] * Bmatrix[k][j]

print("X = ", round(result[j][j], 3))
print("Y = ", round(result[i][j], 3))

# import numpy as np 
# a = np.array(A)
# b = np.array(B)
# np.dot(A,B)
