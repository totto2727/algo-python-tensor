# -*- coding: utf-8 -*-
"""algo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11xOPkh1EPz3U0xEPuktxdw0wUqqtpAmU
"""
import os
import time

import numpy as np
import tensorflow as tf
import keras.layers.advanced_activations as activations
from functools import partial


def main():
    x_train = np.array(
        [
            [
                0, 0, 1, 1, 0, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 0, 1, 1, 0, 0,
            ],
            [
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
            ],
            [
                0, 0, 1, 1, 0, 0,
                0, 1, 0, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
                0, 1, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 1, 1, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 1, 1, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 1, 0, 0,
                0, 1, 0, 1, 0, 0,
                1, 1, 1, 1, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 0, 0,
                0, 0, 1, 1, 0, 0,
                0, 0, 0, 0, 1, 0,
                0, 0, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 0, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 1, 1, 1, 1, 0,
                0, 0, 0, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
                0, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
            ]
        ]
    )
    y_train = tf.keras.utils.to_categorical(range(0, 10))

    x_test = np.array(
        [
            [
                0, 1, 1, 1, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 1, 0, 0, 1, 0,
                0, 0, 1, 1, 0, 0,
            ],
            [
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
            ],
            [
                0, 0, 1, 1, 0, 0,
                0, 1, 0, 0, 1, 0,
                1, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
                0, 1, 1, 1, 1, 1,
                0, 0, 0, 0, 0, 0,
            ],
            [
                1, 1, 1, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                1, 1, 1, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                1, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 0, 0, 0, 0,
                0, 0, 1, 1, 0, 0,
                0, 1, 0, 1, 0, 0,
                1, 1, 1, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 1,
                0, 0, 1, 0, 0, 0,
                0, 0, 1, 1, 0, 0,
                0, 0, 0, 0, 1, 0,
                0, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 1,
                0, 0, 1, 0, 0, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
                0, 1, 0, 0, 0, 0,
                1, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0,
            ],
            [
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 1, 0,
                0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 1, 0,
                0, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 0,
            ]
        ]
    )
    y_test = tf.keras.utils.to_categorical(range(0, 10))

    device_type = 'GPU'
    if device_type == 'GPU' and tf.config.list_physical_devices("GPU") != []:
        gpu_devices = tf.config.experimental.list_physical_devices('GPU')
        tf.config.experimental.set_memory_growth(gpu_devices[0], True)
    else :
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    print(tf.config.list_physical_devices())

    make_model_basic = partial(make_model, x=x_train, y=y_train, x_test=x_test, y_test=y_test, verbose=0)
    test_model_basic = partial(test_model, x=x_test, y=y_test)
    leaky_lamp = activations.LeakyReLU()

    start_time = time.time()

    '''sigmoid&sgd'''
    model_sigmoid = make_model_basic(activation='sigmoid')

    '''relu&sgd'''
    model_lamp = make_model_basic(activation=leaky_lamp)

    '''sigmoid&adam'''
    model_sigmoid_adam = make_model_basic(activation='sigmoid', optimizer='adam')

    '''lamp&adam'''
    model_lamp_adam = make_model_basic(activation=leaky_lamp, optimizer='adam')

    print('\nSigmoid&SGD')
    print(test_model_basic(model_sigmoid))
    print('\nLamp&SGD')
    print(test_model_basic(model_lamp))
    print('\nSigmoid&adam')
    print(test_model_basic(model_sigmoid_adam))
    print('\nLamp&adam')
    print(test_model_basic(model_lamp_adam))

    finish_time = time.time()
    print('\nexecution time', finish_time - start_time)


def make_model(x, y, activation, optimizer='SGD', verbose=0, x_test=None, y_test=None, metrics=None, loss=None):
    metrics = metrics if metrics is not None else ['categorical_accuracy']
    loss = loss if loss is not None else tf.keras.losses.CategoricalCrossentropy(from_logits=True)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation=activation, input_dim=36),
        tf.keras.layers.Dense(10, activation=activation)
    ])

    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=metrics
    )

    if x_test is not None:
        predictions = model(x_test).numpy()
        print("\npredictions\n", predictions)
        print("\npredictions probability\n", tf.nn.softmax(predictions).numpy())

        if y_test is not None:
            print("\ncategorical cross entropy\n", loss(y_test, predictions).numpy())

    print('fit start')
    print()
    model.fit(x, y, epochs=1000, verbose=verbose)
    print('fit finish')

    return model


def test_model(model, x, y=None):
    if y is not None:
        model.evaluate(x, y)

    results = model(x).numpy()
    maxes = results.max(axis=1).tolist()
    result_max_zip = zip(results.tolist(), maxes)

    return list(map(lambda z: z[0].index(z[1]), result_max_zip))


if __name__ == '__main__':
    main()
