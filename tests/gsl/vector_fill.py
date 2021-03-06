#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2018 all rights reserved
#


"""
Fill a vector with a constant value
"""


def test():
    # package access
    import gsl
    # make a vector
    v = gsl.vector(shape=100)
    # set it to some value
    v.fill(value=2)
    # verify it happened
    for e in v: assert e == 2
    # all done
    return v


# main
if __name__ == "__main__":
    test()


# end of file
