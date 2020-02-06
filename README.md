# Imsplit

Python program to split images in separated outputs with optional exclusion filter by brigthness values

**Accepted input formats:** *TIF, JPG, PNG, GIF*


**General usage:**
+ Imsplit.py [-h] [-ny SUBDY] [-nx SUBDX] [-dt DT] [-bt BT] [-dir DIRIM]

**Optional parameters**
+ nx, ny : number of splitts in x and y axis (Width and Height: nx,ny). By default nx=2, ny=2
+ dt,bt  : don't output images below or above RGB mean threshold. By default, dt=0, bt=255 (i.e. not filtered)
+ dir    : Path of directory with input images (by default, current directory of python script execution)
+ h      : help message

**Usage examples**
+ python Imsplit.py                             => Will produce splitted output folder for each image using default values
+ python Imsplit.py -dir test                   => Will produce splitted output folder for each image in test folder
+ python Imsplit.py -nx 3 -ny 6                 => Will produce for each image 3x6=18 splits inside output folder for each input file 
+ python Imsplit.py -nx 3 -ny 6 -dt 10 -bt 200  => Same as above but output only images which RGB mean vaues are whinthin the range 10-200
+ python Imsplit.py -h                          => display help 

