#!/usr/bin/python3
from parser import parse
from fdutils import *
from fd import Functional_Dependencies as FD

f = FD({'A','B'}, {'C','D'})
g = FD({'A','B'}, {'C','D'})

fd1 = parse("input/input1.dep")
fd2 = parse("input/input2.dep")
fd3 = parse("input/input3.dep")
fdg = parse("input/generics.dep")
fda = parse("input/advancedAttributes.dep")

c1 = closure({'A','C'}, fd1)
