""" _shared_model.py_ FL Implementation """

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, GRU, Bidirectional, Dropout, Dense, ConvLSTM2D, Conv2D, Reshape, Conv1D
from tensorflow.keras.optimizers import Adam, SGD

