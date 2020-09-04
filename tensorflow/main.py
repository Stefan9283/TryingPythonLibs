
import tensorflow as tf

print("TF works")
# tf.test.is_built_with_cuda()

string = tf.Variable("this is a string", tf.string)
print(string.shape)     # tf.Tensor(0, shape=(), dtype=int32)
print(tf.rank(string))  # 0


matrix = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

ones = tf.ones([3, 3, 3])

print(69*ones)

ones = tf.reshape(ones, [3, -1])

print(ones)


# print(tf.version)
