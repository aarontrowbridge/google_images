from google_images_download import google_images_download as gid
import os

response = gid.googleimagesdownload()

keywords = "chamelion"

arguments = {"keywords": keywords, "limit": 10, "output_directory": "images"}

response.download(arguments)

