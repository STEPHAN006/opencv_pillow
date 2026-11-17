from PIL import Image
im = Image.open("image.png")
print(im.format, im.size, im.mode)
im.show()