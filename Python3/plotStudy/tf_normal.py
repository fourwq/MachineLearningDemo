import tensorflow as tf
import math

sess = tf.Session()

weights = tf.Variable(tf.truncated_normal([784, 100], stddev=1.0 / math.sqrt(float(784))), name='weights')

sess.run(tf.global_variables_initializer())

result = weights.eval()

sess.close()

