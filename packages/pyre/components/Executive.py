# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import weakref


# declaration
class Executive:
    """
    Mix-in class that provides access to the pyre executive and its managers
    """


    # public data
    pyre_executive = None
    pyre_registrar = None
    pyre_fileserver = None
    pyre_nameserver = None
    pyre_configurator = None


    @classmethod
    def pyre_installExecutive(cls, executive):
        """
        Record {executive} as the top-level framework object
        """
        # build weak references to the framework managers
        cls.pyre_executive = weakref.proxy(executive)
        cls.pyre_registrar = weakref.proxy(executive.registrar)
        cls.pyre_fileserver = weakref.proxy(executive.fileserver)
        cls.pyre_nameserver = weakref.proxy(executive.nameserver)
        cls.pyre_configurator = weakref.proxy(executive.configurator)
        # all done
        return


# end of file 