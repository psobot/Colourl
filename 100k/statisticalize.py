#!/usr/bin/python

import png
import sys
import math

filename = sys.argv[1]
ranking = sys.argv[2]
webname = sys.argv[3]
r = png.Reader(filename)
img = r.asRGBA()
pixels = list(img[2])

aRed = []
aGreen = []
aBlue = []

for line in pixels:
	reds = []
	greens = []
	blues = []
	for pixel in zip(line[::4],  line[1::4],  line[2::4]):
		reds.append(pixel[0])
		greens.append(pixel[1])
		blues.append(pixel[2])
	aRed.append(sum(reds)/len(reds))
	aBlue.append(sum(blues)/len(blues))
	aGreen.append(sum(greens)/len(greens))

averageRed = sum(aRed)/len(aRed)
averageBlue = sum(aBlue)/len(aBlue)
averageGreen = sum(aGreen)/len(aGreen)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

#print ranking+","+webname+","+str(averageRed)+","+str(averageBlue)+","+str(averageGreen)+","+rgb_to_hex((averageRed, averageGreen, averageBlue))
f = open('output.csv', 'a');
f.write(ranking+","+webname+","+str(averageRed)+","+str(averageBlue)+","+str(averageGreen)+","+rgb_to_hex((averageRed, averageGreen, averageBlue))+"\n")
f.close()
