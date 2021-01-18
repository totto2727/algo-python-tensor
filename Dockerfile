FROM tensorflow/tensorflow:latest-gpu

RUN pip install -U pip \
    && pip install keras