# Linux

# Version

Dies ist eine Installationsanleitung für ROS2 Iron für Ubuntu 22.04 LTS (Jammy)


Diese Anleitung basiert auf der Offiziellen [Installationsanleitung von ROS2 Iron für Ubuntu](https://docs.ros.org/en/iron/Installation/Ubuntu-Install-Debians.html)


# Installation


## Setze Locales

Überprüfe deine Locales ob `UTF-8` untersützt wird

```bash
locale
```

wenn nicht führe Folgende Befehle aus:

```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

Überprüfe mit:

```bash
locale
```


## Aktivierung des Repositorys


To enable the ROS2 Repository

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

füge ROS2 GPG key hinzu

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Füge repo zur source list hinzu

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```


## Installation von ROS2


Installation von Updates

```bash
sudo apt update
sudo apt upgrade
```

Installation

```bash
sudo apt install ros-iron-desktop
```



# Überprüfung der Installation

In der 1. Terminal Instanz

```bash
. /opt/ros/iron/setup.bash
ros2 run demo_nodes_ccp talker
```

In der 2. Terminal Instanz

```bash
. /opt/ros/iron/setup.bash
ros2 run demo_nodes_ccp listener
```


# Turtlesim

## Installation


```bash
sudo apt install ros-iron-turtlesim
```

Überprüfe, dass das Turterlism Paket ist installiert:

```bash
ros2 pkg executables turtlesim
```

Folgendes sollte die Ausgabe sein:

```
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

## Ausführung

```bash
ros2 run turtlesim turtlesim_node
```

## Benutzung

```bash
ros2 run turtlesim turtle_teleop_key
```

nun kann man die turtle mit den Pfeiltasten steuern


# RQT

```bash
sudo apt update
sudo apt install ~nros-iron-rqt*
```











