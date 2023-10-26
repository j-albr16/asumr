# Konzept

Das ROS 2 Service-Konzept ist ein weiteres wichtiges Kommunikationsmittel in ROS 2, das es ermöglicht, synchrone Anfragen und Antworten zwischen verschiedenen Knoten in einem ROS 2-System auszutauschen. Während ROS 2 Topics verwendet wird, um asynchrone Datenströme zu übertragen, dienen Services zur Verwaltung von synchrone Kommunikation zwischen Knoten. Hier sind die Schlüsselkonzepte des ROS 2 Service-Konzepts:

1. **Service-Nachrichten**: Services verwenden Nachrichten zur Kommunikation, ähnlich wie Topics. Jedoch sind Service-Nachrichten in der Regel zweigeteilt, bestehend aus einer Service-Anfrage (Request) und einer Service-Antwort (Response). Die Anfrage enthält Informationen, die an einen Dienstleister gesendet werden, während die Antwort die Daten enthält, die vom Dienstleister zurückgegeben werden.

2. **Service-Server**: Ein Knoten, der in der Lage ist, einen Dienst anzubieten, wird als Service-Server bezeichnet. Der Service-Server ist für die Entgegennahme von Anfragen und die Bereitstellung von Antworten verantwortlich. Er wartet auf Anfragen von anderen Knoten und führt die angeforderte Aktion aus, wenn eine Anfrage eingeht.

3. **Service-Client**: Ein Knoten, der eine Anfrage an einen Service-Server sendet und auf die Antwort wartet, wird als Service-Client bezeichnet. Der Service-Client initiiert die Kommunikation, indem er eine Anfrage an den Service-Server sendet und dann auf die Antwort wartet.

4. **Service-Namen**: Jeder Service hat einen eindeutigen Namen, der innerhalb des ROS 2-Systems verwendet wird, um auf den Service zuzugreifen. Service-Namen sind ähnlich wie Topic-Namen strukturiert, z.B., "/get_distance".

5. **Synchrone Kommunikation**: Im Gegensatz zu Topics, bei denen Daten asynchron ausgetauscht werden, sind Services für synchrone Kommunikation konzipiert. Der Service-Client sendet eine Anfrage an den Service-Server und wartet, bis eine Antwort erhalten wird. Dies ermöglicht es, auf Anfragen und Antworten zeitlich genau abgestimmt zu reagieren.

Hier ist ein einfaches Beispiel, wie ein ROS 2 Service verwendet wird:

Angenommen, Sie haben einen Roboter mit einem Service, der die aktuelle Temperatur eines Sensors zurückgibt. Der Service-Server würde die Temperaturanfrage entgegennehmen und die aktuelle Temperatur als Antwort zurückgeben. Der Service-Client initiiert die Anfrage und erhält die Temperaturdaten zurück.

Die Implementierung von Service-Server und -Client in ROS 2 ähnelt der von Publisher und Subscriber, wobei Sie Service-Nachrichten definieren, Service-Server-Knoten erstellen und Service-Client-Knoten erstellen, um Anfragen zu senden und Antworten zu empfangen. Dies ermöglicht es, synchrone Aufgaben in ROS 2-Systemen durchzuführen, wie beispielsweise das Anfordern von Sensorinformationen, das Ausführen von Berechnungen und das Erhalten von Ergebnissen in Echtzeit.
