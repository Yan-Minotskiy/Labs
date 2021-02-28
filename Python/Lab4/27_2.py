from PIL import Image, ImageDraw

image = Image.open("temp.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()


def image_filter1(pixels, i, j):
    """Заменяет цвет исходного пикселя на средний относительно его окружения"""
    r, g, b = 0, 0, 0
    for row in range(11):
        for col in range(11):
            if row != i or col != j:
                r += pixels[row, col][0]
                g += pixels[row, col][1]
                b += pixels[row, col][2]
    return r // 120, g // 120, b // 120


def image_filter2(pixels, i, j, depth):
    """Сепия"""
    a = pixels[i, j][0]
    b = pixels[i, j][1]
    c = pixels[i, j][2]
    S = (a + b + c) // 3
    a = S + depth * 2
    b = S + depth
    c = S
    if a > 255:
        a = 255
    if b > 255:
        b = 255
    if c > 255:
        c = 255
    return a, b, c


def image_filter3(pixels, i, j, ):
    """Негатив"""
    a = pix[i, j][0]
    b = pix[i, j][1]
    c = pix[i, j][2]
    return 255 - a, 255 - b, 255 - c


print(help(image_filter1))