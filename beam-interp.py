# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:58:47 2016

@author: Eli Van Cleve
"""
import numpy as np
#import csv
import pandas as pd
import scipy.interpolate as it

def center(z):
    #center line
    #left line: {-809.57212765,-618.2738018510445}
    #point = {z , x}
    # zlp# is the zmin to zman (x in the new coordinate system)
    y = 0
    zlp1 = [-809.57212765,-618.2738018510445]

    # pi1# is the curve ends {z,x}
    pi11 = [-618.2738018510445,180.1213278161587]
    pi12 = [-360.7002437,-0.0002029671569]

    zlp2 = [pi11[0],pi12[0]]
    zlp3 = [-360.7002437,360.7002437] 
    zlp4 = [-pi12[0],-pi11[0]]
    zlp5 = [618.2738018510445,809.57212765]
    
    dir = 'G:/Eli/RadiaBeam/beam/'
    filename = 'xarray.csv'
    x1 = pd.read_csv(dir+filename, header = None, error_bad_lines=False)
    filename = 'yarray.csv'
    y1 = pd.read_csv(dir+filename, header = None, error_bad_lines=False)
    #print (x1)
    index = np.array([6,5,4,3,2,1,0])
    x1A = x1.to_numpy()[0]
    x1A = x1A[index]
    y1A = y1.to_numpy()[0]
    y1A = y1A[index]
    x2A = -x1A[index]
    y2A = y1A[index]
    

    if ((z >= zlp1[0]) and (z <= zlp1[1])):
        # p# {z,x} of the line
        p1 = [-809.57212765,705.709158215]
        p2 = [-618.2738018510445,180.1213278161587]
        m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
        b1 = p1[1]-m1*p1[0]
        x = m1*z + b1
        #print ("linear")
    elif ((z >= zlp2[0]) and (z <= zlp2[1])):
        '''
        x1 = np.array([-618.2738019, -600,-500, -400,-360.7002437])
        y1 =  np.array([180.1213278, 140.3025356, 38.01518394, 2.830464535, -0.000203])
        '''
        t, c, k = it.splrep(x2A, y2A, s=0, k=3)
        N = 100
        xmin, xmax = x1.min(), x1.max()
        xx = np.linspace(xmin, xmax, N)
        spline = it.BSpline(t, c, k)
        x = float(spline(z))
        #print ('first curve')
    elif ((z >= zlp3[0]) and (z <= zlp3[1])):
        #print ('straight')
        x = 0
    elif ((z >= zlp4[0]) and (z <= zlp4[1])):
        #print ('second curve')
        t, c, k = it.splrep(x1A, y1A, s=0, k=3)
        N = 100
        xmin, xmax = x1.min(), x1.max()
        xx = np.linspace(xmin, xmax, N)
        spline = it.BSpline(t, c, k)
        x = float(spline(z))
   
    else:
        p1 = [809.57212765,705.709158215]
        p2 = [618.2738018510445,180.1213278161587]
        m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
        b1 = p1[1]-m1*p1[0]
        x = m1*z + b1
        #print ('last linear')
    return x , y, z

def deriv(z):
    h = 0.0001
    z1 = z-h/2
    z2 = z+h/2
    x1, y1, z10 = center(z1)
    x2, y2, z20 = center(z2)
    return (x2-x1)/(z2-z1)

def beamZ(cz,cx, px, pz,der): #cx, cy, cz is the centerline x,y,z and px, py, pz are for the particles
    #der = deriv(cz)
    cply = cx
    cplx = cz
    cpx = pz
    cpy = px
    b = cx-der*cz
    if der == 0:
        
    return np.sqrt((cplx-(b-cpy)/der)**2+(cply - cpy)**2)

def dist(p1,p2):
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

class Positions:

    def __init__(self, xarray, yarray,zarray):
        self.xarray = xarray
        self.yarray = yarray
        self.zarray = zarray

    def CallArray(self,name):
        if name == 'x':
            return self.xarray
        elif name == 'y':
            return self.yarray
        elif name == 'z':
            return self.zarray
        else:
            return np.array([])



#dir = '/mnt/g/Eli/RadiaBeam/SQF/'
dir = 'G:/Eli/RadiaBeam/beam/'

#filename = input ("Enter File Name: ")

filename = 'beam-k1.csv'

save = filename[:-4]+'-clean.csv'
print (dir+filename)

data = pd.read_csv(dir+filename, error_bad_lines=False)

'''
#Lsize = len(data.Freq)
#Lsize = len(data.lambda(GHz))
colN = len(data.iloc[0])

timeZeroC = []
#timeZero
colNa = np.array([])
for col in data.columns:
    #print (col)
    colNa = np.append(colNa,col)

StoreData = []
'''


dataA = data.to_numpy()

leng = len(dataA[0])
lr = len(dataA)

ParticlePos = np.array([])



beamZZ = np.array([]) 
dpos = np.array([])

#leng = 28

for i in range(1,leng):
    mod = (i-1)%9
    if (mod < 3): 
        #print ("less 3")
        if (mod == 0):
            xpos = np.array([])
            for j in range(lr):
                x = dataA[j][i]
                xpos = np.append(xpos,x)
        if (mod == 1):
            ypos = np.array([])
            for j in range(lr):
                y = dataA[j][i]
                ypos = np.append(ypos,y)
        if (mod == 2):
            zpos = np.array([])
            for j in range(lr):
                z = dataA[j][i]
                zpos = np.append(zpos,z)
    elif (mod == 3):
        #print ("mod = 3")
        Temp = Positions(xpos,ypos,zpos)
        ParticlePos = np.append(ParticlePos,Temp)
        #print ([xpos,ypos,zpos])
  
xs = 'x'
ys = 'y'
zs = 'z'        

num = len(ParticlePos)
#print (len(ParticlePos))


'''
zmean = np.array([])
ymean = np.array([])
xmean = np.array([])
centerPlane = np.array([])
'''

Npar = len(ParticlePos[0].CallArray(xs))
Pplane = np.array([])
centerLine = np.array([])
#print (range(num))
num = 100
for i in range(num):
    '''
    xmean.append(xmean,np.mean(ParticlePos[i][0]))
    ymean.append(ymean,np.mean(ParticlePos[i][1]))
    zzmean = mean(ParticlePos[i][2])
    zmean.append(zmean,np.mean(zzmean))
    centerPlane.append([center(zzmean)])
    '''
    zzmean = np.mean(ParticlePos[i].CallArray(zs))
    cx, cy, cz = center(np.mean(zzmean))
    centerLine = np.append(centerLine,[cx,cy,cz])
    derivt = deriv(cz)
    for j in range(Npar):
        px = ParticlePos[i].CallArray(xs)[j]
        pz = ParticlePos[i].CallArray(ys)[j]
        pdd = beamZ(cz,cx,px,pz,derivt)
        Temp = Positions(pdd,ParticlePos[i].CallArray(ys),np.array([]))
        Pplane = np.append(Pplane,Temp)

exit()

maxD = np.array([])
#print (Pplane[0].CallArray(xs))
exit()
for i in range(num):
    for j in range(Npar):
        dmax = 0
        maxA = np.array([])
        p0 = [Pplane[i].CallArray(xs)[j],Pplane[i].CallArray(ys)[j]]
        for k in range(NPar):
            if (j != k):
                p1 = [Pplane[i].CallArray(xs)[k],Pplane[i].CallArray(ys)[k]]
                dtemp = dist(p0,p1)
                if (dtemp > dmax):
                    dmax = dtemp
        maxA.append(dmax)
        maxDist = np.max(maxA)    
    maxD.append(maxDist)
print (maxD)
exit()
'''
for i in range(leng):
    if (9 > data.Freq[i] > 4):
        StoreData.append(dataA[i])
'''


#df = pd.DataFrame(StoreData, columns = colNa)
#print (df)

#df.to_csv(dir+save, index = False)

