ARG PYTORCH="2.2.2"
ARG CUDA="12.1"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

# Check here https://hub.docker.com/r/pytorch/pytorch/tags the available versions.
# e.g.: pytorch/pytorch:2.2.2-cuda12.1-cudnn8-devel (this one comes with Ubuntu 22.04)

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

