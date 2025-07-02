# 🛠️ ROS 2 Humble Installation Guide for Jetson Orin

This guide walks you through installing **ROS 2 Humble** with `colcon`, `ros-dev-tools`, and custom message creation support on Ubuntu (Jetson or PC).

---

## ✅ Prerequisites

```
sudo apt update && sudo apt install locales
```

```
sudo locale-gen en_US en_US.UTF-8
```

```
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
```

```
export LANG=en_US.UTF-8
```

Add ROS 2 APT Repository

```
sudo apt install software-properties-common
```

```
sudo add-apt-repository universe
```

```
sudo apt update && sudo apt install curl -y
```

```
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
```

```
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb" # If using Ubuntu derivates use $UBUNTU_CODENAME
```

```
sudo apt install /tmp/ros2-apt-source.deb
```

🚀 Install ROS 2 Humble

```
sudo apt update
```

```
sudo apt upgrade
```

```
sudo apt install -y ros-humble-desktop
```

```
sudo apt install -y ros-dev-tools python3-argcomplete
```

📜 Environment Setup

```
source /opt/ros/humble/setup.bash
```

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

```
source ~/.bashrc
```

🔨 Build Workspace

```
sudo apt install python3-colcon-common-extensions
```

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

```
sudo rosdep init
```

```
rosdep
```

## Create package and Build

```
cd src/
```

```
ros2 pkg create --build-type ament_python --license Apache-2.0
```

```
cd ..
```

```
rosdep install -i --from-path src --rosdistro humble -y
```

```
colcon build --symlink-install
```
```
colcon build --symlink-install --cmake-clean-cache
```

```
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
```

```
source ~/.bashrc
```
