#!/usr/bin/env python
"""24b-odds.py: Advent of Code Day 24: Never tell me the odds"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import sympy as sym


def process_stones(raw):
    stones = {}
    for i, s in enumerate(raw):
        [x, y, z] = [int(x) for x in s.strip().split('@')[0].split(',')]
        [vx, vy, vz] = [int(x) for x in s.strip().split('@')[1].split(',')]
        stones[i] = tuple([x, y, z, vx, vy, vz])
    return stones


def magic_solver(stones):
    a = stones[0]
    b = stones[1]
    c = stones[2]

    x0 = sym.Symbol('x0')
    y0 = sym.Symbol('y0')
    z0 = sym.Symbol('z0')
    vx = sym.Symbol('vx')
    vy = sym.Symbol('vy')
    vz = sym.Symbol('vz')
    ta = sym.Symbol('ta')
    tb = sym.Symbol('tb')
    tc = sym.Symbol('tc')

    solution = sym.solve((x0+vx*ta-a[-3]*ta-a[0],
                          y0 + vy * ta - a[-2] * ta - a[1],
                          z0 + vz * ta - a[-1] * ta - a[2],
                          x0 + vx * tb - b[-3] * tb - b[0],
                          y0 + vy * tb - b[-2] * tb - b[1],
                          z0 + vz * tb - b[-1] * tb - b[2],
                          x0 + vx * tc - c[-3] * tc - c[0],
                          y0 + vy * tc - c[-2] * tc - c[1],
                          z0 + vz * tc - c[-1] * tc - c[2]),
                         (x0, y0, z0, vx, vy, vz, ta, tb, tc))
    print(solution)
    return solution


input_list = u.import_data('24')[:3]
input_stones = process_stones(input_list)
res = magic_solver(input_stones)
print(res[0][0]+res[0][1]+res[0][2])
