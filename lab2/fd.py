#!/usr/bin/python3

class Functional_Dependencies:
    # This class has to be immutable to work with sets
    def __init__(self, left = frozenset(), right = frozenset()):
        self._left = frozenset(left)
        self._right = frozenset(right)
        self._str = None
        self._hash = None
    
    def __hash__(self):
        # Lazy evaluation of hash with cache
        if self._hash == None:
            self._hash = hash(self._left) ^ hash(self._right)
        return self._hash
    
    def __eq__(self, other):
        return isinstance(other, Functional_Dependencies) and hash(self) == hash(other)
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        # Lazy evaluation of str with cache
        if self._str == None:
            # E.g. "A, B, C -> D, E"
            self._str = ", ".join(self._left) + " -> " + ", ".join(self._right)
        return self._str
    
    def __repr__(self):
        return '"' + str(self) + '"'
        
    def split(self):
        res = set()
        for r in self._right:
            res.add(Functional_Dependencies(self._left, {r}))
        return res
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right
