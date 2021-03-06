# -----------------------------------------------------------------------------------------------------------------------------
# IMAGE SPLITTER (IMSPLIT)
# -----------------------------------------------------------------------------------------------------------------------------
# Author: Antonio Oliver Gelabert (ORCID : http://orcid.org/0000-0001-8571-2733)
# -----------------------------------------------------------------------------------------------------------------------------
# Accepted input formats : TIF, JPG, PNG, GIF
# -----------------------------------------------------------------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------------------------------------------------------------
#   nx, ny : number of splitts per dymension (nx,ny)
#   dt,bt : don't output images below or above RGB mean threshold
# -----------------------------------------------------------------------------------------------------------------------------
# Usage examples
# -----------------------------------------------------------------------------------------------------------------------------
# python Imsplit.py                             => Will produce splitted output folder for each image imput file with default
#                                                  values (2x2 split and no filter)
# -----------------------------------------------------------------------------------------------------------------------------
# python Imsplit.py -nx 3 -ny 6                 => Will produce for each image 3x6=18 splits inside output folder for each input file  
# -----------------------------------------------------------------------------------------------------------------------------
# python Imsplit.py -nx 3 -ny 6 -dt 10 -bt 200  => Will produce for each image 3x6=18 splits inside output folder for each input file
#                                                  and output only images which RGB mean value is bigger than 10 and lower than 200

from datetime import datetime
import sys
import os
import cv2
import numpy as np
import warnings
import argparse
import time as tm

print('---------------------------------------------------------------------------------------------------------------')
print('---------------------------    IMAGE SPLITTER (IMSPLIT)    ----------------------------------------------------')
print('---------------------------------------------------------------------------------------------------------------')
print('     Author: Antonio Oliver Gelabert (ORCID : http://orcid.org/0000-0001-8571-2733)                            ')
print('---------------------------------------------------------------------------------------------------------------')
print('                   Accepted input formats : TIF, JPG, PNG, GIF                                                 ')
print('---------------------------------------------------------------------------------------------------------------')
print('                                Parameters                                                                     ')
print('---------------------------------------------------------------------------------------------------------------')
print('             nx, ny : number of splitts per dymension (nx,ny)                                                  ')
print('             dt,bt : do not output images below or above RGB mean threshold                                    ')
print('             dir : Directory of input images                                                                   ')
print('---------------------------------------------------------------------------------------------------------------')
print(' ----------------------------    Usage examples     -----------------------------------------------------------')
print('---------------------------------------------------------------------------------------------------------------')
print('python Imsplit.py                             => Will produce splitted output folder for each image input      ')
print('                                                 file with default values (2x2 split and no filter)            ')
print('---------------------------------------------------------------------------------------------------------------')
print('python Imsplit.py -nx 3 -ny 6                 => Will produce for each image 3x6=18 splits inside output       ')
print('                                                 folder for each input file                                    ')
print('---------------------------------------------------------------------------------------------------------------')
print('python Imsplit.py -nx 3 -ny 6 -dt 10 -bt 200) => Same as above and output only images which RGB mean           ')
print('                                                 value is bigger than 10 and lower than 200                    ')        
print('---------------------------------------------------------------------------------------------------------------')
print('                                  OUTPUTS : RGB mean values                                                    ')
print('---------------------------------------------------------------------------------------------------------------')

# Start counting time seconds to evaluate total time spent by running the program
t0= tm.clock()

# Parsing optional arguments of the program  
ap = argparse.ArgumentParser()
ap.add_argument("-ny", "--subdy", required=False, default='2', help="Number of x divisions (E.g. '-nx 5' will produce 5 subdivisions in y direction or height). Default value :2")
ap.add_argument("-nx", "--subdx", required=False, default='2', help="Number of y divisions (E.g. '-ny 5' will produce 5 subdivisions in x direction or width). Default value :2")
ap.add_argument("-dt", "--dt", required=False, default='0', help="Low threshold brightness filter (between 0 and 255, close to 0 and bigger, to exclude dark images). Default value:0")
ap.add_argument("-bt", "--bt", required=False, default='255', help="High threshold brightness filter (between 0 and 255, close to 255 and lower, to exclude bright images). Default value:255")
ap.add_argument("-dir", "--dirim", required=False, default=".", help="Path of input images. Default value: Current directory ")
args = vars(ap.parse_args())

# Assign args to program variables
directory_in_str=args["dirim"]
subdx=int(args["subdy"])
subdy=int(args["subdx"])
dt=int(args["dt"])
bt=int(args["bt"])
directory = os.fsencode(directory_in_str)

# Ignore warning messages
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# Create string with date and time to be used as label folders
now = datetime.now() 
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%Y%m%d_%H%M%S")

# Loop for all images inside current directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    dirstr=str(date_time)
    if (filename.endswith(".tif")) or (filename.endswith(".jpg")) or (filename.endswith(".png")) or (filename.endswith(".gif")):#&(filename.startswith("SNAP")):
# Create a folder for each image input        
        os.mkdir(directory_in_str+"/split_"+dirstr+"_"+filename[:-3])
        contpic2=cv2.imread(directory_in_str+"/"+filename)
# Compute image dymensions        
        xs=np.shape(contpic2)[0]
        ys=np.shape(contpic2)[1]
# definition of subdivision steps for each dymension (height, width) 
        dh=int(xs/subdx)
        dw=int(ys/subdy)
        
# Make the splits, filter and label
        for k in range(0,subdx,1):
            for j in range(0,subdy,1):
                subpic=contpic2[k*dh:(k+1)*dh,j*dw:(j+1)*dw]
                # Exclude pictures with low portion of tissue
                avgc = np.mean(subpic)
                print(filename+" average RGB value: ",round(avgc,2),"+/-",round(np.std(subpic),2))
# Here the filter to output images between RGB mean values in bt-dt range                
                if (avgc < bt) & (avgc > dt):
                    cv2.imwrite(directory_in_str+"/split_"+dirstr+"_"+filename[:-3]+"/"+filename[:-4]+"_"+str(k)+"_"+str(j)+".tif", contpic2[k*dh:(k+1)*dh,j*dw:(j+1)*dw])

t1= tm.clock()
print("************************************************************************************************************")
print("************************************************************************************************************")
t1 = tm.clock()
print("Job time (s) : ", np.round(t1 - t0,2)) 
print("************************************************************************************************************")
print("************************************************************************************************************") 
