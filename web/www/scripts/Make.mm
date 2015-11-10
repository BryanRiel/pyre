# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#

# project settings
include pyre.def
# the package
PACKAGE = scripts

# the location
EXPORT_WEBDIR = $(EXPORT_ROOT)/web/www/$(PROJECT)/$(PACKAGE)
# the exported items
EXPORT_WEB = *.js

# targets
all: export

export:: export-web

live: live-web-package

# end of file