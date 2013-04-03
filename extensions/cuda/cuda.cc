// -*- C++ -*-
// 
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2013 all rights reserved
// 

#include <portinfo>
#include <Python.h>

// journal
#include <pyre/journal.h>

// CUDA
#include <cuda.h>

// boilerplate
#include "metadata.h"
#include "exceptions.h"
// the module method declarations
#include "discover.h"


// put everything in my private namespace
namespace pyre {
    namespace extensions {
        namespace cuda {

            // the module method table
            PyMethodDef methods[] = {
                // module metadata
                // copyright
                { copyright__name__, copyright, METH_VARARGS, copyright__doc__ },
                // version
                { version__name__, version, METH_VARARGS, version__doc__ },
                // license
                { license__name__, license, METH_VARARGS, license__doc__ },

                // device discovery and other administrative tasks
                // discover
                { discover__name__, discover, METH_VARARGS, discover__doc__ },

                // sentinel
                {0, 0, 0, 0}
            };


            // the module documentation string
            const char * const doc = "provides access to CUDA enabled devices";

            // the module definition structure
            PyModuleDef module = {
                // header
                PyModuleDef_HEAD_INIT,
                // the name of the module
                "cuda",
                // the module documentation string
                doc,
                // size of the per-interpreter state of the module; -1 if this state is global
                -1,
                // the methods defined in this module
                methods
            };

        } // of namespace cuda
    } // of namespace extensions
} // of namespace pyre

// initialization function for the module
// *must* be called PyInit_cuda
PyMODINIT_FUNC
PyInit_cuda()
{
    // create the module
    PyObject * module = PyModule_Create(&pyre::extensions::cuda::module);
    // check whether module creation succeeded and raise an exception if not
    if (!module) {
        return module;
    }

#ifdef USE_CUDA_CRIVER_API
    // initialize cuda
    CUresult status = cuInit(0);
    // check
    if (status != CUDA_SUCCESS) {
        // something went wrong
        PyErr_SetString(PyExc_ImportError, "CUDA initialization failed");
        // raise an exception
        return 0;
    }
#endif

    // otherwise, we are good to go; register the module exceptions
    pyre::extensions::cuda::registerExceptionHierarchy(module);

    // and return the newly created module
    return module;
}


// end of file
