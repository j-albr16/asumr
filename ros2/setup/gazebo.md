# Gazebo

In dieser Veranstaltung arbeiten wir mit GazeboSim, einer Simulationsumgebung, um unseren Code jederzeit zumindest an einem virtuellen Roboter testen zu können.

Mit der folgenden Anleitung gehen wir sicher, dass sowohl die aktuelle Version von Gazebo verfügbar ist, wie auch die Brückensoftware, über die Gazebo und ROS2 kommunizieren. 

Auch hier hält sich die folgende Installationsanleitung weitgehend an die englische [Vorlage](https://gazebosim.org/docs/harmonic/install).

## Installation unter Ubuntu

Die Harmonic-Binärdateien sind für Ubuntu Jammy (22.04) und Ubuntu 24.04 (wenn es veröffentlicht wird) verfügbar. Die Harmonic-Binärdateien werden im Repository `packages.osrfoundation.org` gehostet. Um alle von ihnen zu installieren, kann das Metapaket `gz-harmonic` installiert werden.

Installiere zunächst einige erforderliche Tools:

```bash
sudo apt update
sudo apt install lsb-release wget gnupg
```

Dann installiere Gazebo Harmonic:


```bash
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install gz-harmonic
```

Alle Bibliotheken sollten einsatzbereit sein und die `gz sim`-Anwendung sollte ausgeführt werden können.

# `ros_gz_bridge`

ROS bietet eine umfangreiche Sammlung von Werkzeugen und Bibliotheken für die Entwicklung von Roboteranwendungen, während Gazebo eine Simulationsumgebung für Robotik und Robotersysteme bereitstellt. Die ROS-Gazebo-Brücke (`ros_gz_bridge`) ist eine wichtige Komponente, die es ermöglicht, eine nahtlose Kommunikation zwischen ROS und Gazebo herzustellen.

Die ROS-Gazebo-Brücke fungiert als Vermittler zwischen ROS und Gazebo, indem sie die Übertragung von Steuerbefehlen, Sensorinformationen und anderen Daten zwischen den beiden Plattformen ermöglicht. Dies erleichtert die Entwicklung, Tests und Validierung von unter anderem Steuerungs- und Wahrnehmungsalgorithmen von Robotersystemen in einer simulierten Umgebung, bevor sie auf physischen Robotern eingesetzt werden.

## Installation der Brücke

TODO: Muss das überhaupt installiert werden - Macht Gazebo Sim Sinn?
