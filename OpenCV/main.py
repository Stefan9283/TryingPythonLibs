#! /usr/bin/python3
import cv2
import os

dir = "files"
outdir = 'output'

if outdir not in os.listdir('.'):
    os.makedirs(outdir + '/GRAY', 1)
    os.makedirs(outdir + '/BLUR05', 1)
    os.makedirs(outdir + '/BLUR10', 1)

for file in os.listdir(dir):
    # print(file)
    # Read Image
    img = cv2.imread(dir + "/" + file)
    # Display Image
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    out = "/" + os.path.splitext(file)[0]

    # Applying Grayscale filter to image
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Saving filtered image to new file
    ksize = (5, 5)
    blured5 = image = cv2.blur(img, ksize)
    ksize = (10, 10)
    blured10 = image = cv2.blur(img, ksize)

    cv2.imwrite(outdir + '/GRAY'   + out + 'greytest.jpg', grey)
    cv2.imwrite(outdir + '/BLUR05' + out + 'blur05test.jpg', blured5)
    cv2.imwrite(outdir + '/BLUR10' + out + 'blur10test.jpg', blured10)

