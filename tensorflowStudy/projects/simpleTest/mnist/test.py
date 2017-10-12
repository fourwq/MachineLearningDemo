import input_data
import numpy as np


mnist = input_data.read_data_sets('./MNIST_data', one_hot=True)

print('train data size:', mnist.train.num_examples)
print('validate data size:', mnist.validation.num_examples)
print('test data size:', mnist.test.num_examples)
print('example train lable:\n', mnist.train.labels[0])

#print('example train data:', mnist.train.images[0])

image = mnist.train.images[0]

b = np.int16(image>0)

print(np.reshape(b, (28, 28)))


batch_size = 100
xs,ys = mnist.train.next_batch(batch_size)
print('xs shape: ', xs.shape)
print('ys shape: ', ys.shape)