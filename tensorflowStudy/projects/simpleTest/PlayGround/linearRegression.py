import tensorflow as tf
import numpy as np

x_data = np.random.random((2, 100))
y_data = np.dot([0.1, 0.2], x_data) + 0.3

b = tf.Variable(tf.zeros((1)),name='bbbbbb')
W = tf.Variable(tf.random_uniform((1,2),-1.0, 1.0),name='W')
y = tf.matmul(W, np.float32(x_data)) + b

loss = tf.reduce_mean(tf.square(y-y_data),name='loss')
optimizer = tf.train.GradientDescentOptimizer(0.5,name='optimizer')
train = optimizer.minimize(loss,name='train')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./log', tf.get_default_graph())
    writer.close()
    for step in range(200):
        sess.run(train)
        if step % 20 ==0:
            print(step, sess.run(W),sess.run(b))
