import tensorflow as tf


sess = tf.Session()
# 定义一个1张图，size 3X3,5个通道的输入图像，对应shape为【1，3，3，5】
input = tf.Variable(tf.random_normal([1, 3, 3, 5]))
input2 = tf.Variable(tf.random_normal([1, 5, 5, 5]))

filter  = tf.Variable(tf.random_normal([1, 1, 5, 1]))
filter2 = tf.Variable(tf.random_normal([3, 3, 5, 2]))


op = tf.nn.conv2d(input2, filter2, strides=[1, 1, 1, 1], padding='SAME')

sess.run(tf.global_variables_initializer())

result = sess.run(op)

print(result)
print(filter2.value())

writer = tf.summary.FileWriter('./log', tf.get_default_graph())
writer.close()

sess.close()