import tensorflow as tf

# 定义一个简单的计算图，实现向量的加法操作
# input1 = tf.constant([1.0, 2.0, 3.0], name='input1')
# input2 = tf.Variable(tf.random_uniform([3]), name='input2')
# output = tf.add_n([input1, input2], name='add')

# 生成一个写日志的writer，并将当前的TensorFlow计算图写入日志。TensorFlow提供了多种
# 写日志文件的API， 在后面有介绍。
const = tf.constant(1.0, name='const')

foo = tf.Variable(3, name='foo')
bar = tf.Variable(2, name='bar')
result = foo + bar
initialize = tf.global_variables_initializer()
print(result)
print(tf.Graph.as_graph_def(tf.get_default_graph()))

with tf.Session() as sess:
    sess.run(initialize)
    res = sess.run(result)
print(res)
writer = tf.summary.FileWriter('./log', tf.get_default_graph())
writer.close()
