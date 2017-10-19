import tensorflow as tf
import numpy as np
import input_data
import tensorFlowMNISTutil as util



#MNIST数据集相关的常数
INPUT_NODE = 784
OUTPUT_NODE = 10

#配置神经网络参数
LAYER1_NODE = 500

BATCH_SIZE = 100

LEARNING_RATE_BASE = 0.8

LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001

TRAINING_STEPS = 30000

MOVING_AVERAGE_DECAY = 0.99


def main(argv=None):
    mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
    util.train(mnist)
    return 1

if __name__=='__main__':
    tf.app.run()
