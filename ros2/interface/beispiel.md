---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Beispiel

## Erstellung eines Interfaces

Interfaces werden in einem `.msg` file im `msg/` Ordner im ROS2 Package definiert. In diesen `.msg` files beschreibt jede Zeile eine Variable mit einem Typ und einem Namen.

Hierbei werden beschreibt jede Zeile eine Variable und der Typ wird über ein Leerzeichen von dem Namen der Variablen getrennt.

```bash
fieldtype1 fieldname1
fieldtype2 fieldname2
fieldtype3 fieldname3
```

Beispiel:

```bash
int8 telnumber
bool ledig
```

### Arrays

Es können ebenfalls arrays erstellt werden:

```bash
int8[] some_array
int8[5] 5_ints_array
int8[<=5] bis_zu_5_ints_array

string some_string
string<=5 bist_zu_5_char_string
```

### Standard Werte

Standard werte für Variaben können separiert mit einem Leerzeichen an eine Zeile definiert werden:

```
fieldtype fieldname fielddefault
```

```
uint8 x 42
int16 y -2000
string full_name "John Doe"
int32[] samples [-200, -100, 0, 100, 200]
```

### Konstanten

Konstanten programmatisch nicht mehr verändert werden.

Eine Konstante kann wie folgt definiert werden:

```
constanttype CONStANTNAME=constantvalue
```

Beispiel:

```bash
int32 X=3
int32 Y=1
```

## Services


Services werden in sog. `.srv` files, die sich in einem `srv/` Ordner im ROS2 Package befinden.

Diese `.srv` bestehen aus einem request und response teil, welche analog zu den `.msg` types definiert werden. Die beiden Teile werden durch das Zeichen `---` getrennt:

```
string str
---
string str
```


## Abschluss Beispiel

Es können zusätzlich auch andere Interfaces refernziert werden:

```
#request constants
int8 FOO=1
int8 BAR=2
#request fields
int8 foobar
another_pkg/AnotherMessage msg
---
#response constants
uint32 SECRET=123456
#response fields
another_pkg/YetAnotherMessage val
CustomMessageDefinedInThisPackage value
uint32 an_integer
```













