import  tensorflow as tf
import  os

v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result = v1 + v2

saver = tf.train.Saver()

with tf.Session() as sess:
    print(os.getcwd())
    saver.restore(sess, '../models/playground/model.ckpt')
    print(sess.run(result))

