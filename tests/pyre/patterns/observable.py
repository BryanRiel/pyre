#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Verify that the implementation of Observable works as advertised
"""

  
from pyre.patterns.Observable import Observable


class node(Observable):
    """
    the Observable
    """

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.notify()
        return self

    def __init__(self, value, **kwds):
        super().__init__(**kwds)
        self._value = value
        return


class probe:
    """
    the observer
    """

    def __init__(self, node, **kwds):
        super().__init__(**kwds)
        self.cache = None
        node.addObserver(self._update)
        return

    def _update(self, node):
        self.cache = node.value
        return
    

def test():
    n = node(0)
    p = probe(n)
    n.value = 3.14159

    assert p.cache == n.value

    return node, probe


# main
if __name__ == "__main__":
    test()


# end of file 
