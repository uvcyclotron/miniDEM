'''
Assignment for the Multimedia Project
Utkarsh Verma
2011A7PS137P

Maya Module
'''

from pymel.core import *
import json

f= newFile(f=1)

RR = 50 #no of mesh subdivisions on each side. equal to preset in module1.
CUT = RR-1 #sections
objs = polyPlane(sx=CUT,sy=CUT,w=30,h=30)
mapmesh = objs[0]

#load the mesh data from previous module
zind=[]
f = open('path/to/file/meshdata.txt','r')
zind = json.load(f)

#set z-indices for all mesh points (y in Maya)
for i in range(len(zind)):
	row = zind[i]
	for j in range(len(row)):
		y = row[j]
		k=i*len(zind)+j
		#print k,y," "
		pos = mapmesh.vtx[k].getPosition()
		mapmesh.vtx[k].setPosition([pos[0],-y,pos[2]])
