from PIL import Image
import os
import math
import random

keywords = ['snake', 'chameleon']

pixelsperimage = 500

images = []
for keyword in keywords:
    files = os.listdir('images/' + keyword)
    images += [keyword + '/' + file for file in files]

random.shuffle(images)

N = len(images)

n = math.floor(math.sqrt(N))

collage = Image.new('RGBA', (n * pixelsperimage, n * pixelsperimage), 
                    color=(255, 255, 255, 255))

k = 0
for i in range(0, n * pixelsperimage, pixelsperimage):
    for j in range(0, n * pixelsperimage, pixelsperimage):

        image = Image.open('images/' + images[k]).convert('RGBA')
        image = image.resize((pixelsperimage, pixelsperimage))

        collage.paste(image, (i,j))                  

        k += 1


collage.save('collages/' + '_'.join(keywords) + '.png')