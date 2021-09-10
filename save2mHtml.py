# coding=UTF-8
import requests;
import urllib.request;
from lxml import etree
import  re
import Base64Image
import  os

def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

    }

    html = requests.get(url,headers=headers)

    html.encoding='utf-8'

    xpHtml = etree.HTML(html.text)

    imgurl = xpHtml.xpath('//div[@class="rich_media_content "]//*/img/@data-src')

    result = ""

    title = xpHtml.xpath('//h1[@class="rich_media_title"]/text()')[0]
    title = title.strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('|','_')
    print("正在获取 < "+title+" > 网页信息请稍等.......")
    for i in range(len(imgurl)):

        if i == 0:
            result = re.sub("data-src=", "src=\"" + Base64Image.getBase(imgurl[i])+"\"", html.text, count=1)
        else:
            result = re.sub("data-src=", "src=\"" + Base64Image.getBase(imgurl[i]) + "\"", result, count=1)


    return result,title

def saveHtml(path,file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(path+file_name+ ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)
        f.close()


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")


def save2mHtml(url,dwonload):
    html,title = getHtml(url)
    print("正在保存 < "+title+" > .......")

    if(dwonload==""):
        mkdir(os.path.abspath('.') + "\\dwonload")
        saveHtml(os.path.abspath('.')+"\\dwonload\\",title, html.encode())
    else:
        mkdir(dwonload+"\dwonload\\")
        saveHtml(dwonload+"\dwonload\\",title, html.encode())