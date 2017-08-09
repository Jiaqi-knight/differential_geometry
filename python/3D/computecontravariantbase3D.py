# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computecontravariantbase3D(covariantbase=None,sqrtg=None,*args,**kwargs):
    varargin = computecontravariantbase3D.varargin
    nargin = computecontravariantbase3D.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: May 28th, 2014
#    Last update: May 28th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    g1=covariantbase[:,1:3]
    g2=covariantbase[:,4:6]
    g3=covariantbase[:,7:9]
    G1=cat((multiply(g2[:,2],g3[:,3]) - multiply(g2[:,3],g3[:,2])),(multiply(g2[:,3],g3[:,1]) - multiply(g2[:,1],g3[:,3])),(multiply(g2[:,1],g3[:,2]) - multiply(g2[:,2],g3[:,1]))) / cat(sqrtg,sqrtg,sqrtg)
    G2=cat((multiply(g3[:,2],g1[:,3]) - multiply(g3[:,3],g1[:,2])),(multiply(g3[:,3],g1[:,1]) - multiply(g3[:,1],g1[:,3])),(multiply(g3[:,1],g1[:,2]) - multiply(g3[:,2],g1[:,1]))) / cat(sqrtg,sqrtg,sqrtg)
    G3=cat((multiply(g1[:,2],g2[:,3]) - multiply(g1[:,3],g2[:,2])),(multiply(g1[:,3],g2[:,1]) - multiply(g1[:,1],g2[:,3])),(multiply(g1[:,1],g2[:,2]) - multiply(g1[:,2],g2[:,1]))) / cat(sqrtg,sqrtg,sqrtg)
    contravariantbase=matlabarray(cat(G1,G2,G3))
    return contravariantbase