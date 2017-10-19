import tensorflow as tf

saver = tf.train.import_meta_graph('data/test.ckpt.meta')

sess = tf.Session()

saver.restore(sess, 'data/test.ckpt')

graph = tf.get_default_graph()

print(sess.run(tf.get_default_graph().get_tensor_by_name('W:0')))
print(sess.run(tf.get_default_graph().get_tensor_by_name('b:0')))