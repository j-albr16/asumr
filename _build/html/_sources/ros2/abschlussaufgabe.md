# Abschlussaufgabe

## Einführung

In dieser Aufgabe werden Sie verschiedene Konzepte in ROS 2 erkunden, einschließlich Packages, Nodes, Topics, Interfaces, Services, Launching und Navigation. ROS 2 ist ein leistungsstarkes Framework zur Entwicklung von Robotikanwendungen, und das Verständnis dieser Konzepte ist entscheidend für den effektiven Bau und die Steuerung von Robotern.

## Aufgabe 1: Packages und Nodes (10 Punkte)

**A. Erstellen eines ROS 2-Pakets**

Erstellen Sie ein neues ROS 2-Paket mit dem Namen "my_robot_pkg". Stellen Sie sicher, dass es ein "launch"-Verzeichnis und ein "scripts"-Verzeichnis enthält.

**B. Erstellen eines Publisher Nodes**

Schreiben Sie ein Python-Skript, das einen ROS 2-Node namens "my_publisher_node" erstellt. Der Node sollte Nachrichten an ein Topic namens "sensor_data" mit Dummy-Sensordaten (z.B. Zufallszahlen) veröffentlichen.

**C. Erstellen eines Subscriber Nodes**

Schreiben Sie ein Python-Skript, das einen ROS 2-Node namens "my_subscriber_node" erstellt. Der Node sollte sich für das "sensor_data"-Topic abonnieren und die empfangenen Nachrichten ausgeben.

## Aufgabe 2: Topics und Interfaces (15 Punkte)

**A. Definition einer benutzerdefinierten Nachricht**

Erstellen Sie eine benutzerdefinierte Nachricht in Ihrem Paket. Die Nachricht sollte die Struktur des Standorts eines Roboters definieren (z.B. x, y, theta). Nennen Sie diesen Nachrichtentyp "RobotLocation."

**B. Ändern des Publisher Nodes**

Ändern Sie den Publisher-Node, um Instanzen des Nachrichtentyps "RobotLocation" anstelle von Zufallszahlen an das "robot_location"-Topic zu veröffentlichen.

**C. Ändern des Subscriber Nodes**

Ändern Sie den Subscriber-Node, um "RobotLocation"-Nachrichten vom "robot_location"-Topic zu empfangen und zu verarbeiten.

## Aufgabe 3: Services (15 Punkte)

**A. Erstellen eines ROS 2-Service**

Schreiben Sie ein Python-Skript, das einen ROS 2-Service namens "move_robot" erstellt. Der Service sollte eine Anfrage für einen neuen Roboterstandort (eine Instanz des Nachrichtentyps "RobotLocation") erhalten und den Roboter an diesen Standort bewegen.

**B. Erstellen eines Client Nodes**

Schreiben Sie ein Python-Skript, um einen ROS 2-Node mit dem Namen "move_robot_client" zu erstellen. Der Node sollte den "move_robot"-Service verwenden, um den Roboter an einen bestimmten Standort zu bewegen.

## Aufgabe 4: Launching (10 Punkte)

**A. Erstellen einer Launch-Datei**

Erstellen Sie eine Launch-Datei, die alle von Ihnen in den Aufgaben 1, 2 und 3 erstellten Nodes starten kann. Die Launch-Datei sollte auch Parameter für die Nodes setzen, wie z.B. den anfänglichen Standort des Roboters.

**B. Starten des Systems**

Starten Sie Ihr Roboterkontrollsystem mithilfe der erstellten Launch-Datei.

## Aufgabe 5: Navigation (20 Punkte)

**A. Erstellen eines Navigation Stack**

Integrieren Sie einen Navigations-Stack in Ihr Roboterkontrollsystem. Verwenden Sie einen simulierten Roboter wie den TurtleBot3 und konfigurieren Sie die erforderlichen Parameter für die Navigation.

**B. Implementieren der autonomen Navigation**

Ändern Sie den "move_robot_client"-Node, um die autonome Navigation zu ermöglichen. Implementieren Sie einen einfachen Algorithmus, der es dem Roboter ermöglicht, zu bestimmten Koordinaten innerhalb einer vordefinierten Karte zu navigieren.

## Aufgabe 6: Dokumentation und Bericht (10 Punkte)

**A. Erstellen eines README**

Erstellen Sie eine README-Datei für Ihr "my_robot_pkg"-Paket. Geben Sie Anleitungen zur Erstellung, Ausführung und Verwendung Ihres Roboterkontrollsystems an.

**B. Schreiben eines Berichts**

Verfassen Sie einen Bericht, in dem Sie Ihre Erfahrungen, Herausforderungen und Lösungen bei der Bearbeitung der Aufgaben dokumentieren. Diskutieren Sie die Bedeutung von ROS 2 in der Robotikentwicklung.

## Abgabe

Reichen Sie einen komprimierten Ordner ein, der Ihr ROS 2-Paket, Launch-Dateien, Python-Skripte und Dokumentation enthält.

**Wichtiger Hinweis**: Stellen Sie sicher, dass Sie die geeigneten ROS 2-Konventionen und Best Practices in Ihrem Code und Ihrer Dokumentation verwenden. Kommentieren und formatieren Sie Ihren Code ordnungsgemäß für Klarheit. Eine gute Dokumentation und Code-Organisation sind wesentlich, um Ihr Roboterkontrollsystem verständlich und wartbar zu machen.
