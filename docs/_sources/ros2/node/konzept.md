# Konzept

Ein ROS 2-Knoten (Node) ist eine zentrale Einheit in einem ROS 2-System und bildet die Grundlage für die verteilte Robotik-Softwareentwicklung. Hier sind die Schlüsselkonzepte, die das Konzept einer ROS 2-Node beschreiben:


Eine Node ist eine Kommunikationseinheit innerhalb eines ROS 2-Systems. Er ermöglicht die Kommunikation und den Datenaustausch zwischen verschiedenen Teilen des Roboters oder zwischen Robotern in einem Netzwerk.


Jede Node ist eine in sich geschlossene Einheit, die spezifische Aufgaben ausführt. Dies ermöglicht die Aufteilung großer Roboteranwendungen in kleinere, verwaltbare Einheiten, die unabhängig voneinander entwickelt, getestet und ausgeführt werden können.


Nodes sind modular aufgebaut, was bedeutet, dass Sie sie nach Bedarf erstellen, konfigurieren und austauschen können. Dies erleichtert die Wiederverwendung von Knoten und die Integration neuer Funktionen in ein bestehendes System.


Alle aktiven Nodes sind in einem ROS 2-Graph miteinander verbunden. Der Graph zeigt die Verbindungen zwischen Knoten, Topics und Services und ermöglicht eine einfache Übersicht über die Kommunikation in einem ROS 2-System.

```{image} ../../images/graph.gif
:alt: fishy
:class: bg-primary mb-1
:align: center
```
