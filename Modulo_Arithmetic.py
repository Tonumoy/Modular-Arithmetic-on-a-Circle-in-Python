# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:55:36 2020

@author: Tonumoy
"""

import numpy as np
import matplotlib.pyplot as plt
#import time

i=0
mult_list=[]
mod_list=[]
multiplier = int (input('Enter Multiplier : '))
no_points = int (input('Enter Number of points :'))
theta=360/no_points 
points=[]
p1=[0,1]
circle=plt.Circle((0,0),1,color = 'r',fill=False,linewidth= 4)
fig, ax=plt.subplots() 
ax.add_artist(circle) 
#for j in range (0, multiplier):
#    j+= 1
def transformation(point, angle, list1):
    a=[np.cos(np.radians(angle)), np.sin(np.radians(angle))] 
    b=[-np.sin(np.radians(angle)), np.cos(np.radians(angle))] 
    matrix=[a,b]
    point2=list(np.dot(matrix,point))
    list1.append(point2)
    
while i<no_points: 
    transformation(p1,theta*i,points)
    i+=1
    
num_list=[i for i in range(0,no_points)]#position of points on circle for i in num_list:

for i in num_list:
    s=multiplier*i
    mult_list.append(s)#multipling position of points by the multiplier mod_sums=[s%no_points for s in mult_list]
    
mod_sums=[s%no_points for s in mult_list]
points2=[]

for i in mod_sums: 
    s=points[i]
    points2.append(s) 
    
x,y=zip(*points) 
plt.axis("equal") 
plt.axis('off')
x=[]
y=[]
c=[]
z=[]

for i in points:
    x.append(i[0])
    y.append(i[1]) 
for i in points2:
    c.append(i[0])
    z.append(i[1])
    
i=0

while i<len(x):
    plt.plot([x[i],c[i]],[y[i],z[i]],'k', linewidth=0.5)
    plt.title ('Multiplier =  %i' %multiplier, loc='center')
    
    i+=1 
    #plt.title ('\nNumber Of Points: %i' %no_points, loc='center')
    plt.show()


