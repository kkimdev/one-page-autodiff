#!/usr/bin/env python3

from __future__ import print_function
import math

class Variable:
    all_variables = []

    def __init__(self, value):
        self.value = value
        self.adjoints = []
        Variable.all_variables.append(self)

    def __add__(self, rhs):
        y = Variable(self.value + rhs.value)
        self.adjoints.append((y, 1.0))
        rhs.adjoints.append((y, 1.0))
        return y

    def __mul__(self, rhs):
        y = Variable(self.value * rhs.value)
        self.adjoints.append((y, rhs.value))
        rhs.adjoints.append((y, self.value))
        return y

    def sin(self):
        y = Variable(math.sin(self.value))
        self.adjoints.append((y, math.cos(self.value)))
        return y

    def diff(self):
        assert Variable.all_variables[-1] == self
        self.derivative = 1.0
        for variable in reversed(Variable.all_variables[:-1]):
            variable.derivative = 0.0
            for y, adjoint in variable.adjoints:
                variable.derivative += y.derivative * adjoint

x1 = Variable(3.14)
x2 = Variable(5)
y = (x1 * x2) + x1.sin()
print('y =', y.value)

y.diff()
print('dy/dx1 =', x1.derivative)
print('dy/dx2 =', x2.derivative)
