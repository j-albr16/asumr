# Interface 

Die ROS2 Schnittstellen (Interfaces) sind eine wichtige Weiterentwicklung im ROS2-Framework, welche dazu dient, die Definition und Verwendung von Nachrichten, Diensten und Aktionen in einem ROS2-System zu vereinheitlichen. Es bietet eine Methode zur Definition von Schnittstellen, die sowohl von [Nachrichten](TODO) (Messages), [Diensten](TODO) (Services) als auch [Aktionen](TODO) (Actions) gemeinsam genutzt werden können.

## Schlüsselkonzepte

### Nachrichten, Dienste und Aktionen
   ROS2 unterstützt Nachrichten für asynchrone Datenübertragung über _Topics_, Dienste für synchrone Kommunikation und Aktionen für komplexere, lang andauernde Aufgaben. Jede dieser Kommunikationsformen verwendet spezifische Nachrichtentypen, die zuvor separat definiert wurden.

### Schnittstellen
   Ein ROS2 Interface ist eine strukturierte Definition, die sowohl von Nachrichten, Diensten als auch Aktionen gemeinsam genutzt werden kann. Die Verwendung von Interfaces führt zur Wiederverwendung von Datenstrukturen und fördert die Codequalität und -konsistenz.

### Nachrichten-Schnittstellen
   ROS2 ermöglicht die Definition von Nachrichten mithilfe von Interfaces. Eine Nachricht kann mehrere Felder enthalten, die aus den Typen und Namen bestehen, die in der zugehörigen Interface-Definition festgelegt sind. Nachrichten-Interfaces sind in ROS2-Schnittstellendateien (`.msg`) definiert.

### Dienst-Schnittstellen
   Dienst-Interfaces werden verwendet, um sowohl die Anfrage- als auch die Antwortseite eines Dienstes zu definieren. Dienst-Interfaces werden ebenfalls in Schnittstellendateien (`.srv`) erstellt und können in Service-Servern und -Clients verwendet werden.

### Aktions-Schnittstellen
   Aktionen sind komplexere Aufgaben, die mehrere Anfragen und Rückmeldungen beinhalten. Mit Aktions-Schnittstellen können sowohl die Zieldefinition als auch das Ergebnis der Aktion spezifiziert werden. Aktionen werden in ROS2-Schnittstellendateien (`.action`) definiert.

### Wiederverwendbarkeit und Konsistenz
   Der Einsatz von Interfaces ermöglicht es, die gleichen Datenstrukturen für Nachrichten, Dienste und Aktionen zu verwenden. Dies erhöht die Codekonsistenz und -qualität und erleichtert die Pflege von ROS2-Systemen.

## Verwendungsbeispiel

Angenommen, Sie möchten die Position eines Roboters über ein ROS2-_Topic_ veröffentlichen und auch einen _Service_ anbieten, um die Position auf Anfrage abzurufen. Mit dem _Interface_-Konzept können Sie eine gemeinsame Schnittstelle definieren:

**`position.srv` (Dienst-Schnittstelle)**:
```text
float64 x
float64 y
float64 theta
```

**`position.msg` (Nachrichten-Schnittstelle)**:
```text
float64 x
float64 y
float64 theta
```

In diesem Beispiel teilen die Dienstdefinition und die Nachrichtendefinition die gleiche Schnittstelle zur Darstellung der Positionsinformation. Dies ermöglicht die Wiederverwendung von Datenstrukturen, was zu konsistentem und wartbarem Code führt.

In eurem ROS2-System würdet ihr dann einen _Service-Server_ erstellen, der die Positionsdienstanfragen verarbeitet, und einen _Publisher_-Knoten, der die Positionsnachrichten auf einem _Topic_ veröffentlicht.

## Vertiefung

```{tableofcontents}
```

