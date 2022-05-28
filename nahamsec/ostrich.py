import imageio
from PIL import Image, GifImagePlugin
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
import random
from apng import APNG

filenames = []
flag = "REDACTED" 

orig_filename = "ostrich.jpg"
orig_image = Image.open(orig_filename)
old_pixels = orig_image.load()
pixels = orig_image.load()
width, height = orig_image.size
images = []

res_filename = "result.apng"
res_image = Image.open(res_filename)
new_pixels = res_image.load()

res=0
for x in range(width):
        for y in range(height):
            new_pixels[x,y] = res_image.getpixel((x, y))
            old_pixels[x,y] = orig_image.getpixel((x, y))
            if new_pixels[x,y][2] == 0 and new_pixels[x,y][0] != old_pixels[x,y][0]:
                print(new_pixels[x,y])
                # res=res+1
print("ENDDDDDDD")

for i in range(len(flag)):
    new_filename = f'./ostrich{i}.png'
    new_image = Image.new(orig_image.mode, orig_image.size)
    new_pixels = new_image.load()
    for x in range(width):
        for y in range(height):
            new_pixels[x,y] = orig_image.getpixel((x, y))

    x = random.randrange(0,width)
    y = random.randrange(0,height)
    print(x,y)
    pixel = list(orig_image.getpixel((x, y)))
    print(pixel)

    while(pixel[2] == 0):
        x = random.randrange(0,width)
        y = random.randrange(0,height)
        pixel = list(orig_image.getpixel((random.randrange(0,width), random.randrange(0,height))))
        print("AAAAa")
    
    aaaa=pixel[2]*ord(flag[i])
    new_val = l2b(pixel[2]*ord(flag[i]))
    print(new_val)
    print(aaaa)
    print(aaaa//256)
    print(new_val[0])
    print(aaaa%256)
    print(new_val[1])
    pixel[0] = new_val[0]
    if len(new_val) > 1:
        pixel[1] = new_val[1]
    pixel[2] = 0

    new_pixels[x, y] = (pixel[0], pixel[1], pixel[2])
    new_image.save(new_filename)
    filenames.append(new_filename)
    images.append(new_image)
    print("AAAAAAAAAAAAAAAAAAAaa")

APNG.from_files(filenames, delay=0).save("result1.apng")
print(filenames)
