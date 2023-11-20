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

# Forward Kinematik

##  Simplification of Matrix Multiplication using sympy

Expressing the kinematics as homogeneous transformation matrices.

```{code-cell} ipython3
# Install the pip package in the current Jupyter kernel if neccessary 
import sys
!{sys.executable} -m pip install sympy
```

```{code-cell} ipython3
from sympy import *
theta_1 = Symbol('theta_1')
theta_2 = Symbol('theta_2')
l_1 = Symbol('l_1')
l_2 = Symbol('l_2')
T_1 = Matrix([[cos(theta_1), -sin(theta_1), 0], [sin(theta_1), cos(theta_1),0], [0, 0, 1]])
T_2 = Matrix([[1, 0, l_1], [0, 1, 0], [0, 0, 1]])
T_3 = Matrix([[cos(theta_2), -sin(theta_2), 0], [sin(theta_2), cos(theta_2),0], [0, 0, 1]])
T_4 = Matrix([[1, 0, l_2], [0, 1, 0], [0, 0, 1]])
fw_kin_2segm_expr = T_1 * T_2 * T_3 * T_4
```

## Simplify the expression using sympy

```{code-cell} ipython3
simplify_expression = simplify(str(fw_kin_2segm_expr))
pprint(simplify_expression)
```

## Extending to a 3-segmented manipulator

Adding additional transformation matrices T_5 and T_6

```{code-cell} ipython3
theta_3 = Symbol('theta_3')
l_3 = Symbol('l_3')
T_5 = Matrix([[cos(theta_3), -sin(theta_3), 0], [sin(theta_3), cos(theta_3),0], [0, 0, 1]])
T_6 = Matrix([[1, 0, l_3], [0, 1, 0], [0, 0, 1]])
fw_kin_3segm_expr = T_1 * T_2 * T_3 * T_4 * T_5 * T_6
simplify_expression_3segm = simplify(str(fw_kin_3segm_expr))
pprint(simplify_expression_3segm)
```

## Switch printing to Latex formula

```{code-cell} ipython3
from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=False)
simplify_expression_3segm
```

```{code-cell} ipython3

```
