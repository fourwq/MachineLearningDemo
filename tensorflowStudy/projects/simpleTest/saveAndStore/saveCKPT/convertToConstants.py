import tensorflow as tf
from tensorflow.python.framework import graph_util as gutil

v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result = v1 + v2

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    graph = tf.get_default_graph()
    graph_def = tf.Graph.as_graph_def(graph)
    output_graph_def = gutil.convert_variables_to_constants(sess, graph_def, ['add'])
    with tf.gfile.GFile('data/test.pb','wb') as f:
        f.write(output_graph_def.SerializeToString())