# PersonDetection-RCNN-YOLO_COCODataset

This repository encapsulates the ROS workspace containing the necessary packages and program nodes to simulate a simple turtlebot3 and further performing SLAM on turtlebot3 whilst adding noise to wheel odometry sensor motion model and IMU sensor. It also includes the results folder containing images and videos of simulation of turtlebot3 for different situations and a documentation as part of my Internship with Arrow Electronics (eInfochips).

## Pre-requisites

The simulation requires the following libraries and packages to be installed

- [ROS2 (Foxy)](https://docs.ros.org/en/foxy/Installation.html)

- [turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)

- [robot_localization](http://docs.ros.org/en/noetic/api/robot_localization/html/index.html)

- [navigation2](https://navigation.ros.org/)

- [Python 3.6.x - Python 3.8.x](https://www.python.org/)



## Table of Contents

* [Cloning the repository](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#cloning-the-repository)
* [Installing required rosdep packages and dependencies](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#installing-required-rosdep-packages-and-dependencies)
* [Source the workspace and start up the turtlebot3 environment](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#source-the-workspace-and-start-up-the-turtlebot3-environment)
* [Starting up the robot_localization (ekf_filter node)](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#starting-up-the-robot_localization-ekf_filter-node)
* [Plotting a real-time graph of the odometry and filtered odometry output](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#plotting-a-real-time-graph-of-the-odometry-and-filtered-odometry-output)
* [Moving the turtlebot3 around in the gazebo world](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#moving-the-turtlebot3-around-in-the-gazebo-world)
* [Visualizing the output in Rviz](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#visualizing-the-output-in-rviz)
* [Adding noise to odometry motion model equation](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#adding-noise-to-odometry-motion-model-equation)
* [Adding bias to the IMU sensor of the turtlebot3](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#adding-bias-to-the-imu-sensor-of-the-turtlebot3--)
* [Performing SLAM using turtlebot3 with noisy odometry and noisy IMU values](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#performing-slam-using-turtlebot3-with-noisy-odometry-and-noisy-imu-values)
* [Autonomous Navigation of Turtlebot3 based on EKF output](https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3_ws#autonomous-navigation-of-turtlebot3-based-on-ekf-output)

<br/>


## Cloning the repository

```
git clone https://github.com/AkshayLaddha943/Arrow_SensorFusion_turtlebot3
cd Arrow_SensorFusion_turtlebot3_ws
```


## Installing required rosdep packages and dependencies

```
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install <package_name>
#To build a specific package only
colcon build --symlink-install --packages-select <name-of-pkg>
```
