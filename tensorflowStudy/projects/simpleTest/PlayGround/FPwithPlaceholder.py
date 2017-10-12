import  tensorflow as tf
import numpy as np

w1 = tf.Variable(tf.truncated_normal([2,3], stddev=1))
w2 = np.random.standard_normal((3, 1))

x = tf.placeholder(tf.float32, shape=(3,2), name='input')
a = tf.matmul(x, w1)
y = tf.matmul(a, np.float32(w2))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(y, feed_dict={x: [[0.5, 0.7],[0.1, 0.4],[5, 6]]}))
