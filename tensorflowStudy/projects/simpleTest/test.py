import tensorflow as tf
import numpy as np

a = tf.constant(np.arange(5), dtype=tf.float32,name='a')
a1= tf.range(5,dtype=tf.float32)
b = tf.constant(np.arange(5),dtype=tf.float32, name='b')
c = tf.Variable(tf.ones((1, 5)),dtype=tf.float32)
c1 = tf.ones((1,5))
c = c+b+a

sess = tf.Session()

sess.run(tf.global_variables_initializer())
print(sess.run(a))
print(sess.run(a1))
sess.close()
