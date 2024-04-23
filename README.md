# Example Docker Development Environments Setup
## Setup
- [Install Docker](https://docs.docker.com/get-docker/). You can directly install [Docker Engine with apt](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) with the [postinstall steps](https://docs.docker.com/engine/install/linux-postinstall). Make sure to then install the [Compose plugin](https://docs.docker.com/compose/install/linux/#install-using-the-repository).
- If you have an NVIDIA GPU, install the [NVIDIA Container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and configure it to use with Docker. 
- Clone this repo.
- Each folder in this repo contains a Docker example development environment that you can edit as you see fit for your own projects. Each of them contains a `Dockerfile` and a `docker-compose.yaml` file. 
- If you do not have an NVIDIA GPU, you need to remove the lines referencing NVIDIA in the docker-compose.yml file. 

To start using one of the provided Docker development environments you should:

- Use `docker compose build` in the chosen folder to build the Docker image from the Dockerfile.
- Use `xhost +local:docker` to grant permission for the GUI applications running inside the Docker containers to use the host's display for rendering their GUIs (mounting the `/tmp/.X11-unix:/tmp/.X11-unix:rw` volume and passing the `DISPLAY` environment variable in the docker compose file are crucial for this step to work).  
- Use `docker compose run --name your_container_name master` to create a new container from the image and enter the shell.
- You can now use this shell as you would with a native Ubuntu installation.
- When you close the container, you can start it again and attach to it with `docker start your_container_name -a`
- You can attach Visual Studio Code to a running container using the Docker and Dev Containers extension [as shown here](https://code.visualstudio.com/docs/devcontainers/attach-container).

## Acknowledgment
This repository is based on the great work by [@hoenigpeter](https://github.com/hoenigpeter) here: [https://github.com/hoenigpeter/ros_docker](https://github.com/hoenigpeter/ros_docker)
