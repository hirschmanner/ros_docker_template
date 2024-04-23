# ROS Docker Development Environment

Development Environment with Ubuntu 20.04 and ROS Noetic.

- Use `bash download_ros_example_projects.sh` in the parent directory to download some ROS Noetic examples packages into the `../projects` folder.
- Follow the instructions to build the image and run a container from the main `README`.
- When you are inside your container, you can build the workspace again with `catkin_make` (remember you can run `catkin_make` only from the `catkin_ws` directory and not from its subdirectories).
- You can add new ROS noetic packages in the `../projects` folder. Any change within that folder will be reflected within the Docker container, and vice versa, since it is mounted with read-write permissions.

