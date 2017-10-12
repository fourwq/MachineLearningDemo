import tensorflow as tf
import numpy as np

# w1 = tf.Variable(tf.random_normal((2,3),stddev=1, seed=1))
# w2 = tf.Variable(tf.random_normal((3,1),stddev=1, seed=1))

w1 = np.random.standard_normal((2,3))
w2 = np.random.standard_normal((3,1))


x = tf.constant([[0.7, 0.9]])

a = tf.matmul(x, np.float32(w1))
y = tf.matmul(a, np.float32(w2))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(y))
