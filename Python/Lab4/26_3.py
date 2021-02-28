from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = im.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
    res.save('res.jpg')


makeanagliph('image.jpg', 1000)
