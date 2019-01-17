#!/usr/bin/python
from pyexiftool import exiftool
import os
import cv2

imgs = os.listdir("origin")
print "images", len(imgs)

#arg = {"xmp:PersonInImage":"maozedonggggggggggg", "xmp:HierarchicalSubject":"youzhi"}
#arg = {"FlightYawDegree":12.08, "FlightPitchDegree":-0.003211, "FlightRollDegree":89.9, "GimbalRollDegree":0.0, "GimbalYawDegree": 90.01, "GimbalPitchDegree":10.5}
arg = {"NewXMPxxxTag1":555.65}
#et = exiftool.ExifTool()

for i in range(3):
    img = cv2.imread("origin/"+imgs[i])
    img = cv2.resize(img, (100, 100))
    img_name = "ch_%d.jpg"%i
    cv2.imwrite(img_name, img)
    with exiftool.ExifTool() as et:
        et.set_tags(arg, img_name)
        #et.execute("-GPSLongitude=180.1888\n-GPSLatitude=32.8888\n-GPSAltitude=55.2101", img_name)
        #et.execute("-ExifRoll=-1.123", img_name)
        #et.execute("-ExifYaw=0.01", img_name)
        #et.execute("-ExifPitch=33.5", img_name)
        #et.execute("-ExifCameraYaw=-133.5", img_name)
    
#et.terminate()

#    os.remove(img_name+"_original")
#    cv2.imwrite(img_name, img)

#fileno='fcdp0.jpg'

#with exiftool.ExifTool() as et:
#    et.execute("-GPSLongitude=100.1888",fileno)
#    et.execute("-GPSLatitude=32.8888",fileno)
