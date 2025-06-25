# 🛠️ ROS 2 Humble Custom Message Guide for Jetson Orin

## 🧩 Create Custom ROS 2 Message

```
cd ~/ros2_ws/src
```

```
ros2 pkg create custom_msgs --build-type ament_cmake --dependencies std_msgs
```

```
cd custom_msgs
```

```
mkdir msg
```

```
nano msg/CustomMsg.msg
```

## CMakeLists.txt

Replace contents with:

```
cmake_minimum_required(VERSION 3.5)
project(custom_msgs)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CustomMsg.msg"
  DEPENDENCIES std_msgs
)

ament_package()
```

## Edit package.xml and ensure it includes these lines:

```
<buildtool_depend>ament_cmake</buildtool_depend>

<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<depend>std_msgs</depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
