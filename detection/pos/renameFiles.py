from glob import glob           
from PIL import Image
import os
import re

location = "pos_test_images(300 images)\\*"
cvFile = ".png"
rmFile = ".png"

convertFiles = glob(location+cvFile)
removeFiles = glob(location+rmFile)


# convert files
for img in convertFiles:
    im = Image.open(img)
    img = re.sub(rmFile,'',img) # 파일명에서 .png 제거
    rgb_im = im.convert('RGB')
    rgb_im.save(img+'.bmp')

# remove files
for img in removeFiles:
    os.remove(img)    
    
    