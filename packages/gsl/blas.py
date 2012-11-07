# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#
"""
Support for the BLAS interface
"""

# externals
from . import gsl


# the interface for doubles
# level 1
def ddot(x, y):
    """
    Compute the scalar product {x^T y}
    """
    # compute and return the result
    return gsl.blas_ddot(x.data, y.data)


def dnrm2(x):
    """
    Compute the Euclidean norm
    """
    # compute and return the result
    return gsl.blas_dnrm2(x.data)


def dasum(x):
    """
    Compute the sum of the absolute values of the entries in {x}
    """
    # compute and return the result
    return gsl.blas_dasum(x.data)


def daxpy(α, x, y):
    """
    Compute {α x + y} and store the result in {y}
    """
    # compute
    gsl.blas_daxpy(α, x.data, y.data)
    # and return the result {y}
    return y


# level 2
def dgemv(transpose, α, A, x, β, y):
    """
    Compute {y = α op(A) x + β y}
    """
    # compute
    gsl.blas_dgemv(transpose, α, A.data, x.data, β, y.data)
    # and return the result
    return y


def dtrmv(uplo, transpose, diag, A, x):
    """
    Compute {x = op(A) x}
    """
    # compute
    gsl.blas_dtrmv(uplo, transpose, diag, A.data, x.data)
    # and return the result
    return x


def dtrsv(uplo, transpose, diag, A, x):
    """
    Compute {x = inv(op(A)) x}
    """
    # compute
    gsl.blas_dtrsv(uplo, transpose, diag, A.data, x.data)
    # and return the result
    return x


def dsymv(uplo, α, A, x, β, y):
    """
    Compute {y = α A x + β y}
    """
    # compute
    gsl.blas_dsymv(uplo, α, A.data, x.data, β, y.data)
    # and return the result in {y}
    return y


def dsyr(uplo, α, x, A):
    """
    Compute {A = α x x^T + A}
    """
    # compute
    gsl.blas_dsyr(uplo, α, x.data, A.data)
    # and return the result in {A}
    return A


# level 3
def dgemm(tranA, tranB, α, A, B, β, C):
    """
    Compute {C = α op(A) op(B) + β C}
    """
    # compute
    gsl.blas_dgemm(tranA, tranB, α, A.data, B.data, β, C.data)
    # and return the result
    return C


# end of file 
