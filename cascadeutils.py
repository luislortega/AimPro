import os

# reads all the files in the /negative folder and generates neg.txt from them.
# we'll run it manually like this:
# $ python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from cascadeutils import generate_negatives
# >>> generate_negatives()
# >>> exit()
def generate_negatives():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('datasetnegff'):
            f.write('datasetnegff/' + filename + '\n')
            #f.write('negative/' + filename + '/n')

# the opencv_annotation executable can be found in opencv/build/x64/vc15/bin
# generate positive description file using:
# $ C:/Users/luis_/OneDrive/Escritorio/OpenCV/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/

# You click once to set the upper left corner, then again to set the lower right corner.
# Press 'c' to confirm.
# Or 'd' to undo the previous confirmation.
# When done, click 'n' to move to the next image.
# Press 'esc' to exit.
# Will exit automatically when you've annotated all of the images

# generate positive samples from the annotations to get a vector file using:
# $ C:/Users/luis_/OneDrive/Escritorio/OpenCV/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# train the cascade classifier model using: (El doble de positivos y el numero de negativos)
# $ C:/Users/luis_/OneDrive/Escritorio/OpenCV/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24

# my final classifier training arguments:
# $ C:/Users/luis_/OneDrive/Escritorio/OpenCV/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 200 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999
