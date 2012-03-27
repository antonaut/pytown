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

def projection(Ra, R, S):
    T  = set()
    Ss = set()
    for fd in S:
        Ss |= fd.split()
    
    for X in subsets(R):
        Xp = closure(X,S)
        for fd in Ss:
            if fd.right() <= (Xp - X):
                T.add(FD(X, fd.right()))
    
    other = Ra - R
    for X in T.copy():
        for Y in X.left() | X.right():
            if Y in other:
                T.discard(X)
    
    for X in T.copy():
        for Y in T.copy():
            if X != Y and X.right() == Y.right() and X.left() < Y.left():
                T.discard(Y)

    return T

def BCNF(S):
    R = set()
    for fd in S:
        R |= fd.left() | fd.right()
    return _BCNF(R, S)

def _BCNF(R, S):
    fd = None
    
    for i in S:
        X  = i.left()
        Xp = closure(X, S)
        if Xp != R:
            fd =  i
            break
    
    if fd == None:
        return (set(R),)
    
    R1 = closure(fd.left(), S)
    R2 = fd.left() | (R - R1)
    S1 = projection(R, R1, S)
    S2 = projection(R, R2, S)
    
    return _BCNF(R1, S1) + _BCNF(R2, S2)
        

def subsets(rel):
    for i in range(1, len(rel)):
        for j in combinations(rel, i):
            yield set(j)

def one_less_subsets(Y):
    for x in combinations(Y, len(Y) - 1):
        yield set(x)
