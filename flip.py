from PIL import Image

img = Image.open("test.jpg.jpg")
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flip.save("result.jpg")
print("✅ 翻转完成！去 chuxuegithub 文件夹打开 result.jpg 查看")
