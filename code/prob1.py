import pickle
import sys
import time 
import os
import matplotlib.pyplot as plt
import numpy as np
from pyquaternion import Quaternion
from transforms3d.euler import mat2euler
import mpl_toolkits.mplot3d as a3

def tic():
  return time.time()
def toc(tstart, nm=""):
  print('%s took: %s sec.\n' % (nm,(time.time() - tstart)))

def read_data(fname):
  d = []
  with open(fname, 'rb') as f:
    if sys.version_info[0] < 3:
      d = pickle.load(f)
    else:
      d = pickle.load(f, encoding='latin1')  # needed for python 3
  return d


print("Current Working Directory:", os.getcwd())

dataset="1"
cfile = "C:\Users\kvuon\OneDrive\Documents\Personal\UCSD\ECE 276a\ECE276A_PR1\data\cam" + dataset + ".p"
ifile = "C:\Users\kvuon\OneDrive\Documents\Personal\UCSD\ECE 276a\ECE276A_PR1\data\imu" + dataset + ".p"
vfile = "C:\Users\kvuon\OneDrive\Documents\Personal\UCSD\ECE 276a\ECE276A_PR1\data\vicon" + dataset + ".p"

ts = tic()
camd = read_data(cfile)
imud = read_data(ifile)
vicd = read_data(vfile)
toc(ts,"Data import")

tau=np.array(0)
for i in range(len(imud[0])-1):
    tau = np.append(tau,imud[0][i+1]-imud[0][i]) 

imu_t = imud[0] - imud[0][0] #the time interval is 1/100 seconds

# Plotting ADC IMU Values
fig,axs = plt.subplots(6,1,figsize=(10,20))

for i in range(6):
    axs[i].plot(imu_t,imud[i+1])
    axs[i].ticklabel_format(useOffset=False, style='plain', axis='x')  # Disable offset for each subplot

axs[0].set_title('accel_x')
axs[1].set_title('accel_y')
axs[2].set_title('accel_z')
axs[3].set_title('omega_x')
axs[4].set_title('omega_y')
axs[5].set_title('omega_z')

# Add title to the entire figure
fig.suptitle('ADC IMU Values', fontsize=20)

plt.show()