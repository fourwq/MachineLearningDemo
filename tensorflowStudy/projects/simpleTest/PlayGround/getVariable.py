import  tensorflow as tf

v2 = tf.Variable(tf.constant(1.0, shape=[3,3]), name='v')
v = tf.get_variable('v', shape=[3, 3], initializer=tf.constant_initializer(1.0))
v3 = tf.get_variable('v3', shape=[2,3], initializer=tf.random_uniform_initializer(1, 10))
v4 = tf.get_variable('v4', initializer=[[1, 2, 3,],[5, 6, 4],[9,8,7]])

sess  =  tf.Session()

sess.run(tf.global_variables_initializer())
print(v.name, sess.run(v))
print(v2.name, sess.run(v2))
print(v3.name, sess.run(v3))
print('argmax',sess.run(tf.argmax(v4, 0)))

with tf.variable_scope('s1'):
    v = tf.get_variable('v', [1], initializer=tf.constant_initializer(2.0))
    print(v.name)


with tf.variable_scope('s1', reuse=True):
    v = tf.get_variable('v',[1])
    v2 = tf.get_variable('v2',[1])
    print(v.name)


