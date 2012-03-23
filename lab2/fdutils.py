#!/usr/bin/python3
from itertools import combinations
from fd import Functional_Dependencies as FD

def closure(attrs, fds):
    new_fds = set()
    closure = attrs.copy()
    for fd in fds:
        new_fds |= fd.split()

    done = False
    while not done:
        done = True # assume we are done
        for fd in new_fds:
            if fd.left() <= closure and not fd.right() <= closure:
                closure |= fd.right()
                done = False
    return closure

def projection(R, R1, S):
    T = set()
    for X in combs(R1):
        Xp = closure(X, S)
        for A in R1:
            if A in Xp and {A} != X:
                T.add(FD(X, {A}))
    
    tmp = T.copy()
    for fd1 in tmp:
        for fd2 in tmp:
            if fd1.right() == fd2.left():
                T.discard(FD(fd1.left(), fd2.right()))
    
    tmp = T.copy()
    for fd in tmp:
        Y = fd.left()
        B = fd.right()
        l = len(Y)
        if l >= 2:
            for Z in combs2(Y, l):
                for fd2 in tmp:
                    if Z == fd2.right():
                        T.discard(fd)
                        T.add(FD(Z, B))
    
    return T

def combs(rel):
    for i in range(1, len(rel)):
        for j in combinations(rel, i):
            yield set(j)

def combs2(Y, l):
    for x in combinations(Y, l - 1):
        yield set(x)
