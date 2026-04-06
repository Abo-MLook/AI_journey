import tensorflow as tf
import numpy
#Tensors : ML generalization of vectors and matrices to any number of dimensions
#Tensors created with a wrapper ,also it is built from C++

#tf.Variable
#tf.constant
#tf.placeholder
#tf.SparseTensor
#Most widely-used is tf.Variable, which we'll use here.
#As with TF tensors, in PyTorch we can similarly perform operations,
# and we can easily convert to and from NumPy arrays.

x_tf = tf.Variable(25, dtype=tf.int16) # dtype is optional
print(x_tf)
y_tf = tf.Variable(3, dtype=tf.int16)
print(x_tf + y_tf)
tf_sum = tf.add(x_tf,y_tf)
tf_sum = tf_sum.numpy() # note that NumPy operations automatically convert tensors to NumPy arrays, and vice versa
print(tf_sum)