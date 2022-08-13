import numpy as np

# 1. Create a numpy array 1D with values between 11 and 101, step by 3.
x = np.arange(11, 101)
# print("Array from 11 to 101:")
# print(x)

# 2. Extract the values from the numpy array
#input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#output: [1, 3, 5, 7, 9]
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

indices_1 = np.where(numpy_array%2 == 1)
# print("Output: ", numpy_array[indices_1])


# 3. Replace the odd values in the numpy array with -1
#input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#output: [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
indices_3 = np.where(numpy_array%2 == 1, -1, numpy_array)
# indices_3 = np.asarray([-1 if val < 25 for val in numpy_array])
# print("Output:", indices_3)


# 4. Reshape/Convert 1D array to 2D array.
# Input: np.arrange(10)
# Output: array with shape (2, 5)
numpy_array_4 = np.arange(10).reshape(2, 5)
# print(numpy_array_4)

# 5. Stack array x and y vertically (3 ways)
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)
x = np.arange(10).reshape(2, -1)
y = np.repeat(1, 10).reshape(2, -1)
numpy_array_vertically_1 = np.vstack((x, y))
numpy_array_vertically_2 = np.row_stack((x, y))
numpy_array_vertically_3 = np.concatenate((x, y))

# print(numpy_array_vertically_1)
# print(numpy_array_vertically_2)
# print(numpy_array_vertically_3)

# 6. Stack array x and y horizontally
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)
x = np.arange(10).reshape(2, -1)
y = np.repeat(1, 10).reshape(2, -1)
numpy_array_horizontally = np.hstack((x, y))

# print(numpy_array_horizontally)

# 7. Find common values between 2 numpy arrays:
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b = np.array([2, 5, 10, 9, 4, 8, 7, 12])
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = np.array([2, 5, 10, 9, 4, 8, 7, 12])
c = np.intersect1d(a, b)

# print("Common values",c)

# 8. Remove all values of array y from array x:
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([2, 5, 3])
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 5, 3])
# z = np.setdiff1d(x,y)
# print(z)

# 9. Swap 2 columns/rows in 2D array
# arr = np.arange(9).reshape(3, 3)
arr = np.arange(9).reshape(3, 3)
print(arr)
print(arr.T)


# 10. Reverse 2 columns/rows in 2D a
#arr = np.arange(9).reshape(3,3)
rever = np.fliplr(arr)
print(rever)
print(rever.T)