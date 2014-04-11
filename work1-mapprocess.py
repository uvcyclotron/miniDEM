'''
Assignment for the Multimedia Project
Utkarsh Verma
2011A7PS137P

Map Image Processing Module
'''
from __future__ import print_function
import numpy
import cv2 as cv
from matplotlib import pyplot
import json
from colorama import init, Fore, AnsiToWin32
import sys


#load the contour map
img = cv.imread("f4.png",1)
ht =img.shape[0]
wd =img.shape[1]

#color palette list with RGB values in land height order
palette=[
[180,105, 255], #pink 0 
[140, 180, 210], #brown
[131, 0,   0], #indigo 1 
[227, 0,   0], #blue 2 
[255,71,   0], #lightblue
[255,171,   0], #skyblue
[239, 255,  15], #cyan
[135, 255, 119], #green
[ 35, 255, 219], #yellow
[  0, 187, 255], #orange
[  0,  88, 255], #darkorange 0,87,255
[  0,   0, 237], #red
[  0,   0, 131] #maroon
]

#dict mapping for colors to index numbers
colors = {
     0:	'pink' ,
     1:	'brown' ,
	 2:	'indigo',
	 3:	'blue' ,
	 4:	'ltblue' ,
	 5: 'skblue' ,
	 6: 'cyan' ,
	 7:	'green' ,
	 8:	'yellow' ,
	 9:	'orange' ,
	10:	'dkorng' ,
    11:	'red' ,
	12: 'maroon' 	
}

#this is for coloured output in terminal
colorama_palette = [
'\x1b[37m',
'\x1b[37m',
'\x1b[34m',
'\x1b[34m\x1b[1m',
'\x1b[36m\x1b[2m',
'\x1b[36m\x1b[22m',
'\x1b[36m\x1b[1m',
'\x1b[32m\x1b[1m',
'\x1b[32m', #yellow
'\x1b[33m\x1b[1m',
'\x1b[33m',
'\x1b[31m\x1b[1m',
'\x1b[31m'
]

#get the index of palette color closest to this pixel color
def grabClosest(px):
	b=px[0]
	g=px[1]
	r=px[2]
	mindist = 10000000 #init with large value
	minindex = -1 #init indicates no match
	for i in range(len(palette)):
		bi=palette[i][0]
		gi=palette[i][1]
		ri=palette[i][2]
		#find euclid dist in RGB cube to this color
		dist = (b-bi)**2 + (g-gi)**2 + (r-ri)**2 
		#((r - r1) * .299)^2 + ((g - g1) * .587)^2 + ((b - b1) * .114)^2 ##HSV dist. try later.
		if(mindist > dist):
			mindist = dist
			minindex = i
	#print mindist, b,g,r
	return minindex 

#array storing z-indices of mesh points
mesh_zind = []
RR = 50 #square mesh grid size on each side
for i in range(RR):
	zind_row=[]
	for j in range(RR):
		sj =  j*ht/RR;
		si =  i*wd/RR;
		#print sj,si,
		px= img[si,sj]
		#print px
		ind = grabClosest(px)
		init() #to init the colorama library
#		print colors[ind]," ",
		print(colorama_palette[ind]+ colors[ind]+"\t",end='')
		zind_row.append(ind)
		#print palette.index([px[0],px[1],px[2]])
	mesh_zind.append(zind_row)
   	print('\n')

print(Fore.RESET)
#store the z-indices for further processing by maya module
f = open('meshdata.txt','w')
json.dump(mesh_zind,f)

#show the img using plt
img2 = img[:,:,::-1] #shift from imread's BGR to pyplot's RGB
pyplot.imshow(img2,interpolation='bicubic')
pyplot.show()