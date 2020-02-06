# Imsplit

Python program to split images in separated outputs with optional exclusion filter by brigthness values

**Accepted input formats:** *TIF, JPG, PNG, GIF*

**Parameters**
+ nx, ny : number of splitts in x and y axis (Width and Height: nx,ny)
+ dt,bt  : don't output images below or above RGB mean threshold
+ dir    : Path of directory with input images

**Usage examples**
+ python Imsplit.py                             => Will produce splitted output folder for each image using with default values
+ python Imsplit.py -dir test                   => Will produce splitted output folder for each image in test folder
+ python Imsplit.py -nx 3 -ny 6                 => Will produce for each image 3x6=18 splits inside output folder for each input file 
+ python Imsplit.py -nx 3 -ny 6 -dt 10 -bt 200  => Same as above but output only images which RGB mean vaues are whinthin the range 10-200

**General usage:**
+ Imsplit.py [-h] [-ny SUBDY] [-nx SUBDX] [-dt DT] [-bt BT] [-dir DIRIM]

**Optional arguments:**

+ h, --help                 Show this help message and exit
+ ny SUBDY, --subdy SUBDY  Number of x divisions (E.g. '-nx 5' will produce 5
                           subdivisions in y direction or height). Default value:2
+ nx SUBDX, --subdx SUBDX   Number of y divisions (E.g. '-ny 5' will produce 5
                           subdivisions in x direction or width). Default value:2
+ dt DT, --dt DT            Low threshold brightness filter (between 0 and 255,
                           close to 0 and bigger, to exclude dark images).
                           Default value:0
+ bt BT, --bt BT            High threshold brightness filter (between 0 and 255,
                           close to 255 and lower, to exclude bright images).
                           Default value:255 
+ dir DIRIM, --dirim DIRIM  Path of input images. Default value: Current directory
