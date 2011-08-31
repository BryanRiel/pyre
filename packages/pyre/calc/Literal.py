# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Evaluator import Evaluator


class Literal(Evaluator):
    """
    Evaluator that returns a fixed value
    """


    # public data
    value = None


    def eval(self):
        """
        Compute my value
        """
        return self.value


    def __init__(self, value, **kwds):
        super().__init__(**kwds)
        self.value = value
        return


# end of file 
