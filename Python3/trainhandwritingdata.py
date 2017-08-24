#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:51:44 2017

@author: camera1
"""
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))

b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W)+b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#init_op = tf.initialize_all_variables()
init_op = tf.global_variables_initializer()

saver = tf.train.Saver()

sess = tf.Session()

sess.run(init_op)

for i in range(500):
    batch_xs, batch_ys = mnist.train.next_batch(1)
    sess.run(train_step, feed_dict = {x:batch_xs, y_: batch_ys})
    
save_path = saver.save(sess, "model1.ckpt")
print("Model saved in file: ", save_path)