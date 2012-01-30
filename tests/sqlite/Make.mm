# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


PROJECT = pyre
PROJ_CLEAN += pyre.sql

#--------------------------------------------------------------------------
#

all: test

test: sanity components clean

sanity:
	${PYTHON} ./sanity.py

components:
	${PYTHON} ./sqlite_database.py
	${PYTHON} ./sqlite_attach.py
	${PYTHON} ./sqlite_table.py
	${PYTHON} ./sqlite_references.py


# end of file 