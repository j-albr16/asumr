# Node

Ein ROS2-Knoten (Node) ist eine zentrale Einheit in einem ROS2-System und bildet die Grundlage für die verteilte Robotik-Softwareentwicklung. Hier sind die Schlüsselkonzepte, die das Konzept einer ROS2-Node beschreiben:

## Kommunikationseinheit

Ein Node ermöglicht die Kommunikation und den Datenaustausch zwischen verschiedenen Teilen eines Roboters oder zwischen Robotern in einem Netzwerk innerhalb eines ROS2-Systems.

## In sich geschlossene Einheit

Jeder Node führt spezifische Aufgaben aus und ist eine eigenständige, in sich geschlossene Einheit. Diese Modularität erleichtert die Aufteilung großer Roboteranwendungen in kleinere, verwaltbare Einheiten, die unabhängig voneinander entwickelt, getestet und ausgeführt werden können.

## Modularität

Nodes sind modular aufgebaut, was bedeutet, dass sie nach Bedarf erstellt, konfiguriert und ausgetauscht werden können. Dies erleichtert die Wiederverwendung von Knoten und die Integration neuer Funktionen in ein bestehendes System.

## ROS2-Graph

Alle aktiven Nodes sind in einem ROS2-Graph miteinander verbunden. Dieser Graph visualisiert die Verbindungen zwischen Knoten, Topics und Services und bietet eine einfache Übersicht über die Kommunikation in einem ROS2-System.

```{image} ../images/graph.gif
:alt: fishy
:class: bg-primary mb-1
:align: center
```
## Vertiefung

```{tableofcontents}
```








