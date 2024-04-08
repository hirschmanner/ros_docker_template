FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    python3-catkin-tools python3-osrf-pycommon python3-tk python3-pip tmux nano git clang-tidy clang-format
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /catkin_ws
RUN echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc
RUN mkdir -p src
RUN /bin/bash -c 'source /opt/ros/noetic/setup.bash && catkin_make'
RUN echo 'source /catkin_ws/devel/setup.bash' >> ~/.bashrc

WORKDIR /catkin_ws
CMD ["/bin/bash"]

