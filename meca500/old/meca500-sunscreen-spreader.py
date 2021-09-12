# this program is to generate a meca500 trajectory
import numpy as np
import matplotlib.pyplot as plt

t_resolution = 0.010 #timestamp every 0.1 seconds

#sunscreen initial dots
spread = 16
x_ss = [-spread, -spread, -spread,  0.0, 0.0,   0.0,  spread, spread, spread]
y_ss = [-spread,   0.0,  spread, spread, 0.0, -spread, -spread,  0.0, spread]


#define the length of the segments of time (in seconds) where the path changes direction
t0_len = 0.5 #seconds of trajectory
t1_len = 5.0 #seconds of trajectory
t2_len = 1.0 #seconds of trajectory
t3_len = 5.0 #seconds of trajectory
t4_len = 1.0 #seconds of trajectory
t5_len = 5.0 #seconds of trajectory
t6_len = 1.0 #seconds of trajectory
t7_len = 5.0 #seconds of trajectory

# #cumulative time
# figure(1)
# plt.axvline(x=t0_len,'-r')


t0 = np.multiply(list(range(int(t0_len/t_resolution))), t_resolution) 
t1 = np.multiply(list(range(int(t1_len/t_resolution))), t_resolution) + t0_len 
t2 = np.multiply(list(range(int(t2_len/t_resolution))), t_resolution) + t0_len + t1_len  
t3 = np.multiply(list(range(int(t3_len/t_resolution))), t_resolution) + t0_len + t1_len + t2_len
t4 = np.multiply(list(range(int(t4_len/t_resolution))), t_resolution) + t0_len + t1_len + t2_len + t3_len 
t5 = np.multiply(list(range(int(t5_len/t_resolution))), t_resolution) + t0_len + t1_len + t2_len + t3_len + t4_len
t6 = np.multiply(list(range(int(t6_len/t_resolution))), t_resolution) + t0_len + t1_len + t2_len + t3_len + t4_len + t5_len
t7 = np.multiply(list(range(int(t7_len/t_resolution))), t_resolution) + t0_len + t1_len + t2_len + t3_len + t4_len + t5_len + t6_len

#path0

#path1
xp1_start = -20
yp1_start = -22
xp1_end = -20
yp1_end = 22

A=5
B=xp1_start
w1=np.multiply(4,np.pi)
w2=np.multiply(4,np.pi)
C=2.5
D=8.8
E=yp1_start+1

x1 = np.multiply(A,np.sin(np.multiply(w1,t1-t0_len)))+B
y1 = np.multiply(C,-np.cos(np.multiply(w2,t1-t0_len)))+np.multiply(D,t1-t0_len)+E

#path2
xp2_start = xp1_end
yp2_start = yp1_end
xp2_end = -8
yp2_end = yp1_end

A=5
B=xp2_start
w1=np.multiply(0.5,np.pi)
w2=np.multiply(0.5,np.pi)
C=2.5
D=2.5
E=yp2_start

x2 = np.multiply(A,np.cos(np.multiply(w1,t1-t0_len)))+np.multiply(D,t1-t0_len)+B
y2 = np.multiply(C,-np.sin(np.multiply(w2,t1-t0_len)))+E

#path3
xp3_start = xp2_end
yp3_start = yp2_end
xp3_end = xp2_end
yp3_end = yp1_start

#path4
xp4_start = xp3_end
yp4_start = yp3_end
xp4_end = 8
yp4_end = yp3_end

#path5
xp5_start = xp4_end
yp5_start = yp4_end
xp5_end = 8
yp5_end = yp3_start

#path6
xp6_start = xp5_end
yp6_start = yp5_end
xp6_end = 20
yp6_end = yp5_end

#path7
xp7_start = xp6_end
yp7_start = yp6_end
xp7_end = xp6_end
yp7_end = yp5_start


#plot of x,y path
plt.figure(100)
plt.plot([-25,-25,25,25,-25],[-25,25,25,-25,-25],'g-')
plt.plot([-24,-24,24,24,-24],[-24,24,24,-24,-24],'r-')
plt.plot(x_ss,y_ss,'b.')
plt.plot([xp1_start,xp2_start,xp3_start,xp4_start,xp5_start,xp6_start,xp7_start,xp7_end],[yp1_start,yp2_start,yp3_start,yp4_start,yp5_start,yp6_start,yp7_start,yp7_end],'b-')
plt.ylabel('Y (mm)')
plt.xlabel('X (mm)')
plt.plot(x1,y1,'c-')
plt.plot(x2,y2,'m-')
plt.axis('equal')
plt.show()