
### 1. Installing NumPy

'''
pip install numpy

This command installs the NumPy library using `pip`.
'''

### 2. Creating Arrays

#### Creating 1D, 2D, and 3D Arrays


import numpy as np

# 1D Array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

# 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr_3d)

'''
Output:

1D Array: [1 2 3 4 5]
2D Array:
 [[1 2 3]
 [4 5 6]]
3D Array:
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]


This code creates and prints 1D, 2D, and 3D NumPy arrays.
'''

#### Creating Arrays with Special Values


# Array of zeros
zeros_array = np.zeros((3, 3))
print("Zeros Array:\n", zeros_array)

# Array of ones
ones_array = np.ones((2, 4))
print("Ones Array:\n", ones_array)

# Identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# Array with random values
random_array = np.random.random((2, 2))
print("Random Array:\n", random_array)

# Array with a range of values
range_array = np.arange(0, 10, 2)
print("Range Array:", range_array)

# Array with evenly spaced values
linspace_array = np.linspace(0, 1, 5)
print("Linspace Array:", linspace_array)


'''
Output:

Zeros Array:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Ones Array:
 [[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
Identity Matrix:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Random Array:
 [[0.5488135  0.71518937]
 [0.60276338 0.54488318]]
Range Array: [0 2 4 6 8]
Linspace Array: [0.   0.25 0.5  0.75 1.  ]


This code creates arrays filled with zeros, ones, an identity matrix, 
random values, and arrays with specific ranges and evenly spaced values.
'''

#### Shape and Size of Arrays


# Check shape and size
print("Shape of 2D Array:", arr_2d.shape)
print("Size of 2D Array:", arr_2d.size)


'''
Output:

Shape of 2D Array: (2, 3)
Size of 2D Array: 6


This code checks the shape (dimensions) and size (number of elements) of a 2D array.
'''

### 3. Array Operations

#### Basic Arithmetic Operations


arr = np.array([1, 2, 3, 4])

# Addition
print("Add 5:", arr + 5)

# Subtraction
print("Subtract 2:", arr - 2)

# Multiplication
print("Multiply by 3:", arr * 3)

# Division
print("Divide by 2:", arr / 2)

# Exponentiation
print("Square each element:", arr  2)


'''
Output:

Add 5: [6 7 8 9]
Subtract 2: [-1  0  1  2]
Multiply by 3: [ 3  6  9 12]
Divide by 2: [0.5 1.  1.5 2. ]
Square each element: [ 1  4  9 16]


These are examples of element-wise arithmetic operations on a NumPy array.
'''

#### Statistical Operations


arr = np.array([1, 2, 3, 4, 5])

# Mean
print("Mean:", arr.mean())

# Sum
print("Sum:", arr.sum())

# Standard Deviation
print("Standard Deviation:", arr.std())

# Minimum and Maximum
print("Min:", arr.min())
print("Max:", arr.max())

# Index of Min and Max
print("Index of Min:", arr.argmin())
print("Index of Max:", arr.argmax())


'''
Output:

Mean: 3.0
Sum: 15
Standard Deviation: 1.4142135623730951
Min: 1
Max: 5
Index of Min: 0
Index of Max: 4


These are examples of common statistical operations on a NumPy array.
'''

#### Broadcasting


arr = np.array([1, 2, 3])
broadcasted_array = arr + np.array([10])
print("Broadcasted Array:", broadcasted_array)


'''
Output:

Broadcasted Array: [11 12 13]


Broadcasting allows NumPy to perform operations on arrays of different shapes by expanding the smaller array.
'''


### 4. Indexing, Slicing, and Iterating

#### Indexing


arr = np.array([10, 20, 30, 40, 50])

# Accessing a single element
print("Element at index 2:", arr[2])

# Accessing elements with a boolean mask
mask = arr > 25
print("Elements greater than 25:", arr[mask])


'''
Output:

Element at index 2: 30
Elements greater than 25: [30 40 50]


This code demonstrates basic and boolean indexing in NumPy.
'''

#### Slicing


arr = np.array([10, 20, 30, 40, 50])

# Slice the array
print("Sliced Array [1:4]:", arr[1:4])

# Slice with a step
print("Sliced Array [::2]:", arr[::2])


'''
Output:

Sliced Array [1:4]: [20 30 40]
Sliced Array [::2]: [10 30 50]


Slicing allows you to access sub-arrays within a NumPy array.
'''

#### Iterating


arr = np.array([10, 20, 30])

for element in arr:
    print("Element:", element)


'''
Output:

Element: 10
Element: 20
Element: 30


This code iterates over each element in the array.
'''

### 5. Reshaping and Flattening

#### Reshaping


arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape to 3x2
reshaped_array = arr.reshape(3, 2)
print("Reshaped Array:\n", reshaped_array)


'''
Output:

Reshaped Array:
 [[1 2]
 [3 4]
 [5 6]]


This code reshapes a 2x3 array into a 3x2 array.
'''

#### Flattening


arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened_array = arr.flatten()
print("Flattened Array:", flattened_array)


'''
Output:

Flattened Array: [1 2 3 4 5 6]


Flattening converts a multi-dimensional array into a 1D array.
'''

### 6. Stacking and Splitting Arrays

#### Stacking


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical stacking
vstacked = np.vstack((arr1, arr2))
print("Vertically Stacked Array:\n", vstacked)

# Horizontal stacking
hstacked = np.hstack((arr1, arr2))
print("Horizontally Stacked Array:", hstacked)


'''
Output:

Vertically Stacked Array:
 [[1 2 3]
 [4 5 6]]
Horizontally Stacked Array: [1 2 3 4 5 6]


Stacking combines multiple arrays either vertically or horizontally.
'''

#### Splitting


arr = np.array([1, 2, 3, 4, 5, 6])

# Split into three arrays
split_array = np.split(arr, 3)
print("Split Arrays:", split_array)


'''
Output:

Split Arrays: [array([1, 2]),

 array([3, 4]), array([5, 6])]


Splitting divides an array into multiple sub-arrays.
'''

### 7. Advanced Functions

#### Vectorized Operations


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vectorized addition
result = np.add(arr1, arr2)
print("Vectorized Addition:", result)


'''
Output:

Vectorized Addition: [5 7 9]


Vectorized operations allow for efficient element-wise operations without explicit loops.
'''

#### Broadcasting


arr = np.array([1, 2, 3])

# Broadcasting a scalar addition
broadcasted_array = arr + 5
print("Broadcasted Addition:", broadcasted_array)


'''
Output:

Broadcasted Addition: [6 7 8]


Broadcasting automatically adjusts array shapes for element-wise operations.
'''

#### Advanced Indexing


arr = np.array([[1, 2], [3, 4], [5, 6]])

# Indexing with an array of indices
print("Advanced Indexing:", arr[[0, 1, 2], [1, 0, 1]])


'''
Output:

Advanced Indexing: [2 3 6]


Advanced indexing allows you to access specific elements using arrays of indices.
'''

### 8. Linear Algebra

#### Dot Product


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

dot_product = np.dot(arr1, arr2)
print("Dot Product:\n", dot_product)


'''
Output:

Dot Product:
 [[19 22]
 [43 50]]


The dot product is a key operation in linear algebra, combining rows and columns of matrices.
'''

#### Matrix Inversion


arr = np.array([[1, 2], [3, 4]])

# Calculate the inverse of the matrix
inverse_matrix = np.linalg.inv(arr)
print("Inverse Matrix:\n", inverse_matrix)


'''
Output:

Inverse Matrix:
 [[-2.   1. ]
 [ 1.5 -0.5]]


Matrix inversion is another fundamental operation, used in solving linear systems.
'''

#### Eigenvalues and Eigenvectors


arr = np.array([[1, 2], [3, 4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(arr)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


'''
Output:

Eigenvalues: [-0.37228132  5.37228132]
Eigenvectors:
 [[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]


Eigenvalues and eigenvectors are important in understanding matrix transformations.
'''

### 9. Random Numbers

#### Generating Random Numbers


# Random integers
random_integers = np.random.randint(1, 10, size=5)
print("Random Integers:", random_integers)

# Random floats
random_floats = np.random.rand(5)
print("Random Floats:", random_floats)

# Random normal distribution
random_normal = np.random.randn(5)
print("Random Normal Distribution:", random_normal)


'''
Output:

Random Integers: [7 2 8 3 4]
Random Floats: [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]
Random Normal Distribution: [-0.97727788  0.95008842 -0.15135721 -0.10321885  0.4105985 ]


NumPy provides various methods to generate random numbers, which can be used in simulations, sampling, etc.
'''

#### Random Permutations


arr = np.array([1, 2, 3, 4, 5])

# Shuffle the array
np.random.shuffle(arr)
print("Shuffled Array:", arr)


'''
Output:

Shuffled Array: [5 1 4 3 2]


Shuffling and permutations are useful in scenarios like bootstrapping and cross-validation.
'''

## Example DataFrame
'''
Let's say you have the following DataFrame:
'''

import pandas as pd
import numpy as np

# Sample data
data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'BMW', 'Chevrolet'],
    'Model': ['Camry', 'Civic', 'Focus', '3 Series', 'Malibu'],
    'Segment': ['Sedan', 'Sedan', 'Sedan', 'Luxury', 'SUV'],
    'Price': [np.nan, 8000, 5500, np.nan, 6500]
}

# Create a DataFrame
df = pd.DataFrame(data)
