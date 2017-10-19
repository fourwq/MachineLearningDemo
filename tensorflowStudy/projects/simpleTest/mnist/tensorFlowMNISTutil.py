import tensorflow as tf
import tensorFlowMNIST as master


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    if avg_class is None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        result = tf.matmul(layer1, weights2) + biases2
        return result
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        result = tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)
        return result


def train(mnist):
    x = tf.placeholder(tf.float32, [None, master.INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, master.OUTPUT_NODE], name='y-input')

    weights1 = tf.Variable(tf.truncated_normal((master.INPUT_NODE, master.LAYER1_NODE), stddev=0.1))
    weights2 = tf.Variable(tf.truncated_normal((master.LAYER1_NODE, master.OUTPUT_NODE), stddev=0.1))
    bias1 = tf.Variable(tf.constant(0.1, shape=[1, master.LAYER1_NODE]))
    bias2 = tf.Variable(tf.constant(0.1, shape=[1, master.OUTPUT_NODE]))

    y = inference(x, None, weights1, bias1, weights2, bias2)
    global_step = tf.Variable(0, trainable=False)
    variable_averages = tf.train.ExponentialMovingAverage(master.MOVING_AVERAGE_DECAY, global_step)
    variables_average_op = variable_averages.apply(tf.trainable_variables())

    average_y = inference(x, variable_averages, weights1, bias1, weights2, bias2)

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,
                                                                   labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularization = master.REGULARIZATION_RATE * (tf.nn.l2_loss(weights1) + tf.nn.l2_loss(weights2))

    loss = cross_entropy_mean + regularization

    learning_rate = tf.train.exponential_decay(master.LEARNING_RATE_BASE,
                                               global_step,
                                               mnist.train.num_examples / master.BATCH_SIZE,
                                               master.LEARNING_RATE_DECAY)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    with tf.control_dependencies([train_step, variables_average_op]):
        train_op = tf.no_op(name='train')

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}

        for i in range(master.TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print('after %d training steps, validation accuracy use average model is %g' % (i, validate_acc))
            xs, ys = mnist.train.next_batch(master.BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print('after %d training steps, test accuracy use average model is %g' % (master.TRAINING_STEPS, test_acc))
