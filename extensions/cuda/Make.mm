# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#

PROJECT = pyre
PACKAGE = extensions
MODULE = cuda

include cuda/default.def
include std-pythonmodule.def

PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)/$(MODULE)
PROJ_LCXX_LIBPATH=$(BLD_LIBDIR)
EXTERNAL_LIBS += -ljournal

PROJ_SRCS = \
    exceptions.cc \
    metadata.cc

# end of file
