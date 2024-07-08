import tensorflow as tf

# Define two tensors
A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])

# Element-wise multiplication using tf.multiply()
C = tf.multiply(A, B)
print("Element-wise Multiplication Result:")
print(C.numpy())


import tensorflow as tf

# Define two matrices
A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])

# Matrix multiplication using tf.matmul()
C = tf.matmul(A, B)
print("Matrix Multiplication Result:")
print(C.numpy())
