# coding=UTF-8
import requests;
import urllib.request;
from lxml import etree

def getUrlLink(file):
    list=[]
    with open(file) as lines:
        for line in lines:
            list.append(line)

    return list

