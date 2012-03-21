#!/usr/bin/python3
from itertools import combinations
from fd import Functional_Dependencies as FD

def closure(attrs, fds):
    new_fds = set()
    closure = attrs
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
    for a in combs(R1):
        c = closure(a, S)
        for fd in S:
            if fd.right() < c and fd.right() < R1:
                T.add(fd)
    print(T)
    #tmp = set()
    #for fd in T:
    #    tmp |= fd.split()
    
    tmp = T.copy()
    for fd1 in tmp:
        for fd2 in tmp:
            if fd1.right() == fd2.left():
                T.discard(FD(fd1.left(), fd2.right()))
    print(T)
    
    tmp = T.copy()
    for fd in tmp:
        Y = fd.left()
        B = fd.right()
        l = len(Y)
        if l >= 2:
            for Z in combinations(Y, l - 1):
                fd1 = FD(Z, B)
                for fd2 in tmp:
                    if fd1.right() == fd2.left():
                        T.discard(fd)
                        T.add(fd1)
    
    return T

def combs(rel):
    for i in range(1, len(rel)):
        for j in combinations(rel, i):
            yield set(j)
