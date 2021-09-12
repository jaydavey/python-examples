# this program is to generate a meca500 trajectory
import numpy as np
import matplotlib.pyplot as plt

def eucDist(x1,y1,x2,y2):
    edist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return edist

t_resolution = 0.010 #timestamp every 0.1 seconds


##--Designing the x,y paths in mm
#HD6 plate dims
x_HD6 = [-25,-25,25,25,-25]
y_HD6 = [-25,25,25,-25,-25]

#HD6 plate substrate dims
x_sub_HD6 = [-24,-24,24,24,-24]
y_sub_HD6 = [-24,24,24,-24,-24]

#x,y nominal linear paths
xl = [-16, -20, -20, -8,  -8,   8,  8,  20,  20]
yl = [-16, -20,  20, 20, -20, -20, 20,  20, -20]

#sunscreen initial dots
spread = 16
x_ss = [-spread, -spread, -spread,  0.0, 0.0,   0.0,  spread, spread, spread]
y_ss = [-spread,   0.0,  spread, spread, 0.0, -spread, -spread,  0.0, spread]

##--Designing the x, y paths as functions of time
#define the times between trajectory motion pattern changes
#total time for first spiral pass = 11 seconds
#total distance for nominal spiral pass = 205.657 mm
#nominal path speed = 18.6961 mm/second
t_len = [0.3025, 2.1395, 0.6418, 2.1395, 0.8558, 2.1395, 0.6418, 2.1395]
tl = np.concatenate((np.array([0]),np.cumsum(t_len)), axis=0)

#calculate the nominal corner to corner trajectory velociites
dxl = np.zeros(tl.size-1)
for i in list(range(tl.size-1)):
    print(i)
    print(eucDist(xl[i],yl[i],xl[i+1],yl[i+1]))
    dxl[i] = eucDist(xl[i],yl[i],xl[i+1],yl[i+1])
dtl = np.diff(tl)
vl = np.divide(dxl,dtl)

plt.show(block=False)
t = 0;
while(t<1000):
    ##--Plot x, y paths in mm
    plt.figure(100)
    plt.plot(x_HD6, y_HD6,'g-')
    plt.plot(x_sub_HD6, y_sub_HD6,'r-')
    plt.plot(x_ss,y_ss,'b.')
    plt.plot(xl,yl,'b--')
    plt.ylabel('Y (mm)')
    plt.xlabel('X (mm)')
    plt.axis('equal')
    plt.show(block=False)
    plt.draw()
    t = t+1
    print(t)
    
    
