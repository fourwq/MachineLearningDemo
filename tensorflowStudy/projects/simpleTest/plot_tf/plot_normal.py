import tensorflow as tf
import math
from matplotlib import  pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D
import numpy as np
import  pylab as pl

NUM_X = 100
NUM_Y = 100


sess = tf.Session()

weights = tf.Variable(tf.random_normal([NUM_X, NUM_Y], stddev=1.0 / math.sqrt(float(NUM_X))), name='weights')

sess.run(tf.global_variables_initializer())

result = weights.eval(session=sess)

sess.close()

fig = plt.figure()
# ax = Axes3D(fig)
X = range(NUM_X)
Y = range(NUM_Y)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# ax.plot_surface(X, Y, result, rstride=1, cstride=1, cmap='rainbow')
bins = np.arange(-0.5, 0.5, 0.02)
pl.hist(np.reshape(result,(-1, 1)), bins, histtype='stepfilled')
plt.show()