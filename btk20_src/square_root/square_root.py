# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_square_root')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_square_root')
    _square_root = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_square_root', [dirname(__file__)])
        except ImportError:
            import _square_root
            return _square_root
        try:
            _mod = imp.load_module('_square_root', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _square_root = swig_import_helper()
    del swig_import_helper
else:
    import _square_root
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def cholesky_backsub(A, x):
    return _square_root.cholesky_backsub(A, x)
cholesky_backsub = _square_root.cholesky_backsub

def vector_matrix_product(vec, mat, D):
    return _square_root.vector_matrix_product(vec, mat, D)
vector_matrix_product = _square_root.vector_matrix_product

def make_conjugate_symmetric(mat):
    return _square_root.make_conjugate_symmetric(mat)
make_conjugate_symmetric = _square_root.make_conjugate_symmetric

def cholesky_forwardsub(A, x):
    return _square_root.cholesky_forwardsub(A, x)
cholesky_forwardsub = _square_root.cholesky_forwardsub

def cholesky_forwardsub_complex(lt, rhs, lhs, conjugate=False):
    return _square_root.cholesky_forwardsub_complex(lt, rhs, lhs, conjugate)
cholesky_forwardsub_complex = _square_root.cholesky_forwardsub_complex

def cholesky_backsub_complex(lt, rhs, lhs, conjugate=False):
    return _square_root.cholesky_backsub_complex(lt, rhs, lhs, conjugate)
cholesky_backsub_complex = _square_root.cholesky_backsub_complex

def rank_one_update_cholesky_factor(A11, alpha_m, c_m):
    return _square_root.rank_one_update_cholesky_factor(A11, alpha_m, c_m)
rank_one_update_cholesky_factor = _square_root.rank_one_update_cholesky_factor

def propagate_covar_square_root_real(A11, A12, A21, A22, flag=False):
    return _square_root.propagate_covar_square_root_real(A11, A12, A21, A22, flag)
propagate_covar_square_root_real = _square_root.propagate_covar_square_root_real

def sweep_lower_triangular(A, B):
    return _square_root.sweep_lower_triangular(A, B)
sweep_lower_triangular = _square_root.sweep_lower_triangular

def propagate_covar_square_root_step1(A12, A22):
    return _square_root.propagate_covar_square_root_step1(A12, A22)
propagate_covar_square_root_step1 = _square_root.propagate_covar_square_root_step1

def propagate_covar_square_root_step2a(A11, A12, A21, A22):
    return _square_root.propagate_covar_square_root_step2a(A11, A12, A21, A22)
propagate_covar_square_root_step2a = _square_root.propagate_covar_square_root_step2a

def propagate_covar_square_root_step2b(A22):
    return _square_root.propagate_covar_square_root_step2b(A22)
propagate_covar_square_root_step2b = _square_root.propagate_covar_square_root_step2b

def propagate_covar_square_root(A11, A12, A21, A22):
    return _square_root.propagate_covar_square_root(A11, A12, A21, A22)
propagate_covar_square_root = _square_root.propagate_covar_square_root

def propagate_info_square_root(sqrt_Pm_inv, A12, a_21, a_22, rankOneA12=True):
    return _square_root.propagate_info_square_root(sqrt_Pm_inv, A12, a_21, a_22, rankOneA12)
propagate_info_square_root = _square_root.propagate_info_square_root

def propagate_info_square_root_step2_rls(sqrt_Pm_inv, a_12, a_21, a_22):
    return _square_root.propagate_info_square_root_step2_rls(sqrt_Pm_inv, a_12, a_21, a_22)
propagate_info_square_root_step2_rls = _square_root.propagate_info_square_root_step2_rls

def propagate_info_square_root_rls(sqrt_Pm_inv, a_12, a_21, a_22):
    return _square_root.propagate_info_square_root_rls(sqrt_Pm_inv, a_12, a_21, a_22)
propagate_info_square_root_rls = _square_root.propagate_info_square_root_rls

def add_diagonal_loading(sqrt_Pm_inv, dim, wght):
    return _square_root.add_diagonal_loading(sqrt_Pm_inv, dim, wght)
add_diagonal_loading = _square_root.add_diagonal_loading

def cholesky_diagonal(v, m):
    return _square_root.cholesky_diagonal(v, m)
cholesky_diagonal = _square_root.cholesky_diagonal

def square_diagonal(v, m):
    return _square_root.square_diagonal(v, m)
square_diagonal = _square_root.square_diagonal
# This file is compatible with both classic and new-style classes.


