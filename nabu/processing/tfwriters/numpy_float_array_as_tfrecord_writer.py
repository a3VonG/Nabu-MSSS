'''@file numpy_float_array_as_tfrecord_writer.py
contains the NumpyFloatArrayAsTfrecordWriter class'''

import numpy as np
import tensorflow as tf
import tfwriter

class NumpyFloatArrayAsTfrecordWriter(tfwriter.TfWriter):
    '''a TfWriter to write numpy float arrays'''

    def _get_example(self, data):
        '''write data to a file

        Args:
            data: the data to be written'''

        shape_feature = tf.train.Feature(bytes_list=tf.train.BytesList(
            value=[np.array(data.astype(np.int32).shape).tostring()]))
        data_feature = tf.train.Feature(bytes_list=tf.train.BytesList(
            value=[data.reshape([-1]).astype(np.float32).tostring()]))


        #create the example proto
        example = tf.train.Example(features=tf.train.Features(feature={
            'shape': shape_feature,
            'data': data_feature}))

        return example
