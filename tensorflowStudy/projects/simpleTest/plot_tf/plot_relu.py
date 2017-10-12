import tensorflow as tf
import  numpy as np
import pylab as pl




data_x = np.arange(-5, 5, 0.01)
# data_y = data_x**2
# pl.plot(data_x, data_y)
#
#
# pl.plot(data_x, data_x)
# pl.show()

sess = tf.Session()

x = tf.Variable(data_x)
y = tf.nn.relu(x)

sess.run(tf.global_variables_initializer())
result = sess.run(y)
sess.close()
pl.plot(data_x, data_x)
pl.plot(data_x, result)
pl.show()