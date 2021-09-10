# coding=UTF-8
import save2mHtml
import  sys
import getLink

if __name__ == "__main__":
    isFile=False
    isUrl=False
    dwonloadPath=""
    filePath=""
    url=""

    commds=sys.argv;
    for i in range(1,len(commds)):

        if( commds[i] == '-f' ):
            isFile=True
            filePath=commds[i+1]
            i = 1
            break
        elif( commds[i] == '-u' ):
            isUrl=True
            url = commds[i + 1]
            i += 1
            break
        elif(commds[i] == '-h'):

            break
        else:
            print("你输入的命令无法识别，请重新输入...")

    if(isFile):
        list = getLink.getUrlLink(filePath)
        for url in list:
            save2mHtml.save2mHtml(url,dwonloadPath)

    elif(isUrl):
        print(url)
