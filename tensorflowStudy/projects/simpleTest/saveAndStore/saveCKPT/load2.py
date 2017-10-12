import tensorflow as tf
import numpy as np

with tf.Session() as sess:
    new_saver = tf.train.import_meta_graph('./data2/test.ckpt.meta')
    new_saver.restore(sess, './data2/test.ckpt')
    y = tf.get_collection('pred_network')[0]
    graph = tf.get_default_graph()
    input_x = graph.get_operation_by_name('input_x').outputs[0]
    keep_prob = graph.get_operation_by_name('keep_prob').outputs[0]

    sess.run(y, feed_dict={input_x: ..., keep_prob: ...})