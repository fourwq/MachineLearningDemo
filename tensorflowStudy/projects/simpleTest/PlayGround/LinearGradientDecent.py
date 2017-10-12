import tensorflow as tf
import numpy as np

x_data = np.float32(np.random.rand(2, 100))

y_data = np.dot([0.1, 0.2], x_data) +0.3

b = tf.Variable(tf.zeros([1]))

W = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))

y = tf.matmul(W, x_data) + b

loss = tf.reduce_mean(tf.square(y - y_data))

# 这里只是定义了一步的梯度下降操作，而不是直接执行到最优值。
optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

for step in range(200):
    sess.run(train)

    print(W.eval(session=sess), b.eval(session=sess))

