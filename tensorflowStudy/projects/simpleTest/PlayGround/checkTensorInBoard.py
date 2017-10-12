import tensorflow as tf

# a = tf.constant([1, 2], name='a1')
# b = tf.constant([1, 2], name='b1')
#
# c = a+b
result=tf.constant([1, 2], name='a2')+tf.constant([1, 2], name='b1')

writer = tf.summary.FileWriter('./log', tf.get_default_graph())
writer.close()