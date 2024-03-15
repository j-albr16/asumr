# Packages

## Konzept

### Package

Ein Paket ist eine Organisationsweise für deinen ROS2 Quelltext. In einem Paket ist der Quelltext zum Erstellen von ROS2 Artefakten wie Nodes, Topics und Services definiert.

Packages sind auch eine einfache Möglichkeit ROS2 Code mit anderen Leuten zu teilen:

Minimale Bestandteile eines Pakets:

```text
asumr_package/
    package.xml
    resource/asumr_package/
    setup.cfg
    setup.py
    asumr_package/
    src/
```

Erklärung:

- **package.xml** Metainformationen 
- **resource/_<package_name>_** Marker file für das Paket
- **setup.cfg** Muss vorhanden sein wenn das Paket Executables besitzt (Damit `ros2 run` funktioniert)
- **setup.py** Build Script zum Installieren des Pakets
- **_<package_name>_** Wird von ROS2 Tools verwendet, um das Paket zu finden

### Workspace

Ein ROS2 Workspace ist ein Ordner, der alle deine packages enthält.

```bash
mkdir -p ~/ros2_ws/src
```

wenn du neue Packages erstellst, kannst du diese in den `~/ros2_ws/src` Ordner legen.

```{tableofcontents}
```
