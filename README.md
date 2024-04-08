# ROS Docker Development Setup
## Setup
- [Install docker](https://docs.docker.com/get-docker/). I usually only install [Docker Engine with apt](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) with the [postinstall steps](https://docs.docker.com/engine/install/linux-postinstall).
- If you have an NVIDIA GPU, install the [NVIDIA Container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and configure it to use with Docker. 
- Clone this repo
- Use `bash download_example_projects.sh` to download some ROS Noetic examples packages into the `./projects` folder
- If you do not have an NVIDIA GPU, you need to remove the lines referencing NVIDIA in the docker-compose.yml file. 
- Use `docker compose build` in one of the docker folders depending on if you want to use CUDA or not 
- Use `docker compose run --name ros_noetic master` to create a new container from the image and enter the shell
- You can now use this shell like with a native ROS installation
- Start by building the workspace again with `catkin_make`
- Add other ROS noetic packages in the `./projects` folder for development
- When you close the container, you can start it again and attach to it with `docker start ros_noetic -a`
- You can attach Visual Studio Code to a running container using the Docker and Dev Containers extension [as shown here](https://code.visualstudio.com/docs/devcontainers/attach-container).

## Acknowledgment
This repository is based on the great work by [@hoenigpeter](https://github.com/hoenigpeter) here: [https://github.com/hoenigpeter/ros_docker](https://github.com/hoenigpeter/ros_docker)
