import math
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Not Invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

# 4x  + 3y = 20
# -5x + 9y = 26
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

M = matrix
A = inverse(M)
B = Bmatrix

result = [[0, 0],[0, 0]]
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("X = ", round(result[j][j], 3))
print("Y = ", round(result[i][j], 3))

# import numpy as np 
# a = np.array(A)
# b = np.array(B)
# np.dot(A,B)
