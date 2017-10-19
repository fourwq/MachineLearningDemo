import tensorflow as tf

v = tf.Variable(0, dtype=tf.float32, name='v')
for i in tf.global_variables():
    print(i.name)
ema = tf.train.ExponentialMovingAverage(0.8)
maintain_average_op = ema.apply(tf.global_variables())


for i in tf.global_variables():
    print('with ema',i.name)

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.assign(v, 10))
    sess.run(maintain_average_op)
    saver.save(sess,'data/modle.ckpt')
    print(sess.run([v, ema.average(v)]))
