from PIL import Image

image = Image.open("photo1.jpg")

image.thumbnail((200, 200))

image.save("thumbnail.jpg")