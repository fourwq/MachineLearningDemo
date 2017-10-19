import tensorflow as tf
import numpy as np

W2 = tf.get_variable('W', shape=[2, 3])
W = tf.Variable([[1, 1, 1], [2, 2, 2]], dtype=tf.float32, name='W')
b = tf.Variable([[0, 1, 2]], dtype=tf.float32, name='b')
c = tf.transpose(b)
y = tf.matmul(W, c)
d = c + 1
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(y))
    save_path = saver.save(sess, 'data/test.ckpt')
    saver.export_meta_graph('data/test.ckpt.meta.json', as_text=True)
    print(save_path)
    for vs in tf.global_variables():
        print(vs.name)
