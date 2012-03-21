#!/usr/bin/python3
from fd import Functional_Dependencies as FD
from fdutils import *
def parse(file):
    res = []
    with open(file) as f:
        for line in f:
            l, _, r = line.partition(" -> ")
            left  = set(l.split(", "))
            right = set(r.split(", "))
            res.append(FD(left, right))
    return res


if __name__== "__main__":
    fdz= parse("input/input1.dep")
    print( closure({'A','C'} , fdz) )
