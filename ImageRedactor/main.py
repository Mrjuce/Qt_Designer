from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("original.jpg") as pic_original:
    print("Зображення відкрито: \n Розмір:", pic_original.size)
    print("Формат", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert("L")
    pic_gray.save("gray.jpg")
    print("Зображення відкрито: \n Розмір:", pic_gray.size)
    print("Формат", pic_gray.format)
    print("Тип:", pic_gray.mode)
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("pic_up.jpg")
    pic_up.show()

    mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    mirrow.save("mirrow.jpg")
    mirrow.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save("contr.jpg")
    pic_contrast.show()