# Aufgabe 

Ziel dieser Übung ist es einen Service zu erstellen. Dieser initialisiert bei Erstellung eine Karte (2D Array) und füllt diese zufällig mit `0`en (für Wasser) und `1`en (für Land) füll. Bei einer Anfrage erhält dieser Service eine Position (x und y Wert).  Als Antwort gibt der Service einen Wahrheitswert zurück ob es sich bei dieser Position um ein Wasserfeld handelt.

## Aufgabe 1 - Paket

Erstellen Sie ein Paket mit dem Namen `example_service`. Erstellen sie zusätzlich ein Paket `custom_interfaces`, welches alle Interfaces enthält.

## Aufgabe 2 - Interface

Implementieren Sie ein Interface mit dem Namen `Pos.srv` in das `custom_interfaces` Paket. Dieses `.srv` File enthält im Anfrage Teil den `x` und den `y` Wert. Finden Sie einen Sinnfollen Typen für diese Parameter. Das Interface hat als Rückgabewert ein Boolean mit dem namen `is_water`.

## Aufgabe 3 - Server

Implementieren Sie eine Node mit dem Namen `server.py`. Diese soll bei Initialisierung die besagte Karte mit der Größe `10` initialisieren. Zusätzlich soll diese Node den Service mit besagter Funktionalität erstellen. Vergessen Sie nicht das `custom_interfaces` Paket als Abhängigkeit im `package.xml` einzufügen.

## Aufgabe 4 - Client

Implementieren Sie einen Node mit dem Namen `client.py`. Diese soll einen Client für besagten Service erstellen und eine Methode `send_request` besitzen um eine Anfrage an den Service für eine Position zu stellen. 

Bei Initialisierung soll der Client alle 100 Felder abfragen und die Anzahl an Wasserfeldern auf der Konsole ausgeben.

## Aufgabe 5 - Launch File

Erstellen Sie ein Launch File, welches den Server und den Client startet. Übergeben Sie die Mapgröße als LaunchParameter an den Client und den Server.

Starten Sie den Service über das launch File und überprüfen Sie die Ausgabe.
