import tensorflow as tf
import numpy as np
import pylab as pl

x = tf.constant(np.linspace(-4, 4, 200))
relu = tf.nn.relu(x)
simoid = tf.nn.sigmoid(x)
tanh = tf.nn.tanh(x)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    x_= sess.run(x)
    y_relu=sess.run(relu)
    y_sig = sess.run(simoid)
    y_tanh = sess.run(tanh)

print(x_)
pl.plot(x_, y_relu)
pl.plot(x_, y_sig)
pl.plot(x_, y_tanh)
pl.show()