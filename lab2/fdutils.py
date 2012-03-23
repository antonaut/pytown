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
    for X in subsets(R1):
        Xp = closure(X, S)
        for A in R1:
            if A in Xp and {A} != X:
                T.add(FD(X, {A}))
    
    tmp = T.copy()
    #print(T)
    for fd1 in tmp:
        for fd2 in tmp:
            if fd1.right() == fd2.left():
                T.discard(FD(fd1.left(), fd2.right()))
    
    tmp = T.copy()
    #print(T)
    for fd in tmp:
        Y = fd.left()
        B = fd.right()
        l = len(Y)
        if l >= 2:
            for Z in one_less_subsets(Y):
                for fd2 in tmp:
                    if Z == fd2.right():
                        pass
                        #T.discard(fd)
                        #T.add(FD(Z, B))
    
    #print(T)
    for fd in T.copy():
        if fd.right() <= fd.left():
            T.discard(fd)
    
    #print(T)
    return T

def BCNF(R, S):
    # is R in BCNF?
    tmp = []
    if all( fds_contains_keys(R, S, tmp) ):
        return R
    
    tmp = tmp[0]
    R1 = closure(tmp.left(), S)
    R2 = tmp.left() | (R - R1)
    S1 = projection(R, R1, S)
    S2 = projection(R, R2, S)
    
    print('R1: {}, S1: {}\nR2: {}, S2: {}'.format(R1,S1,R2,S2))
    
    return True
    #return BCNF(R1, S1) | BCNF(R2, S2)

def fds_contains_keys(R, S, tmp):
    K = keys(R, S)
    for fd in S:
        if any( [k in fd.left() for k in K] ):
            yield True
        else:
            tmp.append(fd)
            yield False

def keys(R, S):
    keys = set()
    
    for A in subsets(R):
        if closure(A, S) == R:
            if all( [closure(X, S) == R for X in one_less_subsets(A)] ):
                keys |= A
    return keys

def subsets(rel):
    for i in range(1, len(rel)):
        for j in combinations(rel, i):
            yield set(j)

def one_less_subsets(Y):
    for x in combinations(Y, len(Y) - 1):
        yield set(x)
