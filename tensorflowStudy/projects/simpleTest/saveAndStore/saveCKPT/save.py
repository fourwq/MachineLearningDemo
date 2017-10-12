import tensorflow as tf
import numpy as np

W = tf.Variable([[1,1,1],[2,2,2]], dtype=tf.float32, name='W')
b = tf.Variable([[0, 1, 2]], dtype=tf.float32, name='b')
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    save_path = saver.save(sess, 'data/test.ckpt')
    print(save_path)