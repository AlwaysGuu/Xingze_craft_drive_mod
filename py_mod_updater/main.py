from fileinput import filelineno
from itertools import count
from operator import mod
import urllib.request
import os
import sys
import ssl
import re

# 用户头部
ssl._create_default_https_context = ssl._create_unverified_context
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


print("星泽工艺服务器Mod更新器 v0.1")

print("正在拉取列表...")
'''
# 下载列表
try:
    urllib.request.urlretrieve(
        "https://yunling.de/files/MTR_Server/list", "list")

except Exception as ex:
    print("列表拉取失败，请根据下方打印出的错误信息判断问题")
    print(ex)
    input()
    sys.exit()

# 打开列表并加载内容
'''
lastetEdit = ''
modList = []

with open('list', 'r') as file:
    checkEnd = 0
    countLine = 0
    functionCheck = ''
    fileLines = file.readlines()
    while not(checkEnd):
        thisLine = fileLines[countLine]
    
        functionCheck = re.search('(?<=@).*?(?=\$)', thisLine)
        if functionCheck != None:
            functionCheck = functionCheck.group()
        if not(functionCheck == None):
            if functionCheck == 'Xingze Craft Mod Updater Config':
                countLine += 1
                continue
            if functionCheck == '-lastet_edited':
                lastetEdit = re.search('(?<=\$).*', thisLine)
                lastetEdit = lastetEdit.group()
                countLine += 1
                continue
            if functionCheck == 'endl':
                break
        if re.search('\^', thisLine) == '^':
            temp = re.search('(?<=\^).*',thisLine)
            temp = temp.group()
            modList.append(temp)
            countLine += 1
            continue
print(modList)
