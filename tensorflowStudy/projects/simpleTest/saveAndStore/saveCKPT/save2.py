import tensorflow as tf
import numpy as np

in_dim = 10
out_dim = 10
h1_dim = 5

input_x = tf.placeholder(tf.float32, shape=(None, in_dim), name='input_x')
input_y = tf.placeholder(tf.float32, shape=(None, out_dim), name='input_y')

w1 = tf.Variable(tf.truncated_normal((in_dim, h1_dim), stddev=0.1, name='w1'))
b1 = tf.Variable(tf.zeros(h1_dim, name='b1'))

w2 = tf.Variable(tf.zeros([h1_dim, out_dim]), name='w2')
b2 = tf.Variable(tf.zeros(out_dim),name='b2')

keep_prob = tf.placeholder(tf.float32, name='keep_prob')

hidden1 = tf.nn.relu(tf.matmul(input_x, w1)+b1)
hidden1_drop = tf.nn.dropout(hidden1, keep_prob)

y = tf.nn.softmax(tf.matmul(hidden1_drop, w2)+b2)

saver = tf.train.Saver()
tf.add_to_collection('pred_network', y)

sess = tf.Session()
for step in range(1000):
    sess.run(train_op)
    if step %100==0:
        saver.save(sess, 'data2/test', global_step=step)
