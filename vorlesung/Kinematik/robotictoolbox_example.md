---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: py_38
  language: python
  name: python3
---

# Robotictoolbox Demonstration

The roboticstoolbox provides kinematics calculations for multiple common manipulator arms. Here, we will just demonstrate using these. For more information see the [documentation](https://petercorke.github.io/robotics-toolbox-python/).

```{code-cell} ipython3
:tags: ["hide-cell"]
# Install the pip package in the current Jupyter kernel if neccessary 
import sys
!{sys.executable} -m pip install roboticstoolbox-python

# You have to restart the kernel afterwards!
```

## A) Puma 560 Robot Arm

Simple example for the Puma 560, six degrees of freedom arm. Provided are the DH parameters and a simple forward kinematic setup as well as an inverse kinematics call (using analytical solution.)

```{code-cell} ipython3
import roboticstoolbox as rtb
puma = rtb.models.DH.Puma560()       # instantiate robot model
print(puma)
T = puma.fkine([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
sol = puma.ikine_LM(T) 
print(sol)
```

For visualization we can use matplotlib:

```{code-cell} ipython3
%matplotlib widget
puma.plot(sol.q)
```

## B) Panda robot

with seven degrees of freedom.

```{code-cell} ipython3
import roboticstoolbox as rtb
panda = rtb.models.DH.Panda()
print(panda)
```

## Visualization

For more advanced simulation, see the documentation and running the toolbox locally on your system. This allows to setup the nice swift simulator in your browser.

```{image} https://petercorke.github.io/robotics-toolbox-python/_images/swift.png
:width: 400px
```

+++
