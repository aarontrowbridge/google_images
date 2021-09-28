from PIL import Image, ImageDraw
import os
import math

keyword = "chameleon"

images = os.listdir("images/" + keyword)

N = len(images)

n = math.floor(math.sqrt(N))

pixelsperimage = 500

collage = Image.new("RGBA", (n * pixelsperimage, n * pixelsperimage), 
                    color=(255, 255, 255, 255))

k = 0
for i in range(0, n * pixelsperimage, pixelsperimage):
    for j in range(0, n * pixelsperimage, pixelsperimage):

        image = Image.open("images/" + keyword + "/" + images[k]).convert("RGBA")
        image = image.resize((pixelsperimage, pixelsperimage))

        collage.paste(image, (i,j))

        k += 1


collage.save("collages/" + keyword + ".png")