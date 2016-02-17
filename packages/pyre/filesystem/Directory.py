# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


# superclass
from .InfoStat import InfoStat
from .InfoDirectory import InfoDirectory


# class declaration
class Directory(InfoStat, InfoDirectory):
    """
    Representation of local filesystem folders
    """


# end of file
