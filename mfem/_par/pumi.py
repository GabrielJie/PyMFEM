# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pumi
else:
    import _pumi

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _pumi.SWIG_PyInstanceMethod_New
_swig_new_static_method = _pumi.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

MFEM_VERSION = _pumi.MFEM_VERSION

MFEM_VERSION_STRING = _pumi.MFEM_VERSION_STRING

MFEM_VERSION_TYPE = _pumi.MFEM_VERSION_TYPE

MFEM_VERSION_TYPE_RELEASE = _pumi.MFEM_VERSION_TYPE_RELEASE

MFEM_VERSION_TYPE_DEVELOPMENT = _pumi.MFEM_VERSION_TYPE_DEVELOPMENT

MFEM_VERSION_MAJOR = _pumi.MFEM_VERSION_MAJOR

MFEM_VERSION_MINOR = _pumi.MFEM_VERSION_MINOR

MFEM_VERSION_PATCH = _pumi.MFEM_VERSION_PATCH

MFEM_SOURCE_DIR = _pumi.MFEM_SOURCE_DIR

MFEM_INSTALL_DIR = _pumi.MFEM_INSTALL_DIR

MFEM_TIMER_TYPE = _pumi.MFEM_TIMER_TYPE

MFEM_HYPRE_VERSION = _pumi.MFEM_HYPRE_VERSION

class intp(object):
    r"""Proxy of C++ intp class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(intp self) -> intp"""
        _pumi.intp_swiginit(self, _pumi.new_intp())
    __swig_destroy__ = _pumi.delete_intp

    def assign(self, value):
        r"""assign(intp self, int value)"""
        return _pumi.intp_assign(self, value)
    assign = _swig_new_instance_method(_pumi.intp_assign)

    def value(self):
        r"""value(intp self) -> int"""
        return _pumi.intp_value(self)
    value = _swig_new_instance_method(_pumi.intp_value)

    def cast(self):
        r"""cast(intp self) -> int *"""
        return _pumi.intp_cast(self)
    cast = _swig_new_instance_method(_pumi.intp_cast)

    @staticmethod
    def frompointer(t):
        r"""frompointer(int * t) -> intp"""
        return _pumi.intp_frompointer(t)
    frompointer = _swig_new_static_method(_pumi.intp_frompointer)

# Register intp in _pumi:
_pumi.intp_swigregister(intp)

def intp_frompointer(t):
    r"""intp_frompointer(int * t) -> intp"""
    return _pumi.intp_frompointer(t)
intp_frompointer = _pumi.intp_frompointer

class doublep(object):
    r"""Proxy of C++ doublep class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(doublep self) -> doublep"""
        _pumi.doublep_swiginit(self, _pumi.new_doublep())
    __swig_destroy__ = _pumi.delete_doublep

    def assign(self, value):
        r"""assign(doublep self, double value)"""
        return _pumi.doublep_assign(self, value)
    assign = _swig_new_instance_method(_pumi.doublep_assign)

    def value(self):
        r"""value(doublep self) -> double"""
        return _pumi.doublep_value(self)
    value = _swig_new_instance_method(_pumi.doublep_value)

    def cast(self):
        r"""cast(doublep self) -> double *"""
        return _pumi.doublep_cast(self)
    cast = _swig_new_instance_method(_pumi.doublep_cast)

    @staticmethod
    def frompointer(t):
        r"""frompointer(double * t) -> doublep"""
        return _pumi.doublep_frompointer(t)
    frompointer = _swig_new_static_method(_pumi.doublep_frompointer)

# Register doublep in _pumi:
_pumi.doublep_swigregister(doublep)

def doublep_frompointer(t):
    r"""doublep_frompointer(double * t) -> doublep"""
    return _pumi.doublep_frompointer(t)
doublep_frompointer = _pumi.doublep_frompointer

import mfem._par.pgridfunc
import mfem._par.pfespace
import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.globals
import mfem._par.matrix
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets

def ParMesh2ParPumiMesh(pmesh):
    r"""ParMesh2ParPumiMesh(ParMesh pmesh) -> ParPumiMesh"""
    return _pumi.ParMesh2ParPumiMesh(pmesh)
ParMesh2ParPumiMesh = _pumi.ParMesh2ParPumiMesh
class PumiMesh(mfem._par.mesh.Mesh):
    r"""Proxy of C++ mfem::PumiMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, apf_mesh, generate_edges=0, refine=1, fix_orientation=True):
        r"""__init__(PumiMesh self, apf::Mesh2 * apf_mesh, int generate_edges=0, int refine=1, bool fix_orientation=True) -> PumiMesh"""
        _pumi.PumiMesh_swiginit(self, _pumi.new_PumiMesh(apf_mesh, generate_edges, refine, fix_orientation))

    def Load(self, *args):
        r"""
        Load(PumiMesh self, std::istream & input, int generate_edges=0, int refine=1, bool fix_orientation=True)
        Load(PumiMesh self, apf::Mesh2 * apf_mesh, int generate_edges=0, int refine=1, bool fix_orientation=True)
        """
        return _pumi.PumiMesh_Load(self, *args)
    Load = _swig_new_instance_method(_pumi.PumiMesh_Load)
    __swig_destroy__ = _pumi.delete_PumiMesh

# Register PumiMesh in _pumi:
_pumi.PumiMesh_swigregister(PumiMesh)

class ParPumiMesh(mfem._par.pmesh.ParMesh):
    r"""Proxy of C++ mfem::ParPumiMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, comm, apf_mesh, refine=1, fix_orientation=True):
        r"""__init__(ParPumiMesh self, MPI_Comm comm, apf::Mesh2 * apf_mesh, int refine=1, bool fix_orientation=True) -> ParPumiMesh"""
        _pumi.ParPumiMesh_swiginit(self, _pumi.new_ParPumiMesh(comm, apf_mesh, refine, fix_orientation))

    def RotationPUMItoMFEM(self, apf_mesh, tet, elemId):
        r"""RotationPUMItoMFEM(ParPumiMesh self, apf::Mesh2 * apf_mesh, apf::MeshEntity * tet, int elemId) -> int"""
        return _pumi.ParPumiMesh_RotationPUMItoMFEM(self, apf_mesh, tet, elemId)
    RotationPUMItoMFEM = _swig_new_instance_method(_pumi.ParPumiMesh_RotationPUMItoMFEM)

    def ParentXisPUMItoMFEM(self, apf_mesh, tet, elemId, pumi_xi, checkOrientation=True):
        r"""ParentXisPUMItoMFEM(ParPumiMesh self, apf::Mesh2 * apf_mesh, apf::MeshEntity * tet, int elemId, apf::NewArray< apf::Vector3 > & pumi_xi, bool checkOrientation=True) -> IntegrationRule"""
        return _pumi.ParPumiMesh_ParentXisPUMItoMFEM(self, apf_mesh, tet, elemId, pumi_xi, checkOrientation)
    ParentXisPUMItoMFEM = _swig_new_instance_method(_pumi.ParPumiMesh_ParentXisPUMItoMFEM)

    def ParentXisMFEMtoPUMI(self, apf_mesh, elemId, tet, mfem_xi, pumi_xi, checkOrientation=True):
        r"""ParentXisMFEMtoPUMI(ParPumiMesh self, apf::Mesh2 * apf_mesh, int elemId, apf::MeshEntity * tet, IntegrationRule mfem_xi, apf::NewArray< apf::Vector3 > & pumi_xi, bool checkOrientation=True)"""
        return _pumi.ParPumiMesh_ParentXisMFEMtoPUMI(self, apf_mesh, elemId, tet, mfem_xi, pumi_xi, checkOrientation)
    ParentXisMFEMtoPUMI = _swig_new_instance_method(_pumi.ParPumiMesh_ParentXisMFEMtoPUMI)

    def FieldMFEMtoPUMI(self, *args):
        r"""
        FieldMFEMtoPUMI(ParPumiMesh self, apf::Mesh2 * apf_mesh, ParGridFunction grid_vel, ParGridFunction grid_pr, apf::Field * vel_field, apf::Field * pr_field, apf::Field * vel_mag_field)
        FieldMFEMtoPUMI(ParPumiMesh self, apf::Mesh2 * apf_mesh, ParGridFunction grid_pr, apf::Field * pr_field, apf::Field * pr_mag_field)
        """
        return _pumi.ParPumiMesh_FieldMFEMtoPUMI(self, *args)
    FieldMFEMtoPUMI = _swig_new_instance_method(_pumi.ParPumiMesh_FieldMFEMtoPUMI)

    def VectorFieldMFEMtoPUMI(self, apf_mesh, grid_vel, vel_field, vel_mag_field):
        r"""VectorFieldMFEMtoPUMI(ParPumiMesh self, apf::Mesh2 * apf_mesh, ParGridFunction grid_vel, apf::Field * vel_field, apf::Field * vel_mag_field)"""
        return _pumi.ParPumiMesh_VectorFieldMFEMtoPUMI(self, apf_mesh, grid_vel, vel_field, vel_mag_field)
    VectorFieldMFEMtoPUMI = _swig_new_instance_method(_pumi.ParPumiMesh_VectorFieldMFEMtoPUMI)

    def NedelecFieldMFEMtoPUMI(self, apf_mesh, gf, nedelec_field):
        r"""NedelecFieldMFEMtoPUMI(ParPumiMesh self, apf::Mesh2 * apf_mesh, ParGridFunction gf, apf::Field * nedelec_field)"""
        return _pumi.ParPumiMesh_NedelecFieldMFEMtoPUMI(self, apf_mesh, gf, nedelec_field)
    NedelecFieldMFEMtoPUMI = _swig_new_instance_method(_pumi.ParPumiMesh_NedelecFieldMFEMtoPUMI)

    def UpdateMesh(self, AdaptedpMesh):
        r"""UpdateMesh(ParPumiMesh self, ParMesh AdaptedpMesh)"""
        return _pumi.ParPumiMesh_UpdateMesh(self, AdaptedpMesh)
    UpdateMesh = _swig_new_instance_method(_pumi.ParPumiMesh_UpdateMesh)

    def FieldPUMItoMFEM(self, apf_mesh, field, grid):
        r"""FieldPUMItoMFEM(ParPumiMesh self, apf::Mesh2 * apf_mesh, apf::Field * field, ParGridFunction grid)"""
        return _pumi.ParPumiMesh_FieldPUMItoMFEM(self, apf_mesh, field, grid)
    FieldPUMItoMFEM = _swig_new_instance_method(_pumi.ParPumiMesh_FieldPUMItoMFEM)
    __swig_destroy__ = _pumi.delete_ParPumiMesh

# Register ParPumiMesh in _pumi:
_pumi.ParPumiMesh_swigregister(ParPumiMesh)

class GridFunctionPumi(mfem._par.gridfunc.GridFunction):
    r"""Proxy of C++ mfem::GridFunctionPumi class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, m, PumiM, v_num_loc, mesh_order):
        r"""__init__(GridFunctionPumi self, Mesh m, apf::Mesh2 * PumiM, apf::Numbering * v_num_loc, int const mesh_order) -> GridFunctionPumi"""
        _pumi.GridFunctionPumi_swiginit(self, _pumi.new_GridFunctionPumi(m, PumiM, v_num_loc, mesh_order))
    __swig_destroy__ = _pumi.delete_GridFunctionPumi

# Register GridFunctionPumi in _pumi:
_pumi.GridFunctionPumi_swigregister(GridFunctionPumi)



