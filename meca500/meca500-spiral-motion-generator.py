# this program is to generate a meca500 trajectory
import numpy as np
import matplotlib.pyplot as plt

#x,y nominal linear paths
xl = [-16, -20, -20, -6.66,  -6.66,   6.66,  6.66,  20,  20]
yl = [-16, -20,  20, 20, -20, -20, 20,  20, -20]
t_len = [0.0, 0.3025, 2.1395, 0.7130, 2.1395, 0.7130, 2.1395, 0.7130, 2.1395]
t_int = np.cumsum(t_len)

##--Designing the x, y paths as functions of time
#define the times between trajectory motion pattern changes
#total time for first spiral pass = 11 seconds
#total distance for nominal spiral pass = 205.657 mm
#total distance for spiral = 1649.23 mm
#nominal path speed = 18.6961 mm/second
t_total = 11.0 #seconds
t_res = 0.025 #resolution of output
d_total = 205.657 #mm
v_l_ave = d_total/t_total

# nominal x,y postion given time
def xlyl(t):
    if t<t_int[1]:
        mx1 = (xl[1]-xl[0])/(t_int[1]-t_int[0])
        xlt = mx1*t+xl[0]
        my1 = (yl[1]-yl[0])/(t_int[1]-t_int[0])
        ylt = my1*t+yl[0]
    elif t<t_int[2]:
        xlt = xl[1]
        my1 = (yl[2]-yl[1])/(t_int[2]-t_int[1])
        ylt = my1*t+(yl[1]-my1*t_int[1])
    elif t<t_int[3]:
        mx1 = (xl[3]-xl[2])/(t_int[3]-t_int[2])
        xlt = mx1*t+(xl[2]-mx1*t_int[2])
        ylt = yl[2]
    elif t<t_int[4]:
        xlt = xl[3]
        my1 = (yl[4]-yl[3])/(t_int[4]-t_int[3])
        ylt = my1*t+(yl[3]-my1*t_int[3])
    elif t<t_int[5]:
        mx1 = (xl[5]-xl[4])/(t_int[5]-t_int[4])
        xlt = mx1*t+(xl[4]-mx1*t_int[4])
        ylt = yl[4]
    elif t<t_int[6]:
        xlt = xl[5]
        my1 = (yl[6]-yl[5])/(t_int[6]-t_int[5])
        ylt = my1*t+(yl[5]-my1*t_int[5])
    elif t<t_int[7]:
        mx1 = (xl[7]-xl[6])/(t_int[7]-t_int[6])
        xlt = mx1*t+(xl[6]-mx1*t_int[6])
        ylt = yl[6]
    elif t<t_int[8]:
        xlt = xl[7]
        my1 = (yl[8]-yl[7])/(t_int[8]-t_int[7])
        ylt = my1*t+(yl[7]-my1*t_int[7])
    return xlt, ylt

# nominal x,y postion given time
def xcyc(t):
    A = 6
    w = 25#4.1818
    phi = np.pi*.25
    xct = A*np.cos(w*t+phi)
    yct = A*np.sin(w*t+phi)
    return xct, yct

def eucDist(x1,y1,x2,y2):
    edist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return edist

#sunscreen initial dots
spread = 16
x_ss = [-spread, -spread, -spread,  0.0, 0.0,   0.0,  spread, spread, spread]
y_ss = [-spread,   0.0,  spread, spread, 0.0, -spread, -spread,  0.0, spread]

##--Designing the x,y paths in mm
#HD6 plate dims
x_HD6 = [-25,-25,25,25,-25]
y_HD6 = [-25,25,25,-25,-25]

#HD6 plate substrate dims
x_sub_HD6 = [-24,-24,24,24,-24]
y_sub_HD6 = [-24,24,24,-24,-24]

t = 0;
t_count = [0.0];
xlt = [xl[0]]
ylt = [yl[0]]
xct_int, yct_int = xcyc(0.0)
xct = [xct_int]
yct = [yct_int]
while(t<t_int[8]):
    xlt_new, ylt_new = xlyl(t)
    xlt = xlt+[xlt_new]
    ylt = ylt+[ylt_new]
    xct_new, yct_new = xcyc(t)
    xct = xct+[xct_new]
    yct = yct+[yct_new]
    t_count = t_count + [t]
    t = t+t_res

plt.figure(1)
plt.plot(x_HD6, y_HD6,'g-')
plt.plot(x_sub_HD6, y_sub_HD6,'r-')
plt.plot(x_ss,y_ss,'b.')
plt.plot(xl,yl,'b--')
plt.ylabel('Y (mm)')
plt.xlabel('X (mm)')
plt.axis('equal')
plt.show(block=False)
x_t = np.array(xlt)+np.array(xct)
y_t = np.array(ylt)+np.array(yct)
plt.plot(x_t,y_t,'c-')
plt.draw()
    
# plt.figure(2)
# plt.ylabel('distance (mm)')
# plt.xlabel('time (seconds)')
# plt.plot(t_count,xlt,'r-')
# plt.plot(t_count,ylt,'g-')
# plt.plot(t_count,xct,'c-')
# plt.plot(t_count,yct,'m-')
# plt.show(block=False)

d_t = [0.0]
for i in list(range(x_t.size-1)):
    d_t = d_t+[eucDist(x_t[i],y_t[i],x_t[i+1],y_t[i+1])]
    
d_path_total = np.max(np.cumsum(d_t))
v_path_ave = d_path_total/t_total #mm/s

f = open('meca_gui_script_spiral.txt', 'w')
with open('meca_gui_script_spiral.txt', 'w') as f:
    for i in list(range(x_t.size)):
        f.write(str('MoveLin('+str(round(x_t[i],3))+', '+str(round(y_t[i],3))+', 0, 0, 0, 0)\n'))
f.close()