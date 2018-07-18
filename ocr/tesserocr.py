from PIL import Image

image = Image.open('/home/zhanghang/tmp/timg.jpeg')
print(tesserocr.image_to_text(image))
