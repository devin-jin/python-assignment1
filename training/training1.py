import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
x=tf.constant(4,shape=(3,3))
print(x)