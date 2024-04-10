import numpy as np

# Create an empty 3x3 matrix filled with zeros
matrix1 = np.zeros((3, 3))
matrix2 = np.zeros((3, 3))

matrix1[0, 0] = 1
matrix1[1, 1] = 5
matrix1[2, 2] = 9
matrix2[0, 1] = 2
matrix2[1, 0] = 4
matrix2[1, 2] = 6
matrix2[2, 1] = 3
matrix2[2, 2] = 8

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

matrix3=matrix1+matrix2
print("\nMatrix addition:")
print(matrix3)

matrix4=matrix1-matrix2
print("\nMatrix subtraction:")
print(matrix4)

matrix5=matrix1*matrix2
print("\nMatrix multiplication:")
print(matrix5)

matrix6=2*matrix1
print("\nMatrix multiplication by a constant:")
print(matrix6)