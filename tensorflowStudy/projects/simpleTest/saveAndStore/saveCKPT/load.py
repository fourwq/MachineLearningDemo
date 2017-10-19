import  tensorflow as tf
import  numpy as np

W2 = tf.Variable(tf.truncated_normal([2,3]), dtype=tf.float32, name='W')
b = tf.Variable(tf.truncated_normal([1,3]), dtype=tf.float32, name='b')
saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, 'data/test.ckpt')
    print(sess.run(W2))
    print(sess.run(b))
