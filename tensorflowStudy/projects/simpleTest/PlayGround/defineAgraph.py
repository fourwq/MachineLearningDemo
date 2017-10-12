#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:05:21 2017

@author: camera1
"""

import tensorflow as tf

#define a graph
graph = tf.Graph()
with graph.as_default():
    foo = tf.Variable(3,name='foo')
    bar = tf.Variable(2,name='bar')
    result = foo+bar
    initialize = tf.global_variables_initializer()

print(result)
#define a session
with tf.Session(graph = graph) as sess:
    sess.run(initialize)
    res  = sess.run(result)
print(res)