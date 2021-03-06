# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2018 all rights reserved
#


# externals
import platform
# framework
import pyre
# my protocol
from .Platform import Platform
# cpu info
from .CPUInfo import CPUInfo


# declaration
class Host(pyre.component, family='pyre.platforms.generic', implements=Platform):
    """
    Encapsulation of a generic host
    """

    # public data
    # host
    hostname = platform.node() # the name of the host on which this process is running
    nickname = None # the short name assigned to this host by the user
    # cpus
    cpus = None # the triplet (cpus, physical cores, logical cores)
    # os
    platform = None # the OS type on which this process is running
    release = None # the OS release
    codename = None # the OS version
    # distribution
    distribution = None # a clue about the package manager on this machine

    # user configurable state
    externals = pyre.properties.dict(schema=pyre.properties.str())
    externals.doc = 'a map of package categories to installation instances'

    packager = pyre.platforms.packager()
    packager.doc = 'the manager of external packages installed on this host'


    # meta methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # discover the number of cpus
        self.cpus = self.cpuSurvey()
        # all done
        return


    # implementation details: explorers
    @classmethod
    def cpuSurvey(cls):
        """
        Collect information about the CPU resources on this host
        """
        # by default, we know nothing; so assume one single core cpu with no hyper-threading
        # subclasses should override with their platform dependent survey code
        return CPUInfo()


    # feature support
    @classmethod
    def dynamicLibrary(cls, stem):
        """
        Convert the sequence of stems into likely filenames for shared objects
        """
        # go through each one
        return cls.template_dynamicLibrary.format(cls, stem)


    @classmethod
    def staticLibrary(cls, stem):
        """
        Convert the sequence of stems into likely filenames for shared objects
        """
        # go through each one
        return cls.template_staticLibrary.format(cls, stem)


    @classmethod
    def dynamicLibraries(cls, stems):
        """
        Convert the sequence of stems into likely filenames for shared objects
        """
        # go through each one
        return (cls.template_dynamicLibrary.format(cls, stem) for stem in stems)


    @classmethod
    def staticLibraries(cls, stems):
        """
        Convert the sequence of stems into likely filenames for shared objects
        """
        # go through each one
        return (cls.template_staticLibrary.format(cls, stem) for stem in stems)


# end of file
