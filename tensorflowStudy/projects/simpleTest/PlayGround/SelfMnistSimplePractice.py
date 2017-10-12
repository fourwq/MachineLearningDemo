import  tensorflow as tf
import sys
sys.path.append("..")
import mnist.input_data as input_data

mnist = input_data.read_data_sets('../mnist/MNIST_data/', one_hot=True)

# 定义节点，输出特征数据集
x = tf.placeholder(tf.float32, [None, 784])

# 定义节点，输出标签数据
y_ = tf.placeholder(tf.float32, [None, 10])

# 定义变量，存放权重数据
W = tf.Variable(tf.zeros([784, 10]))

# 定义变量，存放偏置数据
b = tf.Variable(tf.zeros([10]))

# 定义变量，设定假设函数，保存预测结果
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 使用较差熵定义损失函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices=[1]))

# 寻找最优值
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(cross_entropy)

# 初始化所有的变量
init = tf.global_variables_initializer();

sess = tf.Session()
sess.run(init)
for i in range(1000):
    (batch_xs, batch_ys) = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

sess.close()
