# Topic

Ein ROS2 (Robot Operating System 2) _Topic_ (Thema) ist ein grundlegendes Kommunikationskonzept in ROS2, das dazu dient, Daten zwischen verschiedenen Komponenten eines Roboters oder einer Robotersystemarchitektur auszutauschen. ROS2 ist ein flexibles und modulares Framework zur Entwicklung von Robotersoftware, und _Topics_ sind eine wichtige Möglichkeit, um Informationen zwischen [_Nodes_](node.md) (Knoten) in einem ROS2-System zu übertragen.

Hier sind die wichtigsten Merkmale und Konzepte eines ROS2 _Topics_:

1. [**Nachrichten**](TODO):
   _Topics_ dienen dem Austausch von Nachrichten. Nachrichten sind Datenstrukturen, die Informationen übertragen. Sie können einfache Datentypen wie Zahlen oder komplexere Strukturen wie Sensorwerte, Bildinformationen oder Steuerbefehle enthalten. ROS2 unterstützt benutzerdefinierte Nachrichtentypen.

2. **Publisher und Subscriber**:
   Ein ROS2-System besteht aus _Nodes_, die _Publisher_ und/oder _Subscriber_ für verschiedene _Topics_ sein können. Ein _Publisher_ ist ein _Node_, der Nachrichten zu einem bestimmten _Topic_ sendet, während ein Subscriber ein _Node_ ist, der Nachrichten von diesem Topic empfängt.

3. **_Topic_-Namen**:
   Jedes _Topic_ hat einen eindeutigen Namen im ROS2-System. Dieser Name ermöglicht es Knoten, die Nachrichten austauschen möchten, das entsprechende _Topic_ zu identifizieren. Der Name folgt normalerweise einem bestimmten Namensschema, z.B., `/sensor_data` oder `/robot_status`.

4. **Nachrichten-Publizieren**:
   Ein Knoten, der Informationen bereitstellen möchte, erstellt einen _Publisher_ für ein bestimmtes _Topic_ und veröffentlicht Nachrichten auf diesem _Topic_. Andere Knoten können dann diese Nachrichten abrufen.

5. **Nachrichten-Abonnieren**:
   Ein Knoten, der Informationen benötigt, erstellt einen Subscriber für ein bestimmtes _Topic_ und abonniert dieses _Topic_. Wenn ein _Publisher_ Nachrichten auf diesem _Topic_ veröffentlicht, werden sie automatisch an alle _Subscriber_ weitergeleitet.

6. **Rosa1 ROS2 Middleware**:
   ROS2 verwendet ein Middleware-Kommunikationssystem, um den Nachrichtenaustausch zwischen Knoten zu ermöglichen. Dieses Middleware-System ermöglicht es, Nachrichten zwischen Knoten, die auf verschiedenen physischen oder virtuellen Rechnern laufen, auszutauschen.

7. **Nachrichten-Synchronisation**:
   ROS2 ermöglicht auch, dass Knoten zeitlich synchronisierte Nachrichten empfangen können. Dies ist insbesondere in Anwendungen wichtig, in denen zeitliche Koordination erforderlich ist - was bei der Robotik häufg der Fall ist.

Insgesamt ermöglichen ROS2 Topics die Kommunikation und den Datenaustausch zwischen den Komponenten eines Roboters oder Robotersystems auf eine strukturierte und modulare Weise. Dies fördert die Wiederverwendbarkeit von Softwarekomponenten und die Skalierbarkeit von Robotersystemen.

## Vertiefung

```{tableofcontents}
```
