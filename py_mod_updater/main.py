from inspect import ismethod
import zlib
import urllib.request
import os
import sys
import ssl
import re

from sympy import false


def crc32(file_path):
    """
    计算文件 crc32 hash 值
    """
    with open(file_path, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)


# 用户头部
ssl._create_default_https_context = ssl._create_unverified_context
opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


print("星泽工艺服务器Mod更新器 v0.2")

print("正在拉取列表...")

# 下载列表
try:
    urllib.request.urlretrieve(
        "https://yunling.de/files/MTR_Server/list", "list.txt")

except Exception as ex:
    print("列表拉取失败，请根据下方打印出的错误信息判断问题")
    print(ex)
    input()
    sys.exit()

# 打开列表并加载内容

lastetEdit = ''
modList = []

with open('list.txt', 'r') as file:
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
            if functionCheck == 'Xingze Craft Mod Updater Mod List':
                countLine += 1
                continue
            if functionCheck == '-lastet_edited':
                lastetEdit = re.search('(?<=\$).*', thisLine)
                lastetEdit = lastetEdit.group()
                countLine += 1
                continue
            if functionCheck == 'endl':
                break
            if functionCheck == '^':
                temp = re.search('(?<=\$).*', thisLine)
                temp = temp.group()
                modList.append(temp)
                countLine += 1
                continue
print('mod最后修改：'+str(lastetEdit))
print('已拉取到以下mod：'+str(modList))

# 获取crc列表
try:
    urllib.request.urlretrieve(
        "https://yunling.de/files/MTR_Server/crc", "crc")

except Exception as ex:
    print("CRC列表拉取失败，请根据下方打印出的错误信息判断问题")
    print(ex)
    input()
    sys.exit()

crcList = []

with open('crc', 'r') as file:
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
            if functionCheck == 'Xingze Craft Mod Updater Mod CRC List':
                countLine += 1
                continue
            if functionCheck == '-lastet_edited':
                lastetEdit = re.search('(?<=\$).*', thisLine)
                lastetEdit = lastetEdit.group()
                countLine += 1
                continue
            if functionCheck == 'endl':
                break
            if functionCheck == '^':
                temp = re.search('(?<=\$).*', thisLine)
                temp = temp.group()
                crcList.append(temp)
                countLine += 1
                continue
print('CRC最后修改：'+str(lastetEdit))

#大小写转换
crcCount = 0
for i in crcList:
    crcList[crcCount] = str.upper(i)
    crcCount+=1



# 检查CRC
crcCount = 0
isModLastet = 0
while crcCount < len(crcList):
    if os.path.exists(modList[crcCount]) and str(crc32(modList[crcCount])) == crcList[crcCount]:
        print(modList[crcCount]+'为最新版本')
        isModLastet+=1
    crcCount+=1

if isModLastet == len(crcList):
    print('所有mod为最新，按任意键关闭...')
    input()
    sys.exit()


# 下载mod
modListLen = len(modList)
for i in modList:
    print('正在下载：'+i+'...')
    try:
        urllib.request.urlretrieve(
            "https://yunling.de/files/MTR_Server/"+i, i)
        print(i+'下载完成')

    except Exception as ex:
        print(i+"下载失败，请根据下方打印出的错误信息判断问题")
        print(ex)
        input()
        sys.exit()

# 校验CRC
crcCount = 0
for i in modList:
    if not crc32(i) == crcList[crcCount]:
        print(i+' CRC校验失败，这意外着此mod可能存在坏档，建议重新运行更新器')
        input("按任意键退出")
        sys.exit()
    crcCount+=1

print('mod更新完成')
print('所有mod为最新，按任意键关闭...')
input()
sys.exit()