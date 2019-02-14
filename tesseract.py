#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytesseract
from PIL import Image
import time
import os

direct = 'C:\\Users\L1308\Desktop\Python Demo\project\image\cut'
list = os.listdir(direct)

start = time.time()
flag = 1
for img in list:
    name = direct+'\\'+img
    print('---scaning---')
    image = Image.open(name)
    code = pytesseract.image_to_string(image)
    print(str(flag)+"     :     "+img+'    :'    +code)
    flag+=1
end = time.time()
amount = end - start
print("用时:"+str(amount))