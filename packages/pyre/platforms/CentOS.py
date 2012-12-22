# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import re
# superclass
from .Linux import Linux


# declaration
class CentOS(Linux, family='pyre.platforms.centos'):
    """
    Encapsulation of a host running linux on the centos distribution
    """


    # public data
    distribution = 'centos'


# end of file 
