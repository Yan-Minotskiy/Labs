from PIL import Image


def make_preview(size, n_color):
    image = Image.open('image.jpg')
    image = image.resize(size).quantize(n_color)
    image.image.save('image.bmp')

