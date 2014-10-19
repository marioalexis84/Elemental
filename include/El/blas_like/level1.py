#
#  Copyright (c) 2009-2014, Jack Poulson
#  All rights reserved.
#
#  This file is part of Elemental and is under the BSD 2-Clause License, 
#  which can be found in the LICENSE file in the root directory, or at 
#  http://opensource.org/licenses/BSD-2-Clause
#
from ..core import *

from ctypes import CFUNCTYPE

# BLAS 1
# ======

# Axpy
# ----
lib.ElAxpy_i.argtypes = [iType,c_void_p,c_void_p]
lib.ElAxpy_i.restype = c_uint
lib.ElAxpy_s.argtypes = [sType,c_void_p,c_void_p]
lib.ElAxpy_s.restype = c_uint
lib.ElAxpy_d.argtypes = [dType,c_void_p,c_void_p]
lib.ElAxpy_d.restype = c_uint
lib.ElAxpy_c.argtypes = [cType,c_void_p,c_void_p]
lib.ElAxpy_c.restype = c_uint
lib.ElAxpy_z.argtypes = [zType,c_void_p,c_void_p]
lib.ElAxpy_z.restype = c_uint
def Axpy(alphaPre,X,Y):
  if type(X) is not type(Y): raise Exception('Types of X and Y must match')
  if X.tag != Y.tag: raise Exception('Datatypes of X and Y must match')
  alpha = TagToType(X.tag)(alphaPre)
  args = [alpha,X.obj,Y.obj]
  if type(X) is Matrix:
    if   X.tag == iTag: lib.ElAxpy_i(*args)
    elif X.tag == sTag: lib.ElAxpy_s(*args)
    elif X.tag == dTag: lib.ElAxpy_d(*args)
    elif X.tag == cTag: lib.ElAxpy_c(*args)
    elif X.tag == zTag: lib.ElAxpy_z(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == iTag: lib.ElAxpyDist_i(*args)
    elif X.tag == sTag: lib.ElAxpyDist_s(*args)
    elif X.tag == dTag: lib.ElAxpyDist_d(*args)
    elif X.tag == cTag: lib.ElAxpyDist_c(*args)
    elif X.tag == zTag: lib.ElAxpyDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# AxpyTriangle
# ------------
lib.ElAxpyTriangle_i.argtypes = [c_uint,iType,c_void_p,c_void_p]
lib.ElAxpyTriangle_i.restype = c_uint
lib.ElAxpyTriangle_s.argtypes = [c_uint,sType,c_void_p,c_void_p]
lib.ElAxpyTriangle_s.restype = c_uint
lib.ElAxpyTriangle_d.argtypes = [c_uint,dType,c_void_p,c_void_p]
lib.ElAxpyTriangle_d.restype = c_uint
lib.ElAxpyTriangle_c.argtypes = [c_uint,cType,c_void_p,c_void_p]
lib.ElAxpyTriangle_c.restype = c_uint
lib.ElAxpyTriangle_z.argtypes = [c_uint,zType,c_void_p,c_void_p]
lib.ElAxpyTriangle_z.restype = c_uint
def AxpyTriangle(uplo,alphaPre,X,Y):
  if type(X) is not type(Y): raise Exception('Types of X and Y must match')
  if X.tag != Y.tag: raise Exception('Datatypes of X and Y must match')
  alpha = TagToType(X.tag)(alphaPre)
  args = [uplo,alpha,X.obj,Y.obj]
  if type(X) is Matrix:
    if   X.tag == iTag: lib.ElAxpyTriangle_i(*args)
    elif X.tag == sTag: lib.ElAxpyTriangle_s(*args)
    elif X.tag == dTag: lib.ElAxpyTriangle_d(*args)
    elif X.tag == cTag: lib.ElAxpyTriangle_c(*args)
    elif X.tag == zTag: lib.ElAxpyTriangle_z(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == iTag: lib.ElAxpyTriangleDist_i(*args)
    elif X.tag == sTag: lib.ElAxpyTriangleDist_s(*args)
    elif X.tag == dTag: lib.ElAxpyTriangleDist_d(*args)
    elif X.tag == cTag: lib.ElAxpyTriangleDist_c(*args)
    elif X.tag == zTag: lib.ElAxpyTriangleDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Conjugate
# ---------
lib.ElConjugate_c.argtypes = [c_void_p]
lib.ElConjugate_c.restype = c_uint
lib.ElConjugate_z.argtypes = [c_void_p]
lib.ElConjugate_z.restype = c_uint
lib.ElConjugateDist_c.argtypes = [c_void_p]
lib.ElConjugateDist_c.restype = c_uint
lib.ElConjugateDist_z.argtypes = [c_void_p]
lib.ElConjugateDist_z.restype = c_uint
def Conjugate(A):
  args = [A.obj]
  if type(A) is Matrix:
    if   A.tag == cTag: lib.ElConjugate_c(*args)
    elif A.tag == zTag: lib.ElConjugate_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == cTag: lib.ElConjugateDist_c(*args)
    elif A.tag == zTag: lib.ElConjugateDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Copy
# ----
lib.ElCopy_s.argtypes = [c_void_p,c_void_p]
lib.ElCopy_s.restype = c_uint
lib.ElCopy_d.argtypes = [c_void_p,c_void_p]
lib.ElCopy_d.restype = c_uint
lib.ElCopy_c.argtypes = [c_void_p,c_void_p]
lib.ElCopy_c.restype = c_uint
lib.ElCopy_z.argtypes = [c_void_p,c_void_p]
lib.ElCopy_z.restype = c_uint
lib.ElCopyDist_s.argtypes = [c_void_p,c_void_p]
lib.ElCopyDist_s.restype = c_uint
lib.ElCopyDist_d.argtypes = [c_void_p,c_void_p]
lib.ElCopyDist_d.restype = c_uint
lib.ElCopyDist_c.argtypes = [c_void_p,c_void_p]
lib.ElCopyDist_c.restype = c_uint
lib.ElCopyDist_z.argtypes = [c_void_p,c_void_p]
lib.ElCopyDist_z.restype = c_uint
def Copy(A,B):
  if A.tag != B.tag:
    raise Exception('Copying between datatypes is not yet supported in Python')
  if type(A) is not type(B): raise Exception('Matrix types must match')
  args = [A.obj,B.obj]
  if type(A) is Matrix:
    if   B.tag == iTag: lib.ElCopy_i(*args)
    elif B.tag == sTag: lib.ElCopy_s(*args)
    elif B.tag == dTag: lib.ElCopy_d(*args)
    elif B.tag == cTag: lib.ElCopy_c(*args)
    elif B.tag == zTag: lib.ElCopy_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   B.tag == iTag: lib.ElCopyDist_i(*args)
    elif B.tag == sTag: lib.ElCopyDist_s(*args)
    elif B.tag == dTag: lib.ElCopyDist_d(*args)
    elif B.tag == cTag: lib.ElCopyDist_c(*args)
    elif B.tag == zTag: lib.ElCopyDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Diagonal scale
# --------------
lib.ElDiagonalScale_i.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScale_i.restype = c_uint
lib.ElDiagonalScale_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScale_s.restype = c_uint
lib.ElDiagonalScale_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScale_d.restype = c_uint
lib.ElDiagonalScale_c.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalScale_c.restype = c_uint
lib.ElDiagonalScale_z.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalScale_z.restype = c_uint
lib.ElDiagonalScaleDist_i.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScaleDist_i.restype = c_uint
lib.ElDiagonalScaleDist_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScaleDist_s.restype = c_uint
lib.ElDiagonalScaleDist_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalScaleDist_d.restype = c_uint
lib.ElDiagonalScaleDist_c.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalScaleDist_c.restype = c_uint
lib.ElDiagonalScaleDist_z.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalScaleDist_z.restype = c_uint
def DiagonalScale(side,orient,d,X):
  if type(d) is not type(X): raise Exception('Matrix types must match')
  if d.tag != X.tag: raise Exception('Matrix datatypes must match')
  args = [side,d.obj,X.obj]
  argsCpx = [side,orient,d.obj,X.obj]
  if type(X) is Matrix:
    if   X.tag == iTag: lib.ElDiagonalScale_i(*args)
    elif X.tag == sTag: lib.ElDiagonalScale_s(*args)
    elif X.tag == dTag: lib.ElDiagonalScale_d(*args)
    elif X.tag == cTag: lib.ElDiagonalScale_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalScale_z(*argsCpx)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == iTag: lib.ElDiagonalScaleDist_i(*args)
    elif X.tag == sTag: lib.ElDiagonalScaleDist_s(*args)
    elif X.tag == dTag: lib.ElDiagonalScaleDist_d(*args)
    elif X.tag == cTag: lib.ElDiagonalScaleDist_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalScaleDist_z(*argsCpx)
    else: DataExcept()
  else: TypeExcept()

# Diagonal scale trapezoid
# ------------------------
lib.ElDiagonalScaleTrapezoid_i.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoid_i.restype = c_uint
lib.ElDiagonalScaleTrapezoid_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoid_s.restype = c_uint
lib.ElDiagonalScaleTrapezoid_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoid_d.restype = c_uint
lib.ElDiagonalScaleTrapezoid_c.argtypes = \
  [c_uint,c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoid_c.restype = c_uint
lib.ElDiagonalScaleTrapezoid_z.argtypes = \
  [c_uint,c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoid_z.restype = c_uint
lib.ElDiagonalScaleTrapezoidDist_i.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoidDist_i.restype = c_uint
lib.ElDiagonalScaleTrapezoidDist_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoidDist_s.restype = c_uint
lib.ElDiagonalScaleTrapezoidDist_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoidDist_d.restype = c_uint
lib.ElDiagonalScaleTrapezoidDist_c.argtypes = \
  [c_uint,c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoidDist_c.restype = c_uint
lib.ElDiagonalScaleTrapezoidDist_z.argtypes = \
  [c_uint,c_uint,c_uint,c_void_p,c_void_p,iType]
lib.ElDiagonalScaleTrapezoidDist_z.restype = c_uint
def DiagonalScaleTrapezoid(side,uplo,orient,d,X,offset=0):
  if type(d) is not type(X): raise Exception('Matrix types must match')
  if d.tag != X.tag: raise Exception('Matrix datatypes must match')
  args = [side,uplo,d.obj,X.obj,offset]
  argsCpx = [side,uplo,orient,d.obj,X.obj,offset]
  if type(X) is Matrix:
    if   X.tag == iTag: lib.ElDiagonalScaleTrapezoid_i(*args)
    elif X.tag == sTag: lib.ElDiagonalScaleTrapezoid_s(*args)
    elif X.tag == dTag: lib.ElDiagonalScaleTrapezoid_d(*args)
    elif X.tag == cTag: lib.ElDiagonalScaleTrapezoid_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalScaleTrapezoid_z(*argsCpx)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == iTag: lib.ElDiagonalScaleTrapezoidDist_i(*args)
    elif X.tag == sTag: lib.ElDiagonalScaleTrapezoidDist_s(*args)
    elif X.tag == dTag: lib.ElDiagonalScaleTrapezoidDist_d(*args)
    elif X.tag == cTag: lib.ElDiagonalScaleTrapezoidDist_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalScaleTrapezoidDist_z(*argsCpx)
    else: DataExcept()
  else: TypeExcept()

# Diagonal solve
# --------------
lib.ElDiagonalSolve_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolve_s.restype = c_uint
lib.ElDiagonalSolve_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolve_d.restype = c_uint
lib.ElDiagonalSolve_c.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolve_c.restype = c_uint
lib.ElDiagonalSolve_z.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolve_z.restype = c_uint
lib.ElDiagonalSolveDist_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolveDist_s.restype = c_uint
lib.ElDiagonalSolveDist_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolveDist_d.restype = c_uint
lib.ElDiagonalSolveDist_c.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolveDist_c.restype = c_uint
lib.ElDiagonalSolveDist_z.argtypes = [c_uint,c_uint,c_void_p,c_void_p]
lib.ElDiagonalSolveDist_z.restype = c_uint
def DiagonalSolve(side,orient,d,X):
  if type(d) is not type(X): raise Exception('Matrix types must match')
  if d.tag != X.tag: raise Exception('Matrix datatypes must match')
  args = [side,d.obj,X.obj]
  argsCpx = [side,orient,d.obj,X.obj]
  if type(X) is Matrix:
    if   X.tag == sTag: lib.ElDiagonalSolve_s(*args)
    elif X.tag == dTag: lib.ElDiagonalSolve_d(*args)
    elif X.tag == cTag: lib.ElDiagonalSolve_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalSolve_z(*argsCpx)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == sTag: lib.ElDiagonalSolveDist_s(*args)
    elif X.tag == dTag: lib.ElDiagonalSolveDist_d(*args)
    elif X.tag == cTag: lib.ElDiagonalSolveDist_c(*argsCpx)
    elif X.tag == zTag: lib.ElDiagonalSolveDist_z(*argsCpx)
    else: DataExcept()
  else: TypeExcept()

# Dot
# ---
lib.ElDot_i.argtypes = [c_void_p,c_void_p,POINTER(iType)]
lib.ElDot_i.restype = c_uint
lib.ElDot_s.argtypes = [c_void_p,c_void_p,POINTER(sType)]
lib.ElDot_s.restype = c_uint
lib.ElDot_d.argtypes = [c_void_p,c_void_p,POINTER(dType)]
lib.ElDot_d.restype = c_uint
lib.ElDot_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElDot_c.restype = c_uint
lib.ElDot_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElDot_z.restype = c_uint
lib.ElDotDist_i.argtypes = [c_void_p,c_void_p,POINTER(iType)]
lib.ElDotDist_i.restype = c_uint
lib.ElDotDist_s.argtypes = [c_void_p,c_void_p,POINTER(sType)]
lib.ElDotDist_s.restype = c_uint
lib.ElDotDist_d.argtypes = [c_void_p,c_void_p,POINTER(dType)]
lib.ElDotDist_d.restype = c_uint
lib.ElDotDist_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElDotDist_c.restype = c_uint
lib.ElDotDist_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElDotDist_z.restype = c_uint
def Dot(A,B):
  if type(A) is not type(B): raise Exception('Types of A and B must match')
  if A.tag != B.tag: raise Exception('Datatypes of A and B must match')
  prod = TagToType(A.tag)()
  args = [A.obj,B.obj,pointer(prod)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElDot_i(*args) 
    elif A.tag == sTag: lib.ElDot_s(*args)
    elif A.tag == dTag: lib.ElDot_d(*args)
    elif A.tag == cTag: lib.ElDot_c(*args)
    elif A.tag == zTag: lib.ElDot_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElDotDist_i(*args) 
    elif A.tag == sTag: lib.ElDotDist_s(*args)
    elif A.tag == dTag: lib.ElDotDist_d(*args)
    elif A.tag == cTag: lib.ElDotDist_c(*args)
    elif A.tag == zTag: lib.ElDotDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return prod

# Dotu
# ----
lib.ElDot_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElDot_c.restype = c_uint
lib.ElDot_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElDot_z.restype = c_uint
lib.ElDotDist_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElDotDist_c.restype = c_uint
lib.ElDotDist_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElDotDist_z.restype = c_uint
def Dotu(A,B):
  if type(A) is not type(B): raise Exception('Types of A and B must match')
  if A.tag != B.tag: raise Exception('Datatypes of A and B must match')
  prod = TagToType(A.tag)()
  args = [A.obj,B.obj,pointer(prod)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElDot_i(*args) 
    elif A.tag == sTag: lib.ElDot_s(*args)
    elif A.tag == dTag: lib.ElDot_d(*args)
    elif A.tag == cTag: lib.ElDotu_c(*args)
    elif A.tag == zTag: lib.ElDotu_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElDotDist_i(*args) 
    elif A.tag == sTag: lib.ElDotDist_s(*args)
    elif A.tag == dTag: lib.ElDotDist_d(*args)
    elif A.tag == cTag: lib.ElDotuDist_c(*args)
    elif A.tag == zTag: lib.ElDotuDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return prod

# Entrywise fill
# --------------
lib.ElEntrywiseFill_i.argtypes = [c_void_p,CFUNCTYPE(iType)]
lib.ElEntrywiseFill_i.restype = c_uint
lib.ElEntrywiseFill_s.argtypes = [c_void_p,CFUNCTYPE(sType)]
lib.ElEntrywiseFill_s.restype = c_uint
lib.ElEntrywiseFill_d.argtypes = [c_void_p,CFUNCTYPE(dType)]
lib.ElEntrywiseFill_d.restype = c_uint
lib.ElEntrywiseFill_c.argtypes = [c_void_p,CFUNCTYPE(cType)]
lib.ElEntrywiseFill_c.restype = c_uint
lib.ElEntrywiseFill_z.argtypes = [c_void_p,CFUNCTYPE(zType)]
lib.ElEntrywiseFill_z.restype = c_uint
lib.ElEntrywiseFillDist_i.argtypes = [c_void_p,CFUNCTYPE(iType)]
lib.ElEntrywiseFillDist_i.restype = c_uint
lib.ElEntrywiseFillDist_s.argtypes = [c_void_p,CFUNCTYPE(sType)]
lib.ElEntrywiseFillDist_s.restype = c_uint
lib.ElEntrywiseFillDist_d.argtypes = [c_void_p,CFUNCTYPE(dType)]
lib.ElEntrywiseFillDist_d.restype = c_uint
lib.ElEntrywiseFillDist_c.argtypes = [c_void_p,CFUNCTYPE(cType)]
lib.ElEntrywiseFillDist_c.restype = c_uint
lib.ElEntrywiseFillDist_z.argtypes = [c_void_p,CFUNCTYPE(zType)]
lib.ElEntrywiseFillDist_z.restype = c_uint
def EntrywiseFill(A,fill):
  cFill = CFUNCTYPE(TagToType(A.tag))(fill)
  args = [A.obj,cFill]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElEntrywiseFill_i(*args)
    elif A.tag == sTag: lib.ElEntrywiseFill_s(*args)
    elif A.tag == dTag: lib.ElEntrywiseFill_d(*args)
    elif A.tag == cTag: lib.ElEntrywiseFill_c(*args)
    elif A.tag == zTag: lib.ElEntrywiseFill_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElEntrywiseFillDist_i(*args)
    elif A.tag == sTag: lib.ElEntrywiseFillDist_s(*args)
    elif A.tag == dTag: lib.ElEntrywiseFillDist_d(*args)
    elif A.tag == cTag: lib.ElEntrywiseFillDist_c(*args)
    elif A.tag == zTag: lib.ElEntrywiseFillDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Entrywise map
# -------------
lib.ElEntrywiseMap_i.argtypes = [c_void_p,CFUNCTYPE(iType,iType)]
lib.ElEntrywiseMap_i.restype = c_uint
lib.ElEntrywiseMap_s.argtypes = [c_void_p,CFUNCTYPE(sType,sType)]
lib.ElEntrywiseMap_s.restype = c_uint
lib.ElEntrywiseMap_d.argtypes = [c_void_p,CFUNCTYPE(dType,dType)]
lib.ElEntrywiseMap_d.restype = c_uint
lib.ElEntrywiseMap_c.argtypes = [c_void_p,CFUNCTYPE(cType,cType)]
lib.ElEntrywiseMap_c.restype = c_uint
lib.ElEntrywiseMap_z.argtypes = [c_void_p,CFUNCTYPE(zType,zType)]
lib.ElEntrywiseMap_z.restype = c_uint
lib.ElEntrywiseMapDist_i.argtypes = [c_void_p,CFUNCTYPE(iType,iType)]
lib.ElEntrywiseMapDist_i.restype = c_uint
lib.ElEntrywiseMapDist_s.argtypes = [c_void_p,CFUNCTYPE(sType,sType)]
lib.ElEntrywiseMapDist_s.restype = c_uint
lib.ElEntrywiseMapDist_d.argtypes = [c_void_p,CFUNCTYPE(dType,dType)]
lib.ElEntrywiseMapDist_d.restype = c_uint
lib.ElEntrywiseMapDist_c.argtypes = [c_void_p,CFUNCTYPE(cType,cType)]
lib.ElEntrywiseMapDist_c.restype = c_uint
lib.ElEntrywiseMapDist_z.argtypes = [c_void_p,CFUNCTYPE(zType,zType)]
lib.ElEntrywiseMapDist_z.restype = c_uint
def EntrywiseMap(A,mapFunc):
  cMap = CFUNCTYPE(TagToType(A.tag),TagToType(A.tag))(mapFunc)
  args = [A.obj,cMap]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElEntrywiseMap_i(*args)
    elif A.tag == sTag: lib.ElEntrywiseMap_s(*args)
    elif A.tag == dTag: lib.ElEntrywiseMap_d(*args)
    elif A.tag == cTag: lib.ElEntrywiseMap_c(*args)
    elif A.tag == zTag: lib.ElEntrywiseMap_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElEntrywiseMapDist_i(*args)
    elif A.tag == sTag: lib.ElEntrywiseMapDist_s(*args)
    elif A.tag == dTag: lib.ElEntrywiseMapDist_d(*args)
    elif A.tag == cTag: lib.ElEntrywiseMapDist_c(*args)
    elif A.tag == zTag: lib.ElEntrywiseMapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Fill
# ----
lib.ElFill_i.argtypes = [c_void_p,iType]
lib.ElFill_i.restype = c_uint
lib.ElFill_s.argtypes = [c_void_p,sType]
lib.ElFill_s.restype = c_uint
lib.ElFill_d.argtypes = [c_void_p,dType]
lib.ElFill_d.restype = c_uint
lib.ElFill_c.argtypes = [c_void_p,cType]
lib.ElFill_c.restype = c_uint
lib.ElFill_z.argtypes = [c_void_p,zType]
lib.ElFill_z.restype = c_uint
lib.ElFillDist_i.argtypes = [c_void_p,iType]
lib.ElFillDist_i.restype = c_uint
lib.ElFillDist_s.argtypes = [c_void_p,sType]
lib.ElFillDist_s.restype = c_uint
lib.ElFillDist_d.argtypes = [c_void_p,dType]
lib.ElFillDist_d.restype = c_uint
lib.ElFillDist_c.argtypes = [c_void_p,cType]
lib.ElFillDist_c.restype = c_uint
lib.ElFillDist_z.argtypes = [c_void_p,zType]
lib.ElFillDist_z.restype = c_uint
def Fill(A,alphaPre):
  alpha = TagToType(A.tag)(alphaPre)
  args = [A.obj,alpha]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElFill_i(*args)
    elif A.tag == sTag: lib.ElFill_s(*args)
    elif A.tag == dTag: lib.ElFill_d(*args)
    elif A.tag == cTag: lib.ElFill_c(*args)
    elif A.tag == zTag: lib.ElFill_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElFillDist_i(*args)
    elif A.tag == sTag: lib.ElFillDist_s(*args)
    elif A.tag == dTag: lib.ElFillDist_d(*args)
    elif A.tag == cTag: lib.ElFillDist_c(*args)
    elif A.tag == zTag: lib.ElFillDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Hadamard
# --------
lib.ElHadamard_i.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamard_i.restype = c_uint
lib.ElHadamard_s.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamard_s.restype = c_uint
lib.ElHadamard_d.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamard_d.restype = c_uint
lib.ElHadamard_c.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamard_c.restype = c_uint
lib.ElHadamard_z.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamard_z.restype = c_uint
lib.ElHadamardDist_i.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamardDist_i.restype = c_uint
lib.ElHadamardDist_s.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamardDist_s.restype = c_uint
lib.ElHadamardDist_d.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamardDist_d.restype = c_uint
lib.ElHadamardDist_c.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamardDist_c.restype = c_uint
lib.ElHadamardDist_z.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElHadamardDist_z.restype = c_uint
def Hadamard(A,B,C):
  if type(A) is not type(B) or type(B) is not type(C):
    raise Exception('Matrix types must match')
  if A.tag != B.tag or B.tag != C.tag:
    raise Exception('Matrix datatypes must match')
  args = [A.obj,B.obj,C.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElHadamard_i(*args)
    elif A.tag == sTag: lib.ElHadamard_s(*args)
    elif A.tag == dTag: lib.ElHadamard_d(*args)
    elif A.tag == cTag: lib.ElHadamard_c(*args)
    elif A.tag == zTag: lib.ElHadamard_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElHadamardDist_i(*args)
    elif A.tag == sTag: lib.ElHadamardDist_s(*args)
    elif A.tag == dTag: lib.ElHadamardDist_d(*args)
    elif A.tag == cTag: lib.ElHadamardDist_c(*args)
    elif A.tag == zTag: lib.ElHadamardDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Hilbert-Schmidt
# ---------------
lib.ElHilbertSchmidt_i.argtypes = [c_void_p,c_void_p,POINTER(iType)]
lib.ElHilbertSchmidt_i.restype = c_uint
lib.ElHilbertSchmidt_s.argtypes = [c_void_p,c_void_p,POINTER(sType)]
lib.ElHilbertSchmidt_s.restype = c_uint
lib.ElHilbertSchmidt_d.argtypes = [c_void_p,c_void_p,POINTER(dType)]
lib.ElHilbertSchmidt_d.restype = c_uint
lib.ElHilbertSchmidt_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElHilbertSchmidt_c.restype = c_uint
lib.ElHilbertSchmidt_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElHilbertSchmidt_z.restype = c_uint
lib.ElHilbertSchmidtDist_i.argtypes = [c_void_p,c_void_p,POINTER(iType)]
lib.ElHilbertSchmidtDist_i.restype = c_uint
lib.ElHilbertSchmidtDist_s.argtypes = [c_void_p,c_void_p,POINTER(sType)]
lib.ElHilbertSchmidtDist_s.restype = c_uint
lib.ElHilbertSchmidtDist_d.argtypes = [c_void_p,c_void_p,POINTER(dType)]
lib.ElHilbertSchmidtDist_d.restype = c_uint
lib.ElHilbertSchmidtDist_c.argtypes = [c_void_p,c_void_p,POINTER(cType)]
lib.ElHilbertSchmidtDist_c.restype = c_uint
lib.ElHilbertSchmidtDist_z.argtypes = [c_void_p,c_void_p,POINTER(zType)]
lib.ElHilbertSchmidtDist_z.restype = c_uint
def HilbertSchmidt(A,B):
  if type(A) is type(B): raise Exception('Matrix types must match')
  if A.tag != B.tag: raise Exception('Datatypes must match')
  prod = TagToType(A.tag)()
  args = [A.obj,B.obj,pointer(prod)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElHilbertSchmidt_i(*args)
    elif A.tag == sTag: lib.ElHilbertSchmidt_s(*args)
    elif A.tag == dTag: lib.ElHilbertSchmidt_d(*args)
    elif A.tag == cTag: lib.ElHilbertSchmidt_c(*args)
    elif A.tag == zTag: lib.ElHilbertSchmidt_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElHilbertSchmidtDist_i(*args)
    elif A.tag == sTag: lib.ElHilbertSchmidtDist_s(*args)
    elif A.tag == dTag: lib.ElHilbertSchmidtDist_d(*args)
    elif A.tag == cTag: lib.ElHilbertSchmidtDist_c(*args)
    elif A.tag == zTag: lib.ElHilbertSchmidtDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return prod

# Index dependent fill
# --------------------
lib.ElIndexDependentFill_i.argtypes = [c_void_p,CFUNCTYPE(iType,iType,iType)]
lib.ElIndexDependentFill_i.restype = c_uint
lib.ElIndexDependentFill_s.argtypes = [c_void_p,CFUNCTYPE(sType,iType,iType)]
lib.ElIndexDependentFill_s.restype = c_uint
lib.ElIndexDependentFill_d.argtypes = [c_void_p,CFUNCTYPE(dType,iType,iType)]
lib.ElIndexDependentFill_d.restype = c_uint
lib.ElIndexDependentFill_c.argtypes = [c_void_p,CFUNCTYPE(cType,iType,iType)]
lib.ElIndexDependentFill_c.restype = c_uint
lib.ElIndexDependentFill_z.argtypes = [c_void_p,CFUNCTYPE(zType,iType,iType)]
lib.ElIndexDependentFill_z.restype = c_uint
lib.ElIndexDependentFillDist_i.argtypes = \
  [c_void_p,CFUNCTYPE(iType,iType,iType)]
lib.ElIndexDependentFillDist_i.restype = c_uint
lib.ElIndexDependentFillDist_s.argtypes = \
  [c_void_p,CFUNCTYPE(sType,iType,iType)]
lib.ElIndexDependentFillDist_s.restype = c_uint
lib.ElIndexDependentFillDist_d.argtypes = \
  [c_void_p,CFUNCTYPE(dType,iType,iType)]
lib.ElIndexDependentFillDist_d.restype = c_uint
lib.ElIndexDependentFillDist_c.argtypes = \
  [c_void_p,CFUNCTYPE(cType,iType,iType)]
lib.ElIndexDependentFillDist_c.restype = c_uint
lib.ElIndexDependentFillDist_z.argtypes = \
  [c_void_p,CFUNCTYPE(zType,iType,iType)]
lib.ElIndexDependentFillDist_z.restype = c_uint
def IndexDependentFill(A,fill):
  cFill = CFUNCTYPE(TagToType(A.tag),iType,iType)(fill)
  args = [A.obj,cFill]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElIndexDependentFill_i(*args)
    elif A.tag == sTag: lib.ElIndexDependentFill_s(*args)
    elif A.tag == dTag: lib.ElIndexDependentFill_d(*args)
    elif A.tag == cTag: lib.ElIndexDependentFill_c(*args)
    elif A.tag == zTag: lib.ElIndexDependentFill_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElIndexDependentFillDist_i(*args)
    elif A.tag == sTag: lib.ElIndexDependentFillDist_s(*args)
    elif A.tag == dTag: lib.ElIndexDependentFillDist_d(*args)
    elif A.tag == cTag: lib.ElIndexDependentFillDist_c(*args)
    elif A.tag == zTag: lib.ElIndexDependentFillDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Index dependent map
# -------------------
lib.ElIndexDependentMap_i.argtypes = \
  [c_void_p,CFUNCTYPE(iType,iType,iType,iType)]
lib.ElIndexDependentMap_i.restype = c_uint
lib.ElIndexDependentMap_s.argtypes = \
  [c_void_p,CFUNCTYPE(sType,iType,iType,sType)]
lib.ElIndexDependentMap_s.restype = c_uint
lib.ElIndexDependentMap_d.argtypes = \
  [c_void_p,CFUNCTYPE(dType,iType,iType,dType)]
lib.ElIndexDependentMap_d.restype = c_uint
lib.ElIndexDependentMap_c.argtypes = \
  [c_void_p,CFUNCTYPE(cType,iType,iType,cType)]
lib.ElIndexDependentMap_c.restype = c_uint
lib.ElIndexDependentMap_z.argtypes = \
  [c_void_p,CFUNCTYPE(zType,iType,iType,zType)]
lib.ElIndexDependentMap_z.restype = c_uint
lib.ElIndexDependentMapDist_i.argtypes = \
  [c_void_p,CFUNCTYPE(iType,iType,iType,iType)]
lib.ElIndexDependentMapDist_i.restype = c_uint
lib.ElIndexDependentMapDist_s.argtypes = \
  [c_void_p,CFUNCTYPE(sType,iType,iType,sType)]
lib.ElIndexDependentMapDist_s.restype = c_uint
lib.ElIndexDependentMapDist_d.argtypes = \
  [c_void_p,CFUNCTYPE(dType,iType,iType,dType)]
lib.ElIndexDependentMapDist_d.restype = c_uint
lib.ElIndexDependentMapDist_c.argtypes = \
  [c_void_p,CFUNCTYPE(cType,iType,iType,cType)]
lib.ElIndexDependentMapDist_c.restype = c_uint
lib.ElIndexDependentMapDist_z.argtypes = \
  [c_void_p,CFUNCTYPE(zType,iType,iType,zType)]
lib.ElIndexDependentMapDist_z.restype = c_uint
def IndexDependentMap(A,mapFunc):
  typeA = TagToType(A)
  cMap = CFUNCTYPE(typeA,iType,iType,typeA)(mapFunc)
  args = [A.obj,cMap]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElIndexDependentMap_i(*args)
    elif A.tag == sTag: lib.ElIndexDependentMap_s(*args)
    elif A.tag == dTag: lib.ElIndexDependentMap_d(*args)
    elif A.tag == cTag: lib.ElIndexDependentMap_c(*args)
    elif A.tag == zTag: lib.ElIndexDependentMap_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElIndexDependentMapDist_i(*args)
    elif A.tag == sTag: lib.ElIndexDependentMapDist_s(*args)
    elif A.tag == dTag: lib.ElIndexDependentMapDist_d(*args)
    elif A.tag == cTag: lib.ElIndexDependentMapDist_c(*args)
    elif A.tag == zTag: lib.ElIndexDependentMapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Make symmetric/Hermitian
# ------------------------
lib.ElMakeSymmetric_i.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetric_i.restype = c_uint
lib.ElMakeSymmetric_s.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetric_s.restype = c_uint
lib.ElMakeSymmetric_d.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetric_d.restype = c_uint
lib.ElMakeSymmetric_c.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetric_c.restype = c_uint
lib.ElMakeSymmetric_z.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetric_z.restype = c_uint
lib.ElMakeSymmetricDist_i.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetricDist_i.restype = c_uint
lib.ElMakeSymmetricDist_s.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetricDist_s.restype = c_uint
lib.ElMakeSymmetricDist_d.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetricDist_d.restype = c_uint
lib.ElMakeSymmetricDist_c.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetricDist_c.restype = c_uint
lib.ElMakeSymmetricDist_z.argtypes = [c_uint,c_void_p]
lib.ElMakeSymmetricDist_z.restype = c_uint

lib.ElMakeHermitian_c.argtypes = [c_uint,c_void_p]
lib.ElMakeHermitian_c.restype = c_uint
lib.ElMakeHermitian_z.argtypes = [c_uint,c_void_p]
lib.ElMakeHermitian_z.restype = c_uint
lib.ElMakeHermitianDist_c.argtypes = [c_uint,c_void_p]
lib.ElMakeHermitianDist_c.restype = c_uint
lib.ElMakeHermitianDist_z.argtypes = [c_uint,c_void_p]
lib.ElMakeHermitianDist_z.restype = c_uint

def MakeSymmetric(uplo,A,conj=False):
  args = [uplo,A.obj]
  if type(A) is Matrix: 
    if   A.tag == iTag: lib.ElMakeSymmetric_i(*args)
    elif A.tag == sTag: lib.ElMakeSymmetric_s(*args)
    elif A.tag == dTag: lib.ElMakeSymmetric_d(*args)
    elif A.tag == cTag: 
      if conj: lib.ElMakeHermitian_c(*args)
      else:    lib.ElMakeSymmetric_c(*args)
    elif A.tag == zTag: 
      if conj: lib.ElMakeHermitian_z(*args)
      else:    lib.ElMakeSymmetric_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMakeSymmetricDist_i(*args)
    elif A.tag == sTag: lib.ElMakeSymmetricDist_s(*args)
    elif A.tag == dTag: lib.ElMakeSymmetricDist_d(*args)
    elif A.tag == cTag: 
      if conj: lib.ElMakeHermitianDist_c(*args)
      else:    lib.ElMakeSymmetricDist_c(*args)
    elif A.tag == zTag: 
      if conj: lib.ElMakeHermitianDist_z(*args)
      else:    lib.ElMakeSymmetricDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

def MakeHermitian(uplo,A):
  MakeSymmetric(uplo,A,True)

# Make real
# ---------
lib.ElMakeReal_c.argtypes = [c_uint,c_void_p]
lib.ElMakeReal_c.restype = c_uint
lib.ElMakeReal_z.argtypes = [c_uint,c_void_p]
lib.ElMakeReal_z.restype = c_uint
lib.ElMakeRealDist_c.argtypes = [c_uint,c_void_p]
lib.ElMakeRealDist_c.restype = c_uint
lib.ElMakeRealDist_z.argtypes = [c_uint,c_void_p]
lib.ElMakeRealDist_z.restype = c_uint
def MakeReal(uplo,A):
  args = [uplo,A.obj]
  if type(A) is Matrix:
    if   A.tag == cTag: lib.ElMakeReal_c(*args)
    elif A.tag == zTag: lib.ElMakeReal_z(*args)
  elif type(A) is DistMatrix:
    if   A.tag == cTag: lib.ElMakeRealDist_c(*args)
    elif A.tag == zTag: lib.ElMakeRealDist_z(*args)
  else: TypeExcept()

# Make trapezoidal
# ----------------
lib.ElMakeTrapezoidal_i.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidal_i.restype = c_uint
lib.ElMakeTrapezoidal_s.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidal_s.restype = c_uint
lib.ElMakeTrapezoidal_d.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidal_d.restype = c_uint
lib.ElMakeTrapezoidal_c.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidal_c.restype = c_uint
lib.ElMakeTrapezoidal_z.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidal_z.restype = c_uint
lib.ElMakeTrapezoidalDist_i.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidalDist_i.restype = c_uint
lib.ElMakeTrapezoidalDist_s.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidalDist_s.restype = c_uint
lib.ElMakeTrapezoidalDist_d.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidalDist_d.restype = c_uint
lib.ElMakeTrapezoidalDist_c.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidalDist_c.restype = c_uint
lib.ElMakeTrapezoidalDist_z.argtypes = [c_uint,c_void_p,iType]
lib.ElMakeTrapezoidalDist_z.restype = c_uint
def MakeTrapezoidal(uplo,A,offset=0):
  args = [uplo,A.obj,offset]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMakeTrapezoidal_i(*args)
    elif A.tag == sTag: lib.ElMakeTrapezoidal_s(*args)
    elif A.tag == dTag: lib.ElMakeTrapezoidal_d(*args)
    elif A.tag == cTag: lib.ElMakeTrapezoidal_c(*args)
    elif A.tag == zTag: lib.ElMakeTrapezoidal_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMakeTrapezoidalDist_i(*args)
    elif A.tag == sTag: lib.ElMakeTrapezoidalDist_s(*args)
    elif A.tag == dTag: lib.ElMakeTrapezoidalDist_d(*args)
    elif A.tag == cTag: lib.ElMakeTrapezoidalDist_c(*args)
    elif A.tag == zTag: lib.ElMakeTrapezoidalDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Make triangular
# ---------------
lib.ElMakeTriangular_i.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangular_i.restype = c_uint
lib.ElMakeTriangular_s.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangular_s.restype = c_uint
lib.ElMakeTriangular_d.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangular_d.restype = c_uint
lib.ElMakeTriangular_c.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangular_c.restype = c_uint
lib.ElMakeTriangular_z.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangular_z.restype = c_uint
lib.ElMakeTriangularDist_i.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangularDist_i.restype = c_uint
lib.ElMakeTriangularDist_s.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangularDist_s.restype = c_uint
lib.ElMakeTriangularDist_d.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangularDist_d.restype = c_uint
lib.ElMakeTriangularDist_c.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangularDist_c.restype = c_uint
lib.ElMakeTriangularDist_z.argtypes = [c_uint,c_void_p]
lib.ElMakeTriangularDist_z.restype = c_uint
def MakeTriangular(uplo,A):
  args = [uplo,A.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMakeTriangular_i(*args)
    elif A.tag == sTag: lib.ElMakeTriangular_s(*args)
    elif A.tag == dTag: lib.ElMakeTriangular_d(*args)
    elif A.tag == cTag: lib.ElMakeTriangular_c(*args)
    elif A.tag == zTag: lib.ElMakeTriangular_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMakeTriangularDist_i(*args)
    elif A.tag == sTag: lib.ElMakeTriangularDist_s(*args)
    elif A.tag == dTag: lib.ElMakeTriangularDist_d(*args)
    elif A.tag == cTag: lib.ElMakeTriangularDist_c(*args)
    elif A.tag == zTag: lib.ElMakeTriangularDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Max
# ---
class ValueInt_i(ctypes.Structure):
  _fields_ = [("value",iType),("index",iType)]
class ValueInt_s(ctypes.Structure):
  _fields_ = [("value",sType),("index",iType)]
class ValueInt_d(ctypes.Structure):
  _fields_ = [("value",dType),("index",iType)]
class ValueInt_c(ctypes.Structure):
  _fields_ = [("value",cType),("index",iType)]
class ValueInt_z(ctypes.Structure):
  _fields_ = [("value",zType),("index",iType)]
def TagToValueInt(tag):
  if   tag == iTag: return ValueInt_i()
  elif tag == sTag: return ValueInt_s()
  elif tag == dTag: return ValueInt_d()
  elif tag == cTag: return ValueInt_c()
  elif tag == zTag: return ValueInt_z()
  else: DataExcept()

class ValueIntPair_i(ctypes.Structure):
  _fields_ = [("value",iType),("indices",(iType*2))]
class ValueIntPair_s(ctypes.Structure):
  _fields_ = [("value",sType),("indices",(iType*2))]
class ValueIntPair_d(ctypes.Structure):
  _fields_ = [("value",dType),("indices",(iType*2))]
class ValueIntPair_c(ctypes.Structure):
  _fields_ = [("value",cType),("indices",(iType*2))]
class ValueIntPair_z(ctypes.Structure):
  _fields_ = [("value",zType),("indices",(iType*2))]
def TagToValueIntPair(tag):
  if   tag == iTag: return ValueIntPair_i()
  elif tag == sTag: return ValueIntPair_s()
  elif tag == dTag: return ValueIntPair_d()
  elif tag == cTag: return ValueIntPair_c()
  elif tag == zTag: return ValueIntPair_z()
  else: DataExcept()

lib.ElMax_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMax_i.restype = c_uint
lib.ElMax_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMax_s.restype = c_uint
lib.ElMax_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMax_d.restype = c_uint
lib.ElMaxDist_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMaxDist_i.restype = c_uint
lib.ElMaxDist_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMaxDist_s.restype = c_uint
lib.ElMaxDist_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMaxDist_d.restype = c_uint
def Max(A):
  pair = TagToValueIntPair(A.tag)
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMax_i(*args) 
    elif A.tag == sTag: lib.ElMax_s(*args) 
    elif A.tag == dTag: lib.ElMax_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMaxDist_i(*args) 
    elif A.tag == sTag: lib.ElMaxDist_s(*args) 
    elif A.tag == dTag: lib.ElMaxDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElSymmetricMax_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMax_i.restype = c_uint
lib.ElSymmetricMax_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMax_s.restype = c_uint
lib.ElSymmetricMax_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMax_d.restype = c_uint
lib.ElSymmetricMaxDist_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMaxDist_i.restype = c_uint
lib.ElSymmetricMaxDist_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMaxDist_s.restype = c_uint
lib.ElSymmetricMaxDist_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMaxDist_d.restype = c_uint
def SymmetricMax(uplo,A):
  pair = TagToValueIntPair(A.tag)
  args = [uplo,A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSymmetricMax_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMax_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMax_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSymmetricMaxDist_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMaxDist_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMaxDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElVectorMax_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMax_i.restype = c_uint
lib.ElVectorMax_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMax_s.restype = c_uint
lib.ElVectorMax_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMax_d.restype = c_uint
lib.ElVectorMaxDist_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMaxDist_i.restype = c_uint
lib.ElVectorMaxDist_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMaxDist_s.restype = c_uint
lib.ElVectorMaxDist_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMaxDist_d.restype = c_uint
def VectorMax(A):
  pair = TagToValueInt(A.tag)
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElVectorMax_i(*args) 
    elif A.tag == sTag: lib.ElVectorMax_s(*args) 
    elif A.tag == dTag: lib.ElVectorMax_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElVectorMaxDist_i(*args) 
    elif A.tag == sTag: lib.ElVectorMaxDist_s(*args) 
    elif A.tag == dTag: lib.ElVectorMaxDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.index

# MaxAbs
# ------
lib.ElMaxAbs_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMaxAbs_i.restype = c_uint
lib.ElMaxAbs_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMaxAbs_s.restype = c_uint
lib.ElMaxAbs_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMaxAbs_d.restype = c_uint
lib.ElMaxAbs_c.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMaxAbs_c.restype = c_uint
lib.ElMaxAbs_z.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMaxAbs_z.restype = c_uint
lib.ElMaxAbsDist_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMaxAbsDist_i.restype = c_uint
lib.ElMaxAbsDist_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMaxAbsDist_s.restype = c_uint
lib.ElMaxAbsDist_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMaxAbsDist_d.restype = c_uint
lib.ElMaxAbsDist_c.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMaxAbsDist_c.restype = c_uint
lib.ElMaxAbsDist_z.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMaxAbsDist_z.restype = c_uint
def MaxAbs(A):
  pair = TagToValueIntPair(Base(A.tag))
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMaxAbs_i(*args) 
    elif A.tag == sTag: lib.ElMaxAbs_s(*args) 
    elif A.tag == dTag: lib.ElMaxAbs_d(*args) 
    elif A.tag == cTag: lib.ElMaxAbs_c(*args) 
    elif A.tag == zTag: lib.ElMaxAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMaxAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElMaxAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElMaxAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElMaxAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElMaxAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElSymmetricMaxAbs_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMaxAbs_i.restype = c_uint
lib.ElSymmetricMaxAbs_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMaxAbs_s.restype = c_uint
lib.ElSymmetricMaxAbs_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMaxAbs_d.restype = c_uint
lib.ElSymmetricMaxAbs_c.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMaxAbs_c.restype = c_uint
lib.ElSymmetricMaxAbs_z.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMaxAbs_z.restype = c_uint
lib.ElSymmetricMaxAbsDist_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMaxAbsDist_i.restype = c_uint
lib.ElSymmetricMaxAbsDist_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMaxAbsDist_s.restype = c_uint
lib.ElSymmetricMaxAbsDist_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMaxAbsDist_d.restype = c_uint
lib.ElSymmetricMaxAbsDist_c.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMaxAbsDist_c.restype = c_uint
lib.ElSymmetricMaxAbsDist_z.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMaxAbsDist_z.restype = c_uint
def SymmetricMaxAbs(uplo,A):
  pair = TagToValueIntPair(Base(A.tag))
  args = [uplo,A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSymmetricMaxAbs_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMaxAbs_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMaxAbs_d(*args) 
    elif A.tag == cTag: lib.ElSymmetricMaxAbs_c(*args) 
    elif A.tag == zTag: lib.ElSymmetricMaxAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSymmetricMaxAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMaxAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMaxAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElSymmetricMaxAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElSymmetricMaxAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElVectorMaxAbs_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMaxAbs_i.restype = c_uint
lib.ElVectorMaxAbs_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMaxAbs_s.restype = c_uint
lib.ElVectorMaxAbs_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMaxAbs_d.restype = c_uint
lib.ElVectorMaxAbs_c.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMaxAbs_c.restype = c_uint
lib.ElVectorMaxAbs_z.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMaxAbs_z.restype = c_uint
lib.ElVectorMaxAbsDist_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMaxAbsDist_i.restype = c_uint
lib.ElVectorMaxAbsDist_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMaxAbsDist_s.restype = c_uint
lib.ElVectorMaxAbsDist_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMaxAbsDist_d.restype = c_uint
lib.ElVectorMaxAbsDist_c.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMaxAbsDist_c.restype = c_uint
lib.ElVectorMaxAbsDist_z.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMaxAbsDist_z.restype = c_uint
def VectorMaxAbs(A):
  pair = TagToValueInt(Base(A.tag))
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElVectorMaxAbs_i(*args) 
    elif A.tag == sTag: lib.ElVectorMaxAbs_s(*args) 
    elif A.tag == dTag: lib.ElVectorMaxAbs_d(*args) 
    elif A.tag == cTag: lib.ElVectorMaxAbs_c(*args) 
    elif A.tag == zTag: lib.ElVectorMaxAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElVectorMaxAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElVectorMaxAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElVectorMaxAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElVectorMaxAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElVectorMaxAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.index

# Min
# ---
lib.ElMin_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMin_i.restype = c_uint
lib.ElMin_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMin_s.restype = c_uint
lib.ElMin_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMin_d.restype = c_uint
lib.ElMinDist_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMinDist_i.restype = c_uint
lib.ElMinDist_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMinDist_s.restype = c_uint
lib.ElMinDist_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMinDist_d.restype = c_uint
def Min(A):
  pair = TagToValueIntPair(A.tag)
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMin_i(*args) 
    elif A.tag == sTag: lib.ElMin_s(*args) 
    elif A.tag == dTag: lib.ElMin_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMinDist_i(*args) 
    elif A.tag == sTag: lib.ElMinDist_s(*args) 
    elif A.tag == dTag: lib.ElMinDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElSymmetricMin_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMin_i.restype = c_uint
lib.ElSymmetricMin_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMin_s.restype = c_uint
lib.ElSymmetricMin_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMin_d.restype = c_uint
lib.ElSymmetricMinDist_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMinDist_i.restype = c_uint
lib.ElSymmetricMinDist_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMinDist_s.restype = c_uint
lib.ElSymmetricMinDist_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMinDist_d.restype = c_uint
def SymmetricMin(uplo,A):
  pair = TagToValueIntPair(A.tag)
  args = [uplo,A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSymmetricMin_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMin_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMin_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSymmetricMinDist_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMinDist_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMinDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElVectorMin_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMin_i.restype = c_uint
lib.ElVectorMin_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMin_s.restype = c_uint
lib.ElVectorMin_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMin_d.restype = c_uint
lib.ElVectorMinDist_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMinDist_i.restype = c_uint
lib.ElVectorMinDist_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMinDist_s.restype = c_uint
lib.ElVectorMinDist_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMinDist_d.restype = c_uint
def VectorMin(A):
  pair = TagToValueInt(A.tag)
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElVectorMin_i(*args) 
    elif A.tag == sTag: lib.ElVectorMin_s(*args) 
    elif A.tag == dTag: lib.ElVectorMin_d(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElVectorMinDist_i(*args) 
    elif A.tag == sTag: lib.ElVectorMinDist_s(*args) 
    elif A.tag == dTag: lib.ElVectorMinDist_d(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.index

# MinAbs
# ------
lib.ElMinAbs_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMinAbs_i.restype = c_uint
lib.ElMinAbs_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMinAbs_s.restype = c_uint
lib.ElMinAbs_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMinAbs_d.restype = c_uint
lib.ElMinAbs_c.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMinAbs_c.restype = c_uint
lib.ElMinAbs_z.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMinAbs_z.restype = c_uint
lib.ElMinAbsDist_i.argtypes = [c_void_p,POINTER(ValueIntPair_i)]
lib.ElMinAbsDist_i.restype = c_uint
lib.ElMinAbsDist_s.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMinAbsDist_s.restype = c_uint
lib.ElMinAbsDist_d.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMinAbsDist_d.restype = c_uint
lib.ElMinAbsDist_c.argtypes = [c_void_p,POINTER(ValueIntPair_s)]
lib.ElMinAbsDist_c.restype = c_uint
lib.ElMinAbsDist_z.argtypes = [c_void_p,POINTER(ValueIntPair_d)]
lib.ElMinAbsDist_z.restype = c_uint
def MinAbs(A):
  pair = TagToValueIntPair(Base(A.tag))
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElMinAbs_i(*args) 
    elif A.tag == sTag: lib.ElMinAbs_s(*args) 
    elif A.tag == dTag: lib.ElMinAbs_d(*args) 
    elif A.tag == cTag: lib.ElMinAbs_c(*args) 
    elif A.tag == zTag: lib.ElMinAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElMinAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElMinAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElMinAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElMinAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElMinAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElSymmetricMinAbs_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMinAbs_i.restype = c_uint
lib.ElSymmetricMinAbs_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMinAbs_s.restype = c_uint
lib.ElSymmetricMinAbs_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMinAbs_d.restype = c_uint
lib.ElSymmetricMinAbs_c.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMinAbs_c.restype = c_uint
lib.ElSymmetricMinAbs_z.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMinAbs_z.restype = c_uint
lib.ElSymmetricMinAbsDist_i.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_i)]
lib.ElSymmetricMinAbsDist_i.restype = c_uint
lib.ElSymmetricMinAbsDist_s.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMinAbsDist_s.restype = c_uint
lib.ElSymmetricMinAbsDist_d.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMinAbsDist_d.restype = c_uint
lib.ElSymmetricMinAbsDist_c.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_s)]
lib.ElSymmetricMinAbsDist_c.restype = c_uint
lib.ElSymmetricMinAbsDist_z.argtypes = [c_uint,c_void_p,POINTER(ValueIntPair_d)]
lib.ElSymmetricMinAbsDist_z.restype = c_uint
def SymmetricMinAbs(uplo,A):
  pair = TagToValueIntPair(Base(A.tag))
  args = [uplo,A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSymmetricMinAbs_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMinAbs_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMinAbs_d(*args) 
    elif A.tag == cTag: lib.ElSymmetricMinAbs_c(*args) 
    elif A.tag == zTag: lib.ElSymmetricMinAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSymmetricMinAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElSymmetricMinAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElSymmetricMinAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElSymmetricMinAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElSymmetricMinAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.indices[0], pair.indices[1]

lib.ElVectorMinAbs_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMinAbs_i.restype = c_uint
lib.ElVectorMinAbs_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMinAbs_s.restype = c_uint
lib.ElVectorMinAbs_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMinAbs_d.restype = c_uint
lib.ElVectorMinAbs_c.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMinAbs_c.restype = c_uint
lib.ElVectorMinAbs_z.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMinAbs_z.restype = c_uint
lib.ElVectorMinAbsDist_i.argtypes = [c_void_p,POINTER(ValueInt_i)]
lib.ElVectorMinAbsDist_i.restype = c_uint
lib.ElVectorMinAbsDist_s.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMinAbsDist_s.restype = c_uint
lib.ElVectorMinAbsDist_d.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMinAbsDist_d.restype = c_uint
lib.ElVectorMinAbsDist_c.argtypes = [c_void_p,POINTER(ValueInt_s)]
lib.ElVectorMinAbsDist_c.restype = c_uint
lib.ElVectorMinAbsDist_z.argtypes = [c_void_p,POINTER(ValueInt_d)]
lib.ElVectorMinAbsDist_z.restype = c_uint
def VectorMinAbs(A):
  pair = TagToValueInt(Base(A.tag))
  args = [A.obj,pointer(pair)]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElVectorMinAbs_i(*args) 
    elif A.tag == sTag: lib.ElVectorMinAbs_s(*args) 
    elif A.tag == dTag: lib.ElVectorMinAbs_d(*args) 
    elif A.tag == cTag: lib.ElVectorMinAbs_c(*args) 
    elif A.tag == zTag: lib.ElVectorMinAbs_z(*args) 
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElVectorMinAbsDist_i(*args) 
    elif A.tag == sTag: lib.ElVectorMinAbsDist_s(*args) 
    elif A.tag == dTag: lib.ElVectorMinAbsDist_d(*args) 
    elif A.tag == cTag: lib.ElVectorMinAbsDist_c(*args) 
    elif A.tag == zTag: lib.ElVectorMinAbsDist_z(*args) 
    else: DataExcept()
  else: TypeExcept()
  return pair.value, pair.index

# Nrm2
# ----
lib.ElNrm2_s.argtypes = [c_void_p,POINTER(sType)]
lib.ElNrm2_s.restype = c_uint
lib.ElNrm2_d.argtypes = [c_void_p,POINTER(dType)]
lib.ElNrm2_d.restype = c_uint
lib.ElNrm2_c.argtypes = [c_void_p,POINTER(sType)]
lib.ElNrm2_c.restype = c_uint
lib.ElNrm2_z.argtypes = [c_void_p,POINTER(dType)]
lib.ElNrm2_z.restype = c_uint
lib.ElNrm2Dist_s.argtypes = [c_void_p,POINTER(sType)]
lib.ElNrm2Dist_s.restype = c_uint
lib.ElNrm2Dist_d.argtypes = [c_void_p,POINTER(dType)]
lib.ElNrm2Dist_d.restype = c_uint
lib.ElNrm2Dist_c.argtypes = [c_void_p,POINTER(sType)]
lib.ElNrm2Dist_c.restype = c_uint
lib.ElNrm2Dist_z.argtypes = [c_void_p,POINTER(dType)]
lib.ElNrm2Dist_z.restype = c_uint
def Nrm2(A):
  gamma = TagToType(Base(A.tag))()
  args = [A.obj,pointer(gamma)]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElNrm2_s(*args)
    elif A.tag == dTag: lib.ElNrm2_d(*args)
    elif A.tag == cTag: lib.ElNrm2_c(*args)
    elif A.tag == zTag: lib.ElNrm2_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElNrm2Dist_s(*args)
    elif A.tag == dTag: lib.ElNrm2Dist_d(*args)
    elif A.tag == cTag: lib.ElNrm2Dist_c(*args)
    elif A.tag == zTag: lib.ElNrm2Dist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Scale
# -----
lib.ElScale_i.argtypes = [iType,c_void_p]
lib.ElScale_i.restype = c_uint
lib.ElScale_s.argtypes = [sType,c_void_p]
lib.ElScale_s.restype = c_uint
lib.ElScale_d.argtypes = [dType,c_void_p]
lib.ElScale_d.restype = c_uint
lib.ElScale_c.argtypes = [cType,c_void_p]
lib.ElScale_c.restype = c_uint
lib.ElScale_z.argtypes = [zType,c_void_p]
lib.ElScale_z.restype = c_uint
lib.ElScaleDist_i.argtypes = [iType,c_void_p]
lib.ElScaleDist_i.restype = c_uint
lib.ElScaleDist_s.argtypes = [sType,c_void_p]
lib.ElScaleDist_s.restype = c_uint
lib.ElScaleDist_d.argtypes = [dType,c_void_p]
lib.ElScaleDist_d.restype = c_uint
lib.ElScaleDist_c.argtypes = [cType,c_void_p]
lib.ElScaleDist_c.restype = c_uint
lib.ElScaleDist_z.argtypes = [zType,c_void_p]
lib.ElScaleDist_z.restype = c_uint
def Scale(alphaPre,A):
  alpha = TagToType(A.tag)(alphaPre)
  args = [alpha,A.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElScale_i(*args)
    elif A.tag == sTag: lib.ElScale_s(*args)
    elif A.tag == dTag: lib.ElScale_d(*args)
    elif A.tag == cTag: lib.ElScale_c(*args)
    elif A.tag == zTag: lib.ElScale_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElScaleDist_i(*args)
    elif A.tag == sTag: lib.ElScaleDist_s(*args)
    elif A.tag == dTag: lib.ElScaleDist_d(*args)
    elif A.tag == cTag: lib.ElScaleDist_c(*args)
    elif A.tag == zTag: lib.ElScaleDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Scale trapezoid
# ---------------
lib.ElScaleTrapezoid_i.argtypes = [iType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoid_i.restype = c_uint
lib.ElScaleTrapezoid_s.argtypes = [sType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoid_s.restype = c_uint
lib.ElScaleTrapezoid_d.argtypes = [dType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoid_d.restype = c_uint
lib.ElScaleTrapezoid_c.argtypes = [cType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoid_c.restype = c_uint
lib.ElScaleTrapezoid_z.argtypes = [zType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoid_z.restype = c_uint
lib.ElScaleTrapezoidDist_i.argtypes = [iType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoidDist_i.restype = c_uint
lib.ElScaleTrapezoidDist_s.argtypes = [sType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoidDist_s.restype = c_uint
lib.ElScaleTrapezoidDist_d.argtypes = [dType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoidDist_d.restype = c_uint
lib.ElScaleTrapezoidDist_c.argtypes = [cType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoidDist_c.restype = c_uint
lib.ElScaleTrapezoidDist_z.argtypes = [zType,c_uint,c_void_p,iType]
lib.ElScaleTrapezoidDist_z.restype = c_uint
def ScaleTrapezoid(alphaPre,uplo,A,offset=0):
  alpha = TagToType(A.tag)(alphaPre)
  args = [alpha,uplo,A.obj,offset]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElScaleTrapezoid_i(*args)
    elif A.tag == sTag: lib.ElScaleTrapezoid_s(*args)
    elif A.tag == dTag: lib.ElScaleTrapezoid_d(*args)
    elif A.tag == cTag: lib.ElScaleTrapezoid_c(*args)
    elif A.tag == zTag: lib.ElScaleTrapezoid_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElScaleTrapezoidDist_i(*args)
    elif A.tag == sTag: lib.ElScaleTrapezoidDist_s(*args)
    elif A.tag == dTag: lib.ElScaleTrapezoidDist_d(*args)
    elif A.tag == cTag: lib.ElScaleTrapezoidDist_c(*args)
    elif A.tag == zTag: lib.ElScaleTrapezoidDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Set diagonal
# ------------
lib.ElSetDiagonal_i.argtypes = [c_void_p,iType,iType]
lib.ElSetDiagonal_i.restype = c_uint
lib.ElSetDiagonal_s.argtypes = [c_void_p,sType,iType]
lib.ElSetDiagonal_s.restype = c_uint
lib.ElSetDiagonal_d.argtypes = [c_void_p,dType,iType]
lib.ElSetDiagonal_d.restype = c_uint
lib.ElSetDiagonal_c.argtypes = [c_void_p,cType,iType]
lib.ElSetDiagonal_c.restype = c_uint
lib.ElSetDiagonal_z.argtypes = [c_void_p,zType,iType]
lib.ElSetDiagonal_z.restype = c_uint
lib.ElSetDiagonalDist_i.argtypes = [c_void_p,iType,iType]
lib.ElSetDiagonalDist_i.restype = c_uint
lib.ElSetDiagonalDist_s.argtypes = [c_void_p,sType,iType]
lib.ElSetDiagonalDist_s.restype = c_uint
lib.ElSetDiagonalDist_d.argtypes = [c_void_p,dType,iType]
lib.ElSetDiagonalDist_d.restype = c_uint
lib.ElSetDiagonalDist_c.argtypes = [c_void_p,cType,iType]
lib.ElSetDiagonalDist_c.restype = c_uint
lib.ElSetDiagonalDist_z.argtypes = [c_void_p,zType,iType]
lib.ElSetDiagonalDist_z.restype = c_uint
def SetDiagonal(A,alphaPre,offset=0):
  alpha = TagToType(A.tag)(alphaPre)
  args = [A.obj,alpha,offset]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSetDiagonal_i(*args)
    elif A.tag == sTag: lib.ElSetDiagonal_s(*args)
    elif A.tag == dTag: lib.ElSetDiagonal_d(*args)
    elif A.tag == cTag: lib.ElSetDiagonal_c(*args)
    elif A.tag == zTag: lib.ElSetDiagonal_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSetDiagonalDist_i(*args)
    elif A.tag == sTag: lib.ElSetDiagonalDist_s(*args)
    elif A.tag == dTag: lib.ElSetDiagonalDist_d(*args)
    elif A.tag == cTag: lib.ElSetDiagonalDist_c(*args)
    elif A.tag == zTag: lib.ElSetDiagonalDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Swap
# ----
lib.ElSwap_i.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwap_i.restype = c_uint
lib.ElSwap_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwap_s.restype = c_uint
lib.ElSwap_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwap_d.restype = c_uint
lib.ElSwap_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwap_c.restype = c_uint
lib.ElSwap_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwap_z.restype = c_uint
lib.ElSwapDist_i.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwapDist_i.restype = c_uint
lib.ElSwapDist_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwapDist_s.restype = c_uint
lib.ElSwapDist_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwapDist_d.restype = c_uint
lib.ElSwapDist_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwapDist_c.restype = c_uint
lib.ElSwapDist_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElSwapDist_z.restype = c_uint
def Swap(orient,X,Y):
  if type(X) is not type(Y): raise Exception('Matrix types must match')
  if X.tag != Y.tag: raise Exception('Matrix datatypes must match')
  args = [orient,X.obj,Y.obj]
  if type(X) is Matrix:
    if   A.tag == iTag: lib.ElSwap_i(*args)
    elif A.tag == sTag: lib.ElSwap_s(*args)
    elif A.tag == dTag: lib.ElSwap_d(*args)
    elif A.tag == cTag: lib.ElSwap_c(*args)
    elif A.tag == zTag: lib.ElSwap_z(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   A.tag == iTag: lib.ElSwapDist_i(*args)
    elif A.tag == sTag: lib.ElSwapDist_s(*args)
    elif A.tag == dTag: lib.ElSwapDist_d(*args)
    elif A.tag == cTag: lib.ElSwapDist_c(*args)
    elif A.tag == zTag: lib.ElSwapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

lib.ElRowSwap_i.argtypes = [c_void_p,iType,iType]
lib.ElRowSwap_i.restype = c_uint
lib.ElRowSwap_s.argtypes = [c_void_p,iType,iType]
lib.ElRowSwap_s.restype = c_uint
lib.ElRowSwap_d.argtypes = [c_void_p,iType,iType]
lib.ElRowSwap_d.restype = c_uint
lib.ElRowSwap_c.argtypes = [c_void_p,iType,iType]
lib.ElRowSwap_c.restype = c_uint
lib.ElRowSwap_z.argtypes = [c_void_p,iType,iType]
lib.ElRowSwap_z.restype = c_uint
lib.ElRowSwapDist_i.argtypes = [c_void_p,iType,iType]
lib.ElRowSwapDist_i.restype = c_uint
lib.ElRowSwapDist_s.argtypes = [c_void_p,iType,iType]
lib.ElRowSwapDist_s.restype = c_uint
lib.ElRowSwapDist_d.argtypes = [c_void_p,iType,iType]
lib.ElRowSwapDist_d.restype = c_uint
lib.ElRowSwapDist_c.argtypes = [c_void_p,iType,iType]
lib.ElRowSwapDist_c.restype = c_uint
lib.ElRowSwapDist_z.argtypes = [c_void_p,iType,iType]
lib.ElRowSwapDist_z.restype = c_uint
def RowSwap(A,iTo,iFrom):
  args = [A.obj,iTo,iFrom]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElRowSwap_i(*args)
    elif A.tag == sTag: lib.ElRowSwap_s(*args)
    elif A.tag == dTag: lib.ElRowSwap_d(*args)
    elif A.tag == cTag: lib.ElRowSwap_c(*args)
    elif A.tag == zTag: lib.ElRowSwap_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElRowSwapDist_i(*args)
    elif A.tag == sTag: lib.ElRowSwapDist_s(*args)
    elif A.tag == dTag: lib.ElRowSwapDist_d(*args)
    elif A.tag == cTag: lib.ElRowSwapDist_c(*args)
    elif A.tag == zTag: lib.ElRowSwapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

lib.ElColSwap_i.argtypes = [c_void_p,iType,iType]
lib.ElColSwap_i.restype = c_uint
lib.ElColSwap_s.argtypes = [c_void_p,iType,iType]
lib.ElColSwap_s.restype = c_uint
lib.ElColSwap_d.argtypes = [c_void_p,iType,iType]
lib.ElColSwap_d.restype = c_uint
lib.ElColSwap_c.argtypes = [c_void_p,iType,iType]
lib.ElColSwap_c.restype = c_uint
lib.ElColSwap_z.argtypes = [c_void_p,iType,iType]
lib.ElColSwap_z.restype = c_uint
lib.ElColSwapDist_i.argtypes = [c_void_p,iType,iType]
lib.ElColSwapDist_i.restype = c_uint
lib.ElColSwapDist_s.argtypes = [c_void_p,iType,iType]
lib.ElColSwapDist_s.restype = c_uint
lib.ElColSwapDist_d.argtypes = [c_void_p,iType,iType]
lib.ElColSwapDist_d.restype = c_uint
lib.ElColSwapDist_c.argtypes = [c_void_p,iType,iType]
lib.ElColSwapDist_c.restype = c_uint
lib.ElColSwapDist_z.argtypes = [c_void_p,iType,iType]
lib.ElColSwapDist_z.restype = c_uint
def ColSwap(A,jTo,jFrom):
  args = [A.obj,jTo,jFrom]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElColSwap_i(*args)
    elif A.tag == sTag: lib.ElColSwap_s(*args)
    elif A.tag == dTag: lib.ElColSwap_d(*args)
    elif A.tag == cTag: lib.ElColSwap_c(*args)
    elif A.tag == zTag: lib.ElColSwap_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElColSwapDist_i(*args)
    elif A.tag == sTag: lib.ElColSwapDist_s(*args)
    elif A.tag == dTag: lib.ElColSwapDist_d(*args)
    elif A.tag == cTag: lib.ElColSwapDist_c(*args)
    elif A.tag == zTag: lib.ElColSwapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

lib.ElSymmetricSwap_i.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwap_i.restype = c_uint
lib.ElSymmetricSwap_s.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwap_s.restype = c_uint
lib.ElSymmetricSwap_d.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwap_d.restype = c_uint
lib.ElSymmetricSwap_c.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwap_c.restype = c_uint
lib.ElSymmetricSwap_z.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwap_z.restype = c_uint
lib.ElSymmetricSwapDist_i.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwapDist_i.restype = c_uint
lib.ElSymmetricSwapDist_s.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwapDist_s.restype = c_uint
lib.ElSymmetricSwapDist_d.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwapDist_d.restype = c_uint
lib.ElSymmetricSwapDist_c.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwapDist_c.restype = c_uint
lib.ElSymmetricSwapDist_z.argtypes = [c_uint,c_void_p,iType,iType]
lib.ElSymmetricSwapDist_z.restype = c_uint
def SymmetricSwap(uplo,A,jTo,jFrom):
  args = [uplo,A.obj,jTo,jFrom]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElSymmetricSwap_i(*args)
    elif A.tag == sTag: lib.ElSymmetricSwap_s(*args)
    elif A.tag == dTag: lib.ElSymmetricSwap_d(*args)
    elif A.tag == cTag: lib.ElSymmetricSwap_c(*args)
    elif A.tag == zTag: lib.ElSymmetricSwap_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElSymmetricSwapDist_i(*args)
    elif A.tag == sTag: lib.ElSymmetricSwapDist_s(*args)
    elif A.tag == dTag: lib.ElSymmetricSwapDist_d(*args)
    elif A.tag == cTag: lib.ElSymmetricSwapDist_c(*args)
    elif A.tag == zTag: lib.ElSymmetricSwapDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Transpose/Adjoint
# -----------------
lib.ElTranspose_s.argtypes = [c_void_p,c_void_p]
lib.ElTranspose_s.restype = c_uint
lib.ElTranspose_d.argtypes = [c_void_p,c_void_p]
lib.ElTranspose_d.restype = c_uint
lib.ElTranspose_c.argtypes = [c_void_p,c_void_p]
lib.ElTranspose_c.restype = c_uint
lib.ElTranspose_z.argtypes = [c_void_p,c_void_p]
lib.ElTranspose_z.restype = c_uint
lib.ElTransposeDist_s.argtypes = [c_void_p,c_void_p]
lib.ElTransposeDist_s.restype = c_uint
lib.ElTransposeDist_d.argtypes = [c_void_p,c_void_p]
lib.ElTransposeDist_d.restype = c_uint
lib.ElTransposeDist_c.argtypes = [c_void_p,c_void_p]
lib.ElTransposeDist_c.restype = c_uint
lib.ElTransposeDist_z.argtypes = [c_void_p,c_void_p]
lib.ElTransposeDist_z.restype = c_uint

lib.ElAdjoint_c.argtypes = [c_void_p,c_void_p]
lib.ElAdjoint_c.restype = c_uint
lib.ElAdjoint_z.argtypes = [c_void_p,c_void_p]
lib.ElAdjoint_z.restype = c_uint
lib.ElAdjointDist_c.argtypes = [c_void_p,c_void_p]
lib.ElAdjointDist_c.restype = c_uint
lib.ElAdjointDist_z.argtypes = [c_void_p,c_void_p]
lib.ElAdjointDist_z.restype = c_uint

def Transpose(A,B,conj=False):
  if A.tag != B.tag:
    raise Exception('Transposing between datatypes not yet supported in Python')
  if type(A) is not type(B): raise Exception('Matrix types must match')
  args = [A.obj,B.obj]
  if type(A) is Matrix:
    if   B.tag == iTag: lib.ElTranspose_i(*args)
    elif B.tag == sTag: lib.ElTranspose_s(*args)
    elif B.tag == dTag: lib.ElTranspose_d(*args)
    elif B.tag == cTag:
      if conj: lib.ElAdjoint_c(*args)
      else:    lib.ElTranspose_c(*args)
    elif B.tag == zTag: 
      if conj: lib.ElAdjoint_z(*args)
      else:    lib.ElTranspose_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   B.tag == iTag: lib.ElTransposeDist_i(*args)
    elif B.tag == sTag: lib.ElTransposeDist_s(*args)
    elif B.tag == dTag: lib.ElTransposeDist_d(*args)
    elif B.tag == cTag:
      if conj: lib.ElAdjointDist_c(*args)
      else:    lib.ElTransposeDist_c(*args)
    elif B.tag == zTag: 
      if conj: lib.ElAdjointDist_z(*args)
      else:    lib.ElTransposeDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

def Adjoint(A,B):
  Transpose(A,B,True)

# Real part
# ---------
# TODO: Version which returns the result instead?
lib.ElRealPart_i.argtypes = [c_void_p,c_void_p]
lib.ElRealPart_i.restype = c_uint
lib.ElRealPart_s.argtypes = [c_void_p,c_void_p]
lib.ElRealPart_s.restype = c_uint
lib.ElRealPart_d.argtypes = [c_void_p,c_void_p]
lib.ElRealPart_d.restype = c_uint
lib.ElRealPart_c.argtypes = [c_void_p,c_void_p]
lib.ElRealPart_c.restype = c_uint
lib.ElRealPart_z.argtypes = [c_void_p,c_void_p]
lib.ElRealPart_z.restype = c_uint
lib.ElRealPartDist_i.argtypes = [c_void_p,c_void_p]
lib.ElRealPartDist_i.restype = c_uint
lib.ElRealPartDist_s.argtypes = [c_void_p,c_void_p]
lib.ElRealPartDist_s.restype = c_uint
lib.ElRealPartDist_d.argtypes = [c_void_p,c_void_p]
lib.ElRealPartDist_d.restype = c_uint
lib.ElRealPartDist_c.argtypes = [c_void_p,c_void_p]
lib.ElRealPartDist_c.restype = c_uint
lib.ElRealPartDist_z.argtypes = [c_void_p,c_void_p]
lib.ElRealPartDist_z.restype = c_uint
def RealPart(A,AReal):
  if AReal.tag != Base(A.tag):
    raise Exception('AReal must have the base datatype of A')
  if type(A) is not type(AReal): raise Exception('Matrix types must match')
  args = [A.obj,AReal.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElRealPart_i(*args)
    elif A.tag == sTag: lib.ElRealPart_s(*args)
    elif A.tag == dTag: lib.ElRealPart_d(*args)
    elif A.tag == cTag: lib.ElRealPart_c(*args)
    elif A.tag == zTag: lib.ElRealPart_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElRealPartDist_i(*args)
    elif A.tag == sTag: lib.ElRealPartDist_s(*args)
    elif A.tag == dTag: lib.ElRealPartDist_d(*args)
    elif A.tag == cTag: lib.ElRealPartDist_c(*args)
    elif A.tag == zTag: lib.ElRealPartDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Imaginary part
# --------------
# TODO: Version which returns the result instead?
lib.ElImagPart_i.argtypes = [c_void_p,c_void_p]
lib.ElImagPart_i.restype = c_uint
lib.ElImagPart_s.argtypes = [c_void_p,c_void_p]
lib.ElImagPart_s.restype = c_uint
lib.ElImagPart_d.argtypes = [c_void_p,c_void_p]
lib.ElImagPart_d.restype = c_uint
lib.ElImagPart_c.argtypes = [c_void_p,c_void_p]
lib.ElImagPart_c.restype = c_uint
lib.ElImagPart_z.argtypes = [c_void_p,c_void_p]
lib.ElImagPart_z.restype = c_uint
lib.ElImagPartDist_i.argtypes = [c_void_p,c_void_p]
lib.ElImagPartDist_i.restype = c_uint
lib.ElImagPartDist_s.argtypes = [c_void_p,c_void_p]
lib.ElImagPartDist_s.restype = c_uint
lib.ElImagPartDist_d.argtypes = [c_void_p,c_void_p]
lib.ElImagPartDist_d.restype = c_uint
lib.ElImagPartDist_c.argtypes = [c_void_p,c_void_p]
lib.ElImagPartDist_c.restype = c_uint
lib.ElImagPartDist_z.argtypes = [c_void_p,c_void_p]
lib.ElImagPartDist_z.restype = c_uint
def ImagPart(A,AImag):
  if AImag.tag != Base(A.tag):
    raise Exception('AImag must have the base datatype of A')
  if type(A) is not type(AImag): raise Exception('Matrix types must match')
  args = [A.obj,AImag.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElImagPart_i(*args)
    elif A.tag == sTag: lib.ElImagPart_s(*args)
    elif A.tag == dTag: lib.ElImagPart_d(*args)
    elif A.tag == cTag: lib.ElImagPart_c(*args)
    elif A.tag == zTag: lib.ElImagPart_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElImagPartDist_i(*args)
    elif A.tag == sTag: lib.ElImagPartDist_s(*args)
    elif A.tag == dTag: lib.ElImagPartDist_d(*args)
    elif A.tag == cTag: lib.ElImagPartDist_c(*args)
    elif A.tag == zTag: lib.ElImagPartDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Update diagonal
# ---------------
lib.ElUpdateDiagonal_i.argtypes = [c_void_p,iType,iType]
lib.ElUpdateDiagonal_i.restype = c_uint
lib.ElUpdateDiagonal_s.argtypes = [c_void_p,sType,iType]
lib.ElUpdateDiagonal_s.restype = c_uint
lib.ElUpdateDiagonal_d.argtypes = [c_void_p,dType,iType]
lib.ElUpdateDiagonal_d.restype = c_uint
lib.ElUpdateDiagonal_c.argtypes = [c_void_p,cType,iType]
lib.ElUpdateDiagonal_c.restype = c_uint
lib.ElUpdateDiagonal_z.argtypes = [c_void_p,zType,iType]
lib.ElUpdateDiagonal_z.restype = c_uint
lib.ElUpdateDiagonalDist_i.argtypes = [c_void_p,iType,iType]
lib.ElUpdateDiagonalDist_i.restype = c_uint
lib.ElUpdateDiagonalDist_s.argtypes = [c_void_p,sType,iType]
lib.ElUpdateDiagonalDist_s.restype = c_uint
lib.ElUpdateDiagonalDist_d.argtypes = [c_void_p,dType,iType]
lib.ElUpdateDiagonalDist_d.restype = c_uint
lib.ElUpdateDiagonalDist_c.argtypes = [c_void_p,cType,iType]
lib.ElUpdateDiagonalDist_c.restype = c_uint
lib.ElUpdateDiagonalDist_z.argtypes = [c_void_p,zType,iType]
lib.ElUpdateDiagonalDist_z.restype = c_uint
def UpdateDiagonal(A,alphaPre,offset=0):
  alpha = TagToType(A.tag)(alphaPre)
  args = [A.obj,alpha,offset]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElUpdateDiagonal_i(*args)
    elif A.tag == sTag: lib.ElUpdateDiagonal_s(*args)
    elif A.tag == dTag: lib.ElUpdateDiagonal_d(*args)
    elif A.tag == cTag: lib.ElUpdateDiagonal_c(*args)
    elif A.tag == zTag: lib.ElUpdateDiagonal_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElUpdateDiagonalDist_i(*args)
    elif A.tag == sTag: lib.ElUpdateDiagonalDist_s(*args)
    elif A.tag == dTag: lib.ElUpdateDiagonalDist_d(*args)
    elif A.tag == cTag: lib.ElUpdateDiagonalDist_c(*args)
    elif A.tag == zTag: lib.ElUpdateDiagonalDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Zero
# ----
lib.ElZero_i.argtypes = [c_void_p]
lib.ElZero_i.restype = c_uint
lib.ElZero_s.argtypes = [c_void_p]
lib.ElZero_s.restype = c_uint
lib.ElZero_d.argtypes = [c_void_p]
lib.ElZero_d.restype = c_uint
lib.ElZero_c.argtypes = [c_void_p]
lib.ElZero_c.restype = c_uint
lib.ElZero_z.argtypes = [c_void_p]
lib.ElZero_z.restype = c_uint
lib.ElZeroDist_i.argtypes = [c_void_p]
lib.ElZeroDist_i.restype = c_uint
lib.ElZeroDist_s.argtypes = [c_void_p]
lib.ElZeroDist_s.restype = c_uint
lib.ElZeroDist_d.argtypes = [c_void_p]
lib.ElZeroDist_d.restype = c_uint
lib.ElZeroDist_c.argtypes = [c_void_p]
lib.ElZeroDist_c.restype = c_uint
lib.ElZeroDist_z.argtypes = [c_void_p]
lib.ElZeroDist_z.restype = c_uint
def Zero(A):
  args = [A.obj]
  if type(A) is Matrix:
    if   A.tag == iTag: lib.ElZero_i(*args)
    elif A.tag == sTag: lib.ElZero_s(*args)
    elif A.tag == dTag: lib.ElZero_d(*args)
    elif A.tag == cTag: lib.ElZero_c(*args)
    elif A.tag == zTag: lib.ElZero_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == iTag: lib.ElZeroDist_i(*args)
    elif A.tag == sTag: lib.ElZeroDist_s(*args)
    elif A.tag == dTag: lib.ElZeroDist_d(*args)
    elif A.tag == cTag: lib.ElZeroDist_c(*args)
    elif A.tag == zTag: lib.ElZeroDist_z(*args)
    else: DataExcept()
  else: TypeExcept()