import csv

reader = csv.reader(open("output.csv", "rb"))
writer = csv.writer(open("data.csv", "wb"))
hues = []

def rgbToHSV(r, g, b):
    """Convert RGB color space to HSV color space
    
    @param r: Red
    @param g: Green
    @param b: Blue
    return (h, s, v)  
    """
    maxc = max(r, g, b)
    minc = min(r, g, b)
    colorMap = {
        id(r): 'r',
        id(g): 'g',
        id(b): 'b'
    }
    if colorMap[id(maxc)] == colorMap[id(minc)]:
        h = 0
    elif colorMap[id(maxc)] == 'r':
        h = ((g - b) * 60.0 / (maxc - minc)) % 360
    elif colorMap[id(maxc)] == 'g':
        h = ((b - r) * 60.0 / (maxc - minc)) + 120
    elif colorMap[id(maxc)] == 'b':
        h = ((r - g) * 60.0 / (maxc - minc)) + 240
    v = maxc
    if maxc == 0.0:
        s = 0.0
    else:
        s = 1 - (minc * 1.0 / maxc)
    return (h, s, v)

rownum = -1
for row in reader:
    rownum += 1
    if rownum == 0:
        continue
    rank = row[0]
    site = row[1]
    r = row[2]
    g = row[3]
    b = row[4]
    hexstr = row[5]
    if r == g and r == b:
        print site + ' (' + hexstr + ') lacks any colour, ignoring.'
    else:
        hue = int(round(rgbToHSV(int(row[2]), int(row[3]), int(row[4]))[0]))
        hues.append(hue)
        print 'hue: ' + str(hue) + ' \t for site' + site
        writer.writerow((rank, site, hue))

print '\n' + 'average hue: ' + str(int(round((sum(hues) / len(hues)))))
