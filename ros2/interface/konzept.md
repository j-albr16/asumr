# Konzept

Das ROS 2 Interface-Konzept ist eine wichtige Weiterentwicklung im ROS 2-Framework, das dazu dient, die Definition und Verwendung von Nachrichten, Diensten und Aktionen in einem ROS 2-System zu vereinheitlichen. Es bietet eine Methode zur Definition von Schnittstellen (Interfaces), die sowohl von Nachrichten, Diensten als auch Aktionen gemeinsam genutzt werden können. Hier sind die Schlüsselkonzepte des ROS 2 Interface-Konzepts:

1. **Nachrichten, Dienste und Aktionen**: ROS 2 unterstützt Nachrichten für asynchrone Datenübertragung über Topics, Dienste für synchrone Kommunikation und Aktionen für komplexere, lang andauernde Aufgaben. Jede dieser Kommunikationsformen verwendet spezifische Nachrichtentypen, die zuvor separat definiert wurden.

2. **Interfaces**: Ein ROS 2 Interface ist eine strukturierte Definition, die sowohl von Nachrichten, Diensten als auch Aktionen gemeinsam genutzt werden kann. Die Verwendung von Interfaces führt zur Wiederverwendung von Datenstrukturen und fördert die Codequalität und -konsistenz.

3. **Nachrichten-Interfaces**: ROS 2 ermöglicht die Definition von Nachrichten mithilfe von Interfaces. Eine Nachricht kann mehrere Felder enthalten, die aus den Typen und Namen bestehen, die in der zugehörigen Interface-Definition definiert sind. Nachrichten-Interfaces sind in ROS 2-Schnittstellendateien (`.msg`) definiert.

4. **Dienst-Interfaces**: Dienst-Interfaces werden verwendet, um sowohl die Anfrage- als auch die Antwortseite eines Dienstes zu definieren. Dienst-Interfaces werden ebenfalls in Schnittstellendateien (`.srv`) erstellt und können in Service-Servern und -Clients verwendet werden.

5. **Aktion-Interfaces**: Aktionen sind komplexere Aufgaben, die mehrere Anfragen und Rückmeldungen beinhalten. Mit Aktion-Interfaces können sowohl die Zieldefinition als auch das Ergebnis der Aktion spezifiziert werden. Aktionen werden in ROS 2-Schnittstellendateien (`.action`) definiert.

6. **Wiederverwendbarkeit und Konsistenz**: Der Einsatz von Interfaces ermöglicht es, die gleichen Datenstrukturen für Nachrichten, Dienste und Aktionen zu verwenden. Dies erhöht die Codekonsistenz und -qualität und erleichtert die Pflege von ROS 2-Systemen.

Hier ist ein einfaches Beispiel zur Verwendung eines ROS 2 Interface-Konzepts:

Angenommen, Sie möchten die Position eines Roboters über einen ROS 2-Topic veröffentlichen und auch einen Service anbieten, um die Position auf Anfrage abzurufen. Mit dem Interface-Konzept können Sie eine gemeinsame Schnittstellen-Definition erstellen:

**Position.srv (Service-Interface)**:
```yaml
float64 x
float64 y
float64 theta
```

**Position.msg (Nachrichten-Interface)**:
```yaml
float64 x
float64 y
float64 theta
```

In diesem Beispiel teilen die Service-Definition und die Nachrichtendefinition die gleiche Schnittstelle zur Darstellung der Positionsinformation. Dies ermöglicht die Wiederverwendung von Datenstrukturen, was zu konsistentem und wartbarem Code führt.

In Ihrem ROS 2-System würden Sie dann einen Service-Server erstellen, der die Positionsdienstanfragen verarbeitet, und einen Publisher-Knoten, der die Positionsnachrichten auf einem Topic veröffentlicht. Das Interface-Konzept ermöglicht es, die gleichen Datenstrukturen für diese beiden Kommunikationsmittel zu verwenden, was die Entwicklung und Wartung erleichtert.
