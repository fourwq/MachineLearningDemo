import input_data
import numpy as np
import tensorflow as tf


mnist = input_data.read_data_sets('./MNIST_data', one_hot=True)

print('train data size:', mnist.train.num_examples)
print('validate data size:', mnist.validation.num_examples)
print('test data size:', mnist.test.num_examples)
print('example train lable:\n', mnist.train.labels[0])

#print('example train data:', mnist.train.images[0])

image = mnist.train.images[0]

b = np.int16(image>0)

print(np.reshape(b, (28, 28)))


batch_size = 100
xs,ys = mnist.train.next_batch(batch_size)
print('xs shape: ', xs.shape)
print('ys shape: ', ys.shape)


####################################

global_step = tf.Variable(0) #保存当前训练的步数
learning_rate = 0.1 #原始的学习率
decay_step = 100 #表示经过多少步的训练优化，然后执行学习率衰减
decay_rate = 0.96 #表示衰减的系数
learning_rate = tf.train.exponential_decay(learning_rate, global_step,decay_step, decay_rate, staircase=True)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss=loss, global_step=global_step)

######################################
