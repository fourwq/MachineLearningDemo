import time
import tensorflow as tf
import sys
sys.path.append('..')
import input_data

import mnist_inference
import mnist_train

EVAL_INTERVAL_SECS = 10

def evaluate(mnist):
    with tf.Graph.as_default(tf.get_default_graph()) as g:
        x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.int64, name='y-input')
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}
        test_feed = {x:mnist.test.images,
                     y_:mnist.test.labels}

        y = mnist_inference.inference(x, None)
        correct_prediction = tf.equal(tf.argmax(y,1), y_)
        accuracy  =tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        variable_average = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_average.variables_to_restore()
        saver = tf.train.Saver()
        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print('after %s training steps, validation accuracy=%g'%(global_step, accuracy_score))
                    test_accuracy_score = sess.run(accuracy, feed_dict=test_feed)
                    print('after %s training steps, test accuracy=%g' % (global_step, test_accuracy_score))
                else:
                    print('no checkpoint file found')
                    return
            time.sleep(EVAL_INTERVAL_SECS)

def main(argv=None):
    mnist = input_data.read_data_sets('../MNIST_data')
    evaluate(mnist)
    return 1

if __name__ == '__main__':
    tf.app.run()