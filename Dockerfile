# Copyright (c) 2019, NVIDIA Corporation. All rights reserved.
#
# This work is made available under the Nvidia Source Code License-NC.
# To view a copy of this license, visit
# https://nvlabs.github.io/stylegan2/license.html

FROM ubuntu:18.04
USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y --no-install-recommends python3.6 python3-dev && apt-get clean
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

RUN pip3 install tensorflow==1.15.0
RUN pip3 install opencv-python
RUN pip3 install scikit-image
RUN pip3 install tqdm

RUN pip3 install pyyaml==5.4.1
RUN pip3 install oyaml


ENV TARGET_CHIP="GAP8"
ENV PYTHONIOENCODING=utf-8

COPY . /home

WORKDIR "/home"
CMD ["python3", "RunCheckerTest.py"]