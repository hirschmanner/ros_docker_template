# Pytorch-CPU only version Docker Development Environment

Development Environment with Ubuntu 22.04 with CUDA, Pytorch and other standard computer vision libraries.

- Follow the instructions to build the image and run a container from the main `README`.
- The folder contains a python script you can execute to make sure all the packages are installed correctly. It will be copied in the directory `my_scripts` inside the docker image.
- You can change the `PYTORCH`, `PYTHON_VER`, `UBUNTU_VER` arguments to use different versions by either editing them directly in the `Dockerfile` or add the following `args` entry under the build configurations in the `docker-compose.yml` file:


        build:
            ...
            args:
                PYTORCH: "1.9.0"  # Examples of overriding default ARG values
                PYTHON_VER: "3.8"
                UBUNTU_VER: "20.04"



