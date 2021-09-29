from google_images_download import google_images_download as gid

response = gid.googleimagesdownload()

keywords = "chameleon,snake"
num_images = 10

arguments = {"keywords": keywords, "limit": num_images, "output_directory": "images"}

response.download(arguments)

