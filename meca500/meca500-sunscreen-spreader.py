# this program is to generate a meca250 trajectory
import numpy as np
import matplotlib.pyplot as plt

#create a series of timestamps to define points in time
t_resolution = 0.100 #timestamp every 0.1 seconds
t0_len = 0.5 #seconds of trajectory
t1_len = 5.0 #seconds of trajectory
t2_len = 1.0 #seconds of trajectory
t3_len = 5.0 #seconds of trajectory
t4_len = 1.0 #seconds of trajectory
t5_len = 5.0 #seconds of trajectory
t6_len = 1.0 #seconds of trajectory
t7_len = 5.0 #seconds of trajectory

#sunscreen initial dots
spread = 16
x_ss = [-spread, -spread, -spread,  0.0, 0.0,   0.0,  spread, spread, spread]
y_ss = [-spread,   0.0,  spread, spread, 0.0, -spread, -spread,  0.0, spread]


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
yp1_start = -20
xp1_end = -20
yp1_end = 20

xp1 = [xp1_start]*len(t1)
yp1 = np.multiply(t1-t0_len,8)+yp1_start

#path2

#plot
plt.plot([-25,-25,25,25,-25],[-25,25,25,-25,-25],'g-')
plt.plot([-24,-24,24,24,-24],[-24,24,24,-24,-24],'r-')
plt.plot(x_ss,y_ss,'b.')
plt.plot(xp1,yp1,'b-')
plt.ylabel('Y (mm)')
plt.xlabel('X (mm)')
plt.show()