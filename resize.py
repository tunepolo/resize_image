from PIL import Image

img = Image.open('元画像.jpg')

Lsize = (600, 450) if img.width > img.height else (450, 600)
L2size = (1200, 900) if img.width > img.height else (900, 1200)
L3size = (1800, 1350) if img.width > img.height else (1350, 1800)

img.resize(Lsize, Image.BICUBIC).save('L_バイキュービック.jpg', img.format, quality=80)

img.resize(L2size, Image.LANCZOS).save('2L_ランチョス_Q80.jpg', img.format, quality=80)
img.resize(L2size, Image.LANCZOS).save('2L_ランチョス_Q85.jpg', img.format, quality=85)
img.resize(L3size, Image.LANCZOS).save('3L_ランチョス_Q85.jpg', img.format, quality=85)

img.resize(Lsize, Image.LANCZOS).save('L_ランチョス_Q80.jpg', img.format, quality=80)
img.resize(Lsize, Image.LANCZOS).save('L_ランチョス_Q85.jpg', img.format, quality=85)
img.resize(Lsize, Image.LANCZOS).save('L_ランチョス_Q90.jpg', img.format, quality=90)
img.resize(Lsize, Image.LANCZOS).save('L_ランチョス_Q95.jpg', img.format, quality=95)
