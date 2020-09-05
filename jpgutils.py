from glob import glob                                                           
import cv2 
import os

# we'll run it manually like this:
# $ python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from jpgutils import convert_png_to_jpg
# >>> convert_png_to_jpg()
# >>> exit()
def convert_png_to_jpg():
    mydir = "datasetposff"
    pngs = glob(mydir+'/*.png')
    for j in pngs:
        img = cv2.imread(j)
        cv2.imwrite(j[:-3] + 'jpg', img)
    #delete the files png
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))