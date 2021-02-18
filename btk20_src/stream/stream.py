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
        mname = '.'.join((pkg, '_stream')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_stream')
    _stream = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_stream', [dirname(__file__)])
        except ImportError:
            import _stream
            return _stream
        try:
            _mod = imp.load_module('_stream', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _stream = swig_import_helper()
    del swig_import_helper
else:
    import _stream
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

class VectorCharFeatureStreamPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorCharFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorCharFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return _stream.VectorCharFeatureStreamPtr___iter__(self)

    def __deref__(self):
        return _stream.VectorCharFeatureStreamPtr___deref__(self)

    def __init__(self):
        this = _stream.new_VectorCharFeatureStreamPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _stream.delete_VectorCharFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.VectorCharFeatureStreamPtr_name(self)

    def size(self):
        return _stream.VectorCharFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.VectorCharFeatureStreamPtr_next(self, frameX)

    def reset(self):
        return _stream.VectorCharFeatureStreamPtr_reset(self)
VectorCharFeatureStreamPtr_swigregister = _stream.VectorCharFeatureStreamPtr_swigregister
VectorCharFeatureStreamPtr_swigregister(VectorCharFeatureStreamPtr)

class VectorShortFeatureStreamPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorShortFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorShortFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return _stream.VectorShortFeatureStreamPtr___iter__(self)

    def __deref__(self):
        return _stream.VectorShortFeatureStreamPtr___deref__(self)

    def __init__(self):
        this = _stream.new_VectorShortFeatureStreamPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _stream.delete_VectorShortFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.VectorShortFeatureStreamPtr_name(self)

    def size(self):
        return _stream.VectorShortFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.VectorShortFeatureStreamPtr_next(self, frameX)

    def reset(self):
        return _stream.VectorShortFeatureStreamPtr_reset(self)
VectorShortFeatureStreamPtr_swigregister = _stream.VectorShortFeatureStreamPtr_swigregister
VectorShortFeatureStreamPtr_swigregister(VectorShortFeatureStreamPtr)

class VectorFloatFeatureStreamPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorFloatFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorFloatFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return _stream.VectorFloatFeatureStreamPtr___iter__(self)

    def __deref__(self):
        return _stream.VectorFloatFeatureStreamPtr___deref__(self)

    def __init__(self):
        this = _stream.new_VectorFloatFeatureStreamPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _stream.delete_VectorFloatFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.VectorFloatFeatureStreamPtr_name(self)

    def size(self):
        return _stream.VectorFloatFeatureStreamPtr_size(self)

    def is_end(self):
        return _stream.VectorFloatFeatureStreamPtr_is_end(self)

    def next(self, frameX=-5):
        return _stream.VectorFloatFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.VectorFloatFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.VectorFloatFeatureStreamPtr_reset(self)
VectorFloatFeatureStreamPtr_swigregister = _stream.VectorFloatFeatureStreamPtr_swigregister
VectorFloatFeatureStreamPtr_swigregister(VectorFloatFeatureStreamPtr)

class VectorFeatureStreamPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return _stream.VectorFeatureStreamPtr___iter__(self)

    def __deref__(self):
        return _stream.VectorFeatureStreamPtr___deref__(self)

    def __init__(self):
        this = _stream.new_VectorFeatureStreamPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _stream.delete_VectorFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.VectorFeatureStreamPtr_name(self)

    def size(self):
        return _stream.VectorFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.VectorFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.VectorFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.VectorFeatureStreamPtr_reset(self)
VectorFeatureStreamPtr_swigregister = _stream.VectorFeatureStreamPtr_swigregister
VectorFeatureStreamPtr_swigregister(VectorFeatureStreamPtr)

class VectorComplexFeatureStreamPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorComplexFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorComplexFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return _stream.VectorComplexFeatureStreamPtr___iter__(self)

    def __deref__(self):
        return _stream.VectorComplexFeatureStreamPtr___deref__(self)

    def __init__(self):
        this = _stream.new_VectorComplexFeatureStreamPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _stream.delete_VectorComplexFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.VectorComplexFeatureStreamPtr_name(self)

    def size(self):
        return _stream.VectorComplexFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.VectorComplexFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.VectorComplexFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.VectorComplexFeatureStreamPtr_reset(self)
VectorComplexFeatureStreamPtr_swigregister = _stream.VectorComplexFeatureStreamPtr_swigregister
VectorComplexFeatureStreamPtr_swigregister(VectorComplexFeatureStreamPtr)

class PyVectorShortFeatureStreamPtr(VectorShortFeatureStreamPtr):
    __swig_setmethods__ = {}
    for _s in [VectorShortFeatureStreamPtr]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyVectorShortFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorShortFeatureStreamPtr]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyVectorShortFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _stream.new_PyVectorShortFeatureStreamPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        return _stream.PyVectorShortFeatureStreamPtr___deref__(self)
    __swig_destroy__ = _stream.delete_PyVectorShortFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.PyVectorShortFeatureStreamPtr_name(self)

    def size(self):
        return _stream.PyVectorShortFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.PyVectorShortFeatureStreamPtr_next(self, frameX)

    def reset(self):
        return _stream.PyVectorShortFeatureStreamPtr_reset(self)
PyVectorShortFeatureStreamPtr_swigregister = _stream.PyVectorShortFeatureStreamPtr_swigregister
PyVectorShortFeatureStreamPtr_swigregister(PyVectorShortFeatureStreamPtr)

class PyVectorFloatFeatureStreamPtr(VectorFloatFeatureStreamPtr):
    __swig_setmethods__ = {}
    for _s in [VectorFloatFeatureStreamPtr]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyVectorFloatFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorFloatFeatureStreamPtr]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyVectorFloatFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _stream.new_PyVectorFloatFeatureStreamPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        return _stream.PyVectorFloatFeatureStreamPtr___deref__(self)
    __swig_destroy__ = _stream.delete_PyVectorFloatFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.PyVectorFloatFeatureStreamPtr_name(self)

    def size(self):
        return _stream.PyVectorFloatFeatureStreamPtr_size(self)

    def is_end(self):
        return _stream.PyVectorFloatFeatureStreamPtr_is_end(self)

    def next(self, frameX=-5):
        return _stream.PyVectorFloatFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.PyVectorFloatFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.PyVectorFloatFeatureStreamPtr_reset(self)
PyVectorFloatFeatureStreamPtr_swigregister = _stream.PyVectorFloatFeatureStreamPtr_swigregister
PyVectorFloatFeatureStreamPtr_swigregister(PyVectorFloatFeatureStreamPtr)

class PyVectorFeatureStreamPtr(VectorFeatureStreamPtr):
    __swig_setmethods__ = {}
    for _s in [VectorFeatureStreamPtr]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyVectorFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorFeatureStreamPtr]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyVectorFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _stream.new_PyVectorFeatureStreamPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        return _stream.PyVectorFeatureStreamPtr___deref__(self)
    __swig_destroy__ = _stream.delete_PyVectorFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.PyVectorFeatureStreamPtr_name(self)

    def size(self):
        return _stream.PyVectorFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.PyVectorFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.PyVectorFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.PyVectorFeatureStreamPtr_reset(self)
PyVectorFeatureStreamPtr_swigregister = _stream.PyVectorFeatureStreamPtr_swigregister
PyVectorFeatureStreamPtr_swigregister(PyVectorFeatureStreamPtr)

class PyVectorComplexFeatureStreamPtr(VectorComplexFeatureStreamPtr):
    __swig_setmethods__ = {}
    for _s in [VectorComplexFeatureStreamPtr]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyVectorComplexFeatureStreamPtr, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorComplexFeatureStreamPtr]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyVectorComplexFeatureStreamPtr, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _stream.new_PyVectorComplexFeatureStreamPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        return _stream.PyVectorComplexFeatureStreamPtr___deref__(self)
    __swig_destroy__ = _stream.delete_PyVectorComplexFeatureStreamPtr
    __del__ = lambda self: None

    def name(self):
        return _stream.PyVectorComplexFeatureStreamPtr_name(self)

    def size(self):
        return _stream.PyVectorComplexFeatureStreamPtr_size(self)

    def next(self, frameX=-5):
        return _stream.PyVectorComplexFeatureStreamPtr_next(self, frameX)

    def current(self):
        return _stream.PyVectorComplexFeatureStreamPtr_current(self)

    def reset(self):
        return _stream.PyVectorComplexFeatureStreamPtr_reset(self)
PyVectorComplexFeatureStreamPtr_swigregister = _stream.PyVectorComplexFeatureStreamPtr_swigregister
PyVectorComplexFeatureStreamPtr_swigregister(PyVectorComplexFeatureStreamPtr)

class FileHandlerPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileHandlerPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileHandlerPtr, name)
    __repr__ = _swig_repr

    def __init__(self, filename, mode):
        this = _stream.new_FileHandlerPtr(filename, mode)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        return _stream.FileHandlerPtr___deref__(self)
    __swig_destroy__ = _stream.delete_FileHandlerPtr
    __del__ = lambda self: None

    def read_int(self):
        return _stream.FileHandlerPtr_read_int(self)

    def read_string(self):
        return _stream.FileHandlerPtr_read_string(self)

    def write_int(self, val):
        return _stream.FileHandlerPtr_write_int(self, val)

    def write_string(self, val):
        return _stream.FileHandlerPtr_write_string(self, val)
FileHandlerPtr_swigregister = _stream.FileHandlerPtr_swigregister
FileHandlerPtr_swigregister(FileHandlerPtr)

# This file is compatible with both classic and new-style classes.


