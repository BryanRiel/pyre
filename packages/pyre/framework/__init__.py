# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#

"""
This package contains the various top level framework managers.

This is the home of the pyre executive, a singleton that provides access to all pyre framework
services. Use pyre.executive to gain access to this object. The remainder of the classes that
are defined here are not meant to be instantiated directly, unless you are trying to extend the
framework. Be aware that the framework bootstrapping process is fairly sensitive to the
instantiation and initialization order of these objects, so caveat emptor.
"""


# the framework singleton
def executive(**kwds):
    """
    Factory for the framework executive.

    The pyre executive builds and maintains the top-level framework objects that provide the
    runtime framework services
    """
    from .Pyre import Pyre
    return Pyre(**kwds)


# end of file 
