FROM tensorflow/tensorflow:latest-gpu

RUN apt update \
    && apt install -y --no-install-recommends \
    git \
    && pip install --no-cache-dir\
    keras \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

