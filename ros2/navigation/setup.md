# Setup

## Nav2

Nav2 ist eine Sammlung an Paketen, die es uns erlaubt Navigation in unseren Robotern zu implementieren.

Nav2 besitzt beispielsweise Pakete um folgende Funktionalitäten umzusetzen:

- Laden, Speichern und zur verfügung Stellen von Karten
- Lokalisation
- Pfadplanung
- Konvertierung von Sensordaten zu einer Umgebungswelt

Um die **ros navigation** Pakete zu installieren müssen folgende Befehle ausgeführt werden:

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```

## Turtlebot3

Ein TurtleBot ist ein beliebter mobiler Roboter, der für Bildungs- und Forschungszwecke entwickelt wurde. Er besitzt zusätzlich grundlegende Sensoren, um seine Umwelt und seine Position festzustellen. 

Der folgende Befehl installiert Pakete, welche eine Simulation und Steuerung eines Turtlebots erlauben:

```bash
sudo apt install ros-humble-turtlebot3*
```

## SLAM

SLAM steht für **S**imultaneous **L**ocalization **a**nd **M**apping. Es bezeichnet ein Verfahren, bei dem ein Roboter gleichzeitig eine Karte seiner Umgebung schätzt und sich selbst in dieser verortet.

Für die Verwendung von SLAM in Nav2 muss folgendes Paket installiert werden:

```bash
sudo apt install ros-humble-slam-toolbox
```





