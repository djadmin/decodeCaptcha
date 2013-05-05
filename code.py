from PIL import Image
img=Image.open("vit.bmp")

img=img.convert("RGBA")

pixdata=img.load()

for y in xrange(img.size[1]):
	for x in xrange(img.size[0]):
		if pixdata[x,y]==(23,133,12,255):
			pixdata[x,y]=(0,0,0,255)
		else: pixdata[x,y]=(255,255,255,255)

		
img.save("vit-black.gif","GIF")


#import sys

# python chop.py [chop-factor] [in-file] [out-file]

chop = int(1)
image = Image.open('vit-black.gif').convert('1')
width, height = image.size
data = image.load()

# Iterate through the rows.
for y in range(height):
    for x in range(width):

        # Make sure we're on a dark pixel.
        if data[x, y] > 128:
            continue

        # Keep a total of non-white contiguous pixels.
        total = 0

        # Check a sequence ranging from x to image.width.
        for c in range(x, width):

            # If the pixel is dark, add it to the total.
            if data[c, y] < 128:
                total += 1

            # If the pixel is light, stop the sequence.
            else:
                break

        # If the total is less than the chop, replace everything with white.
        if total <= chop:
            for c in range(total):
                data[x + c, y] = 255

        # Skip this sequence we just altered.
        x += total


# Iterate through the columns.
for x in range(width):
    for y in range(height):

        # Make sure we're on a dark pixel.
        if data[x, y] > 128:
            continue

        # Keep a total of non-white contiguous pixels.
        total = 0

        # Check a sequence ranging from y to image.height.
        for c in range(y, height):

            # If the pixel is dark, add it to the total.
            if data[x, c] < 128:
                total += 1

            # If the pixel is light, stop the sequence.
            else:
                break

        # If the total is less than the chop, replace everything with white.
        if total <= chop:
            for c in range(total):
                data[x, y + c] = 255

        # Skip this sequence we just altered.
        y += total

image.save('vit-hack.gif')

from pytesser import *
image=Image.open('vit-hack.gif')
print image_to_string(image)
