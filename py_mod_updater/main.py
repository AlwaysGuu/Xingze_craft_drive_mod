import json,urllib.request,os,sys,hashlib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


print("星泽工艺服务器Mod更新器 v0.1")

print("正在自检...")

if not( os.path.exists('MTR.jar')) :
    print("无法找到MTR mod，是否要下载？")
    print("d - 下载 c - 取消")
    if input("选择（输入字母后回车）:") == "d":
        try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/MTR.jar","MTR.jar")
        except Exception as ex:
            print("下载失败！错误信息：")
            print(ex)
            input()
            sys.exit()
    else:
        sys.exit()

if not( os.path.exists('joban.jar')) :
    print("无法找到joban mod，是否要下载？")
    print("d - 下载 c - 取消")
    if input("选择（输入字母后回车）:") == "d":
        try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/joban.jar","joban.jar")
        except Exception as ex:
            print("下载失败!")
            print(ex)
            input()
            sys.exit()
    else:
        sys.exit()

if not( os.path.exists('XZD.jar')) :
    print("无法找到驱动 mod，是否要下载？")
    print("d - 下载 c - 取消")
    if input("选择（输入字母后回车）:") == "d":
        try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/XZD.jar","XZD.jar")
        except Exception as ex:
            print("下载失败!")
            print(ex)
            input()
            sys.exit()
    else:
        sys.exit()



print("正在检查更新...")

try:
    urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/md5.txt","md5.txt")

except Exception as ex:
    print("mod md5值拉取失败！")
    print(ex)
    input()
    sys.exit()

with open('md5.txt',"r") as f:
    MTR_MD5 = f.readlines()[0].strip()

    #print("Latest MTR mod MD5:"+MTR_MD5)


with open('md5.txt',"r") as f:

    j_MD5 = f.readlines()[1].strip()

    #print("Latest joban mod MD5:"+j_MD5)

with open('md5.txt',"r") as f:

    D_MD5 = f.readlines()[2].strip()

    #print("Latest Drive mod MD5:"+D_MD5)


with open('MTR.jar',"rb") as f:
    file = f.read()
if hashlib.md5(file).hexdigest() != MTR_MD5:
    print("有新的MTR mod，正在下载更新...")
    try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/MTR.jar","MTR.jar")
    except Exception as ex:
        print("下载失败!")
        print(ex)
        input()
        sys.exit()
else:
    print("MTR mod为最新")

with open('joban.jar',"rb") as f:
    file = f.read()
if hashlib.md5(file).hexdigest() != j_MD5:
    print("有新的Joban mod，正在下载更新...")
    try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/joban.jar","joban.jar")
    except Exception as ex:
        print("下载失败!")
        print(ex)
        input()
        sys.exit()
else:
    print("Joban mod为最新")

with open('XZD.jar',"rb") as f:
    file = f.read()
if hashlib.md5(file).hexdigest() != D_MD5:
    print("有新的驱动 mod，正在下载更新...")
    try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/XZD.jar","XZD.jar")
    except Exception as ex:
        print("下载失败!")
        print(ex)
        input()
        sys.exit()
else:
    print("驱动 mod为最新")


print("全部mod为最新")
input("按任意键退出...")