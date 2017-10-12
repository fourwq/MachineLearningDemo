import tensorflow as tf
import time
from mnist import input_data

mnist = input_data.read_data_sets('../mnist/MNIST_data/', one_hot=True)

start_time = time.time()

def weight_variable(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1), name='weight')


def bias_variable(shape):
    return tf.Variable(tf.constant(0.1, shape=shape),name='bias')


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME',name='conv2d')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='max_pool')


# 定义数据
input_x = tf.placeholder('float', shape=[None, 784],name='input_x')
input_y = tf.placeholder('float', shape=[None, 10],name='input_y')

# 第一层，卷积层
L1 = {
    'x': tf.reshape(input_x, [-1, 28, 28, 1],name='reshape28x28'),
    'w': weight_variable([5, 5, 1, 32]),
    'b': bias_variable([32])
}
L1_output = tf.nn.relu(conv2d(L1['x'], L1['w']) + L1['b'],name='relu')

# 第二层， 池化层

L2_pool_output = max_pool_2x2(L1_output)

# 第三层 卷积层
L3 = {
    'x': L2_pool_output,
    'W': weight_variable([5, 5, 32, 64]),
    'b': bias_variable([64])
}
L3_output = tf.nn.relu(conv2d(L3['x'], L3['W']) + L3['b'],name='relu')

# 第四层 池化层
L4_pool_output = max_pool_2x2(L3_output)

# 第五层，全连接层
L5 = {
    'x': tf.reshape(L4_pool_output, [-1, 7 * 7 * 64],name='reshape7x7x64'),
    'W': weight_variable([7 * 7 * 64, 1024]),
    'b': bias_variable([1024])
}
L5_output = tf.nn.relu(tf.matmul(L5['x'], L5['W']) + L5['b'],name='relu')

# dropout
keep_prob = tf.placeholder('float',name='keepProb')

dropout_output = tf.nn.dropout(L5_output, keep_prob,name='dropout')

# 第六层， 输出层
L6 = {
    'x': dropout_output,
    'W': weight_variable([1024, 10]),
    'b': bias_variable([10])
}
predict_y = tf.nn.softmax(tf.matmul(L6['x'], L6['W']) + L6['b'],name='softmax')

# 训练

cross_entropy = -tf.reduce_sum(input_y * tf.log(predict_y),name='lossfunc')
train_step = tf.train.AdamOptimizer(1e-4,name='adam').minimize(cross_entropy,name='trainStep')
correct_prediction = tf.equal(tf.argmax(predict_y, 1), tf.argmax(input_y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'),name='accuracy')

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for i in range(200):
    batch = mnist.train.next_batch(100)
    if i % 20 == 0:
        train_accuracy = accuracy.eval(session=sess, feed_dict={input_x: batch[0], input_y: batch[1], keep_prob: 1.0})
        print('step: %d, training accuracy: %g' % (i, train_accuracy))
    sess.run(train_step, feed_dict={input_x: batch[0], input_y: batch[1], keep_prob: 0.5})

print("test accuracy : %g" % (accuracy.eval(session=sess, feed_dict={input_x: mnist.test.images,
                                                                     input_y: mnist.test.labels,
                                                                     keep_prob: 1.0})))
writer = tf.summary.FileWriter('./log', tf.get_default_graph())
writer.close()

sess.close()

end_time = time.time()

print('cost time: %.3f' % (end_time - start_time))