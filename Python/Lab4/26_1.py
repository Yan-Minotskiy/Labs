from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    r = 0
    g = 0
    b = 0
    for i in range(new_image.size[0]):
        draw.line((i, 0, i, 512), fill=(r, g, b), width=2)
        if i % 4 == 0:
            if color == "R" or color == "r":
                r += 2
            elif color == "G" or color == "g":
                g += 2
            elif color == "B" or color == "b":
                b += 2
    new_image.save("res.png", "PNG")
