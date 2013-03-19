# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


from .Type import Type


class Float(Type):
    """
    A class declarator for floats
    """


    # interface
    @classmethod
    def coerce(cls, value, **kwds):
        """
        Attempt to convert {value} into a float
        """
        # get the interpreter to evaluate simple expressions
        if isinstance(value, str):
            value = eval(value)
        # attempt to cast {value} into a float
        try:
            return float(value)
        except (TypeError, ValueError) as error:
            raise cls.CastingError(value=value, description=str(error)) from error


# end of file 