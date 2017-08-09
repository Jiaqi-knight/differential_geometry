# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computesecondChristoffelsymbol2D(N=None,deltaq=None,covariantbase=None,contravariantbase=None,firstdevneighbours=None,*args,**kwargs):
    varargin = computesecondChristoffelsymbol2D.varargin
    nargin = computesecondChristoffelsymbol2D.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: July 18th, 2014
#    Last update: July 18th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    g1=covariantbase[:,1:2]
    g2=covariantbase[:,3:4]
    #g3 = covariantbase(:,7:9);
    
    G1=contravariantbase[:,1:2]
    G2=contravariantbase[:,3:4]
    #G3 = contravariantbase(:,7:9);
    
    g1d1=zeros(N,2)
    g1d2=zeros(N,2)
    g2d1=zeros(N,2)
    g2d2=zeros(N,2)
    for i in arange(1,N).reshape(-1):
        j1=1
        if 1 == firstdevneighbours[i,dot(4,(j1 - 1)) + 1]:
            g1d1[i,1:2]=multiply(0.5,cat((g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1] - g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]),(g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2] - g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]))) / deltaq[j1]
            g2d1[i,1:2]=multiply(0.5,cat((g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1] - g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]),(g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2] - g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]))) / deltaq[j1]
        else:
            if 2 == firstdevneighbours[i,dot(4,(j1 - 1)) + 1]:
                g1d1[i,1:2]=cat((dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]) + dot(2,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],1])),(dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]) + dot(2,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],2]))) / deltaq[j1]
                g2d1[i,1:2]=cat((dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]) + dot(2,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],1])),(dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]) + dot(2,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],2]))) / deltaq[j1]
            else:
                if 3 == firstdevneighbours[i,dot(4,(j1 - 1)) + 1]:
                    g1d1[i,1:2]=cat((dot(1.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]) - dot(2,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1]) + dot(0.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],1])),(dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]) + dot(2,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],2]))) / deltaq[j1]
                    g2d1[i,1:2]=cat((dot(1.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],1]) - dot(2,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],1]) + dot(0.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],1])),(dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 2],2]) + dot(2,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 3],2]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j1 - 1)) + 4],2]))) / deltaq[j1]
        j2=2
        if 1 == firstdevneighbours[i,dot(4,(j2 - 1)) + 1]:
            g1d2[i,1:2]=multiply(0.5,cat((g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1] - g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]),(g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2] - g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]))) / deltaq[j2]
            g2d2[i,1:2]=multiply(0.5,cat((g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1] - g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]),(g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2] - g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]))) / deltaq[j2]
        else:
            if 2 == firstdevneighbours[i,dot(4,(j2 - 1)) + 1]:
                g1d2[i,1:2]=cat((dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]) + dot(2,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],1])),(dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]) + dot(2,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],2]))) / deltaq[j2]
                g2d2[i,1:2]=cat((dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]) + dot(2,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],1])),(dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]) + dot(2,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],2]))) / deltaq[j2]
            else:
                if 3 == firstdevneighbours[i,dot(4,(j2 - 1)) + 1]:
                    g1d2[i,1:2]=cat((dot(1.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]) - dot(2,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1]) + dot(0.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],1])),(dot(- 1.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]) + dot(2,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2]) - dot(0.5,g1[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],2]))) / deltaq[j2]
                    g2d2[i,1:2]=cat((dot(1.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],1]) - dot(2,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],1]) + dot(0.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],1])),(dot(- 1.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 2],2]) + dot(2,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 3],2]) - dot(0.5,g2[firstdevneighbours[i,dot(4,(j2 - 1)) + 4],2]))) / deltaq[j2]
    
    secondChristoffelsymbol=matlabarray(cat(sum(multiply(g1d1,G1),2),sum(multiply(g1d2,G1),2),sum(multiply(g2d1,G1),2),sum(multiply(g2d2,G1),2),sum(multiply(g1d1,G2),2),sum(multiply(g1d2,G2),2),sum(multiply(g2d1,G2),2),sum(multiply(g2d2,G2),2)))
    return secondChristoffelsymbol