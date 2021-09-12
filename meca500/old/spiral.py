# this program is to generate a meca250 trajectory
import numpy as np
import matplotlib.pyplot as plt

#create a series of timestamps to define points in time
t_resolution = 0.100 #timestamp every 0.1 seconds
t0_len = 0.5 #seconds of trajectory
t1_len = 5.0 #seconds of trajectory

t0 = np.multiply(list(range(int(t0_len/t_resolution))), t_resolution) 
t1 = np.multiply(list(range(int(t1_len/t_resolution))), t_resolution) + t0_len 

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
plt.subplot(121)
plt.plot([-25,-25,25,25,-25],[-25,25,25,-25,-25],'g-')
plt.plot([-24,-24,24,24,-24],[-24,24,24,-24,-24],'r-')
plt.ylabel('Y (mm)')
plt.xlabel('X (mm)')

plt.subplot(122)
plt.plot(t1,t1,'r-')

plt.show()
