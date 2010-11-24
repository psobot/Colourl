#!/usr/bin/python

import sys
import Image
import ImageStat

filename = sys.argv[1]
ranking = sys.argv[2]
webname = sys.argv[3]

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

print 'Reading image...'
try:
	im = Image.open(filename)
except:
	print 'Invalid png for '+webname
	exit()

print 'Statisticalizing... '
stat = ImageStat.Stat(im)
mean = stat.mean
avg = (int(round(mean[0])), int(round(mean[1])), int(round(mean[2])))
print 'average: ' + str(avg) + ' (' + rgb_to_hex(avg) + ')'

f = open('output.csv', 'a');
f.write(ranking+","+webname+","+str(avg[0])+","+str(avg[1])+","+str(avg[2])+","+rgb_to_hex(avg)+"\n")
f.close()

print 'Done.'
