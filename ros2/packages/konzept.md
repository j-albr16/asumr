# Konzept

## Package

Ein Package ist eine Organisationsweise für deinen ROS2 Code. In einem Package ist der Sourcecode zum erstellen von ROS2 Artefakten wie Nodes, Topics und Services definiert.

Packages sind auch eine einfache möglichkeit ROS2 Code mit anderen leuten zu Teilen:

Minimale bestandteile eines Packages:

```python
asumr_package/
    package.xml
    resource/asumr_package/
    setup.cfg
    setup.py
    asumr_package/
    src/
```

Erklärung:

**package.xml** Metainformationen 
**resource/<package_name>** Marker file für Package
**setup.cfg** Muss vorhanden sein wenn das Package Executables besitzt (Damit `ros2 run` funktioniert)
**setup.py** Build Script zum installieren des Packages
**<package_name>** Wird von ROS2 tools verwendet, um das Package zu finden



## Workspace

Ein ROS2 Workspace ist ein Ordner, der alle deine packages enthält.


```bash
mkdir ~/ros2_ws
mkdir ~/ros2_ws/src
```

wenn du neue Packages erstellst, kannst du diese in den `~/ros2_ws/src` Ordner legen.
