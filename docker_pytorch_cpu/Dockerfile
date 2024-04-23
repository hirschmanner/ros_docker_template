ARG PYTORCH="2.0.1"
ARG PYTHON_VER="3.10.11"
ARG UBUNTU_VER="22.04"

FROM cnstark/pytorch:${PYTORCH}-py${PYTHON_VER}-ubuntu${UBUNTU_VER}

# Check here https://hub.docker.com/r/pytorch/pytorch/tags the available versions.
# e.g.: cnstark/pytorch:2.0.1-py3.10.11-ubuntu22.04

# Install opencv dependencies
RUN apt update 
RUN apt install -y ffmpeg libsm6 libxext6 libsm6 libxext6 libxrender-dev

RUN pip install open3d
RUN pip install opencv-python
RUN pip install opencv-contrib-python

RUN mkdir /my_scripts
COPY example.py /my_scripts/example.py

WORKDIR /my_scripts
CMD ["/bin/bash"]

