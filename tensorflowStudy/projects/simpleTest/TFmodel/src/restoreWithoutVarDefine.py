import tensorflow as tf

saver = tf.train.import_meta_graph('../models/playground/model.ckpt.meta')
with tf.Session() as sess:
    saver.restore(sess, '../models/playground/model.ckpt')
    print(sess.run(tf.Graph.get_tensor_by_name(tf.get_default_graph(), 'add:0')))
