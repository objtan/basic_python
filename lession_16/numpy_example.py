import numpy as np
# 1. 1D array
arr = np.array([1, 2, 3, 4])
# print(arr)

# 2. 2D array
arr = np.array([[4, 5, 6], [1, 2, 3]])
# print(arr)

# 3. 3D array
arr = np.array([[2, 3, 1,3], [1, 4, 19, 23], [5, 9, 2, 0]])
# print(arr.shape)

# 4. initialize arrays with zeros values
arr = np.zeros((3, 4), dtype=float)
# print(arr)

# 5. initialize arrays with ones values
arr = np.ones((3, 4), dtype=int)
# print(arr)

# 6. initialize arrays with arrange
arr = np.arange(3, 4, 9)
# print(type(arr))

# 7. initialize arrays with any values
arr = np.full((3, 4), 9)
# print(arr) 

# 8. initialize arrays with eye values
arr = np.eye(4, dtype=int)
# print(arr)

# 9. initialize arrays with random values
arr = np.random.random((3, 4))
arr_1 = np.random.randint(9, size=(3, 4))
# print(arr)
# print(arr_1)

# Numpy arrays infomation
# Type
'''print(arr.dtype)
print(type(arr))
print(arr.shape)
print(arr.size)
print(arr.ndim)'''


# Array indexing/slicing
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=int)
'''print(arr)
print(arr[:2, 1:3])
print(arr[0, 1])
print(arr[1, :])'''

# integer indexing
# print(arr[[0, 1, 2], [0, 1, 0]])

# boolean indexing
# print(arr[arr > 5])

# Array Mathematic
x = np.array([[1, 2], [3, 4]], dtype=float)
y = np.array([[5, 6], [7, 8]], dtype=float)
# print(x + y)
# print(np.add(x, y))

# print(x - y)
# print(np.subtract(x, y))

# print(x * y)
# print(np.multiply(x, y))

# print(x / y)
# print(np.divide(x, y))

# print(np.sqrt(x))

# print(x.dot(y))
# print(np.dot(x, y))
