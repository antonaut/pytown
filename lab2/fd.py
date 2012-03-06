#!/bin/python

class Functional_Dependencies:
    def __init__(self, left = set(), right = set()):
        self._left = left
        self._right = right
    
    def __hash__(self):
        # Lazy evaluation of hash with cache
        if(self._hash == None):
            self._hash = 0
            for x in self._left | self._right:
                # Just xor the lefts and rights hashes together
                self._hash ^= hash(x)
        return self._hash
    
    def __eq__(self, other):
        return isinstance(other, Functional_Dependencies) && hash(self) == hash(other)
    
    def __ne__(self, other):
        return !(self == other)
    
    def __str__(self):
        # Lazy evaluation of hash with cache
        if(self._str == None):
            # E.g. "A, B, C -> D, E"
            self._str = ", ".join(self._left) + " -> " + ", ".join(self._right)
        return self._str
        
    def split(self):
        res = set()
        for r in self._right:
            res.add(Functional_Dependencies(self._left, r))
        return res