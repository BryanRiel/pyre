# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


from .Unary import Unary


class ReflectiveDivision(Unary):
    """
    Divide a scalar by the value of a node
    """


    def compute(self):
        """
        Compute and return my value
        """
        return self._factor / self._op.value


    # meta-methods
    def __init__(self, factor, **kwds):
        super().__init__(**kwds)
        self._factor = factor
        return


# end of file 
