# coding=utf-8

from PIL import Image, ImageDraw

if __name__ == "__main__":
    # img_path = "imgs/aori.jpg"
    # img = Image.open(img_path, "r")
    # print(img.size)
    # for item in dir(img):
    #     print(item)
    #
    # img.show()
    # box = (0, 0, 200, 200)
    # img_crop = img.crop(box)
    # img_crop.show()

    w, h = 200, 200
    r = 50
    img = Image.new("RGB", (w, h), color="white")
    img1 = ImageDraw.Draw(img)
    img1.rectangle((0, 0, w - r, h - r), fill="red")
    img1.chord((w - r - r / 2 - 0.375 * r, h / 2 - r, w - r / 2 - 0.375 * r, h / 2), start=30, end=330, fill="white")
    img1.chord((w / 2 - r, h - r - r / 2 + 0.375 * r, w / 2, h - r / 2 + 0.375 * r), start=-60, end=240, fill="red")
    img.show()
    img.save("./result/p1.png")



