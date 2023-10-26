# Konzept

Ein ROS 2 (Robot Operating System 2) Topic ist ein grundlegendes Kommunikationskonzept in ROS 2, das dazu dient, Daten zwischen verschiedenen Komponenten eines Roboters oder einer Robotersystemarchitektur auszutauschen. ROS 2 ist ein flexibles und modulares Framework zur Entwicklung von Robotersoftware, und Topics sind eine wichtige Möglichkeit, um Informationen zwischen Knoten (Nodes) in einem ROS 2-System zu übertragen.

Hier sind die wichtigsten Merkmale und Konzepte eines ROS 2 Topics:

1. **Nachrichten**: Topics dienen dem Austausch von Nachrichten. Nachrichten sind Datenstrukturen, die Informationen übertragen. Sie können einfache Datentypen wie Zahlen oder komplexere Strukturen wie Sensorwerte, Bildinformationen oder Steuerbefehle enthalten. ROS 2 unterstützt benutzerdefinierte Nachrichtentypen.

2. **Publisher und Subscriber**: Ein ROS 2-System besteht aus Knoten, die Publisher und/oder Subscriber für verschiedene Topics sein können. Ein Publisher ist ein Knoten, der Nachrichten zu einem bestimmten Topic sendet, während ein Subscriber ein Knoten ist, der Nachrichten von diesem Topic empfängt.

3. **Topic-Namen**: Jedes Topic hat einen eindeutigen Namen im ROS 2-System. Dieser Name ermöglicht es Knoten, die Nachrichten austauschen möchten, das entsprechende Topic zu identifizieren. Der Name folgt normalerweise einem bestimmten Namensschema, z.B., "/sensor_data" oder "/robot_status".

4. **Nachrichten-Publizieren**: Ein Knoten, der Informationen bereitstellen möchte, erstellt einen Publisher für ein bestimmtes Topic und veröffentlicht Nachrichten auf diesem Topic. Andere Knoten können dann diese Nachrichten abrufen.

5. **Nachrichten-Abonnieren**: Ein Knoten, der Informationen benötigt, erstellt einen Subscriber für ein bestimmtes Topic und abonniert dieses Topic. Wenn ein Publisher Nachrichten auf diesem Topic veröffentlicht, werden sie automatisch an alle Subscriber weitergeleitet.

6. **Rosa1 ROS 2 Middleware**: ROS 2 verwendet ein Middleware-Kommunikationssystem, um den Nachrichtenaustausch zwischen Knoten zu ermöglichen. Dieses Middleware-System ermöglicht es, Nachrichten zwischen Knoten, die auf verschiedenen physischen oder virtuellen Rechnern laufen, auszutauschen.

7. **Nachrichten-Synchronisation**: ROS 2 ermöglicht auch die Synchronisation von Nachrichten, sodass Knoten Nachrichten empfangen können, die zeitlich synchronisiert sind. Dies ist insbesondere in Anwendungen wichtig, in denen zeitliche Koordination erforderlich ist, wie bei der Robotik.

Insgesamt ermöglichen ROS 2 Topics die Kommunikation und den Datenaustausch zwischen den Komponenten eines Roboters oder Robotersystems auf eine strukturierte und modulare Weise. Dies fördert die Wiederverwendbarkeit von Softwarekomponenten und die Skalierbarkeit von Robotersystemen.


