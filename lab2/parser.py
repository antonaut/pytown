#!/usr/bin/python3
from fd import Functional_Dependencies as FD

def parse(file):
    res = []
    with open(file) as f:
        for line in f:
            l, _, r = line.partition(" -> ")
            left  = set(l.split(", "))
            right = set(r.split(", "))
            res.add(FD(left, right))
    return res
