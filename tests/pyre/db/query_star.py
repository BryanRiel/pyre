#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Exercise table declaration
"""


def test():
    # access to the package
    import pyre.db

    # declare a simple table
    class Weather(pyre.db.table, id="weather"):
        """
        The sample table from the postgres tutorial
        """

        # the fields
        city = pyre.db.str()
        date = pyre.db.date()
        low = pyre.db.int()
        high = pyre.db.int()
        precipitation = pyre.db.float()

    # and a matching trivial query
    class star(pyre.db.query, tables=Weather): pass

    # get a server
    server = pyre.db.server()
    # generate the SQL statement
    stmt = tuple(server.sql.select(star))
    print('\n'.join(stmt))
    assert stmt == (
        "SELECT",
        "    *",
        "  FROM weather;"
        )

    # all done
    return star


# main
if __name__ == "__main__":
    test()


# end of file 