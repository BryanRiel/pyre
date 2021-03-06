// -*- C++ -*-
//
// michael a.g. aïvázis
// orthologue
// (c) 1998-2018 all rights reserved
//

// given a file named "grid.dat" in the current directory, use the low level interface to map
// it into memory

// portability
#include <portinfo>
// externals
#include <unistd.h>
// support
#include <pyre/memory.h>

// entry point
int main() {
    // the cell type
    typedef double cell_t;
    // desired size
    size_t page = ::getpagesize();
    // the name of the file
    pyre::memory::uri_t name {"grid.dat"};

    // the file size, in bytes
    size_t size = 2*page;
    // turn on the info channel
    // pyre::journal::debug_t("pyre.memory.direct").activate();
    // map a buffer over the file; if anything goes wrong, we'll get an exception
    void * buffer = pyre::memory::direct_t<cell_t>::map(name, size, 0, true);
    // and unmap it
    pyre::memory::direct_t<char>::unmap(buffer, size);

    // all done
    return 0;
}

// end of file
