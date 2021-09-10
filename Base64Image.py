# coding=UTF-8
import os,base64
import requests as req
from PIL import Image
from io import BytesIO
def getBase(url):
    response = req.get(url) # 将这个图片保存在内存
    # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
    image = Image.open(BytesIO(response.content))
    # 得到这个图片的base64编码
    ls_f=base64.b64encode(BytesIO(response.content).read())
    # 打印出这个base64编码

    return "data:image/gif;base64,"+ls_f.decode()

