import tensorflow as tf
v = tf.Variable(0, dtype=tf.float32, name='v')

ema = tf.train.ExponentialMovingAverage(0.9)


print('ema',ema.variables_to_restore())
y= tf.Variable(0, dtype=tf.float32, name='y')
print('ema',ema.variables_to_restore())
saver = tf.train.Saver(ema.variables_to_restore())

for i in tf.global_variables():
    print('with ema',i.name)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, 'data/modle.ckpt')
    print(sess.run(v))