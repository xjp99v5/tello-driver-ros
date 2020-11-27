# Tello ROS driver 

ROS driver used in the course DTEK0081 Perception and Navigation in Robotics

## Installation

We will use by default the same workspace as for the drone-racing repo: [https://github.com/TIERS/drone-racing](https://github.com/TIERS/drone-racing).

If you don't have it, create the workspace and clone this repo
```
mkdir -p  ~/drone_racing_ws/src && cd ~/drone_racing_ws/src
git clone --recursive https://github.com/TIERS/tello-driver-ros.git
```

Instanll dependency
```
sudo apt install ros-melodic-camera-info-manager-py ros-melodic-codec-image-transport python-catkin-tools
sudo -H pip3 install --upgrade pip
sudo -H pip3 install https://github.com/damiafuentes/DJITelloPy/archive/master.zip
```

And build it
```
catkin init
catkin build
```

## Launch for Tello with its own Wi-Fi AP

- Turn on Tello drone
- Connect to drone's WiFi access point (`TELLO_XXXXXX`)

Then launch the driver
```
source ~/drone_racing_ws/devel/setup.bash
roslaunch tello_driver tello_node.launch tello_ip:="192.168.10.1"
```

You can control it with the `teleop_twist_keyboard` node. Install it with
```
sudo apt install ros-melodic-teleop-twist-keyboard
```

and run it
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/tello/cmd_vel
```

## Launch for Tello Edo connected to same Wi-Fi network

- Turn on Tello EDU drone
- Check IP (for the course, they are written on top of the drone)

Then launch the driver modifying the IP
```
source ~/drone_racing_ws/devel/setup.bash
roslaunch tello_driver tello_node.launch tello_ip:="192.168.XXX.XXX"
```


## ROS Nodes

### Subscribed topics
* ```/tello/cmd_vel``` [geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
* ```/tello/emergency``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/fast_mode``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/flattrim``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/flip``` [std_msgs/Uint8](http://docs.ros.org/api/std_msgs/html/msg/UInt8.html)
* ```/tello/land``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/palm_land``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/manual_takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)
* ```/tello/throw_takeoff``` [std_msgs/Empty](http://docs.ros.org/api/std_msgs/html/msg/Empty.html)

### Published topics
* ```/tello/camera/camera_info``` [sensor_msgs/CameraInfo](http://docs.ros.org/api/sensor_msgs/html/msg/CameraInfo.html)
* ```/tello/image_raw``` [sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
* ```/tello/imag/raw/h264``` [h264_image_transport/H264Packet](https://github.com/tilk/h264_image_transport/blob/master/msg/H264Packet.msg)
* ```/tello/odom``` [nav_msgs/Odometry](http://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)
* ```/tello/imu``` [sensor_msgs/Imu](http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html)
* ```/tello/status``` [tello_driver/TelloStatus](https://github.com/appie-17/tello_driver/blob/development/msg/TelloStatus.msg)

### Parameters
* ```~/tello_driver_node/connect_timeout_sec```
* ```~/tello_driver_node/fixed_video_rate```
* ```~/tello_driver_node/local_cmd_client_port```
* ```~/tello_driver_node/local_vid_server_port```
* ```~/tello_driver_node/stream_h264_video```
* ```~/tello_driver_node/tello_cmd_server_port```
* ```~/tello_driver_node/tello_ip```
* ```~/tello_driver_node/vel_cmd_scale```
* ```~/tello_driver_node/video_req_sps_hz```
* ```~/tello_driver_node/altitude_limit```
* ```~/tello_driver_node/attitude_limit```
* ```~/tello_driver_node/low_bat_threshold```


## Contact

For any questions, write to `jopequ@utu.fi`.

Visit us at [https://tiers.utu.fi](https://tiers.utu.fi)
