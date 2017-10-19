import tensorflow as tf

reader = tf.train.NewCheckpointReader('data/test.ckpt')
all_variables = reader.get_variable_to_shape_map()

for variables_name in all_variables:
    print(variables_name, all_variables[variables_name])

print('W value: ', reader.get_tensor('W_1'))