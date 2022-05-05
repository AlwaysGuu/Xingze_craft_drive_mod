import json,urllib.request,os,sys,urllib3,hashlib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


print("Xingze Craft Mod Updater v0.1")

print("Self Check...")

if not( os.path.exists('MTR.jar')) :
    print("Can't found MTR mod. Do you want to download?")
    print("d - Download c - Cancel")
    if input("Choose:") == "d":
        try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/MTR.jar","MTR.jar")
        except Exception as ex:
            print("Error!")
            print(ex)
            input()
            sys.exit()
    else:
        sys.exit()

if not( os.path.exists('joban.jar')) :
    print("Can't found joban mod. Do you want to download?")
    print("d - Download c - Cancel")
    if input("Choose:") == "d":
        try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/joban.jar","joban.jar")
        except Exception as ex:
            print("Error!")
            print(ex)
            input()
            sys.exit()
    else:
        sys.exit()



print("Getting Updates...")

try:
    urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/md5.txt","md5.txt")

except Exception as ex:
    print("Error to getting upadtes!")
    print(ex)
    input()
    sys.exit()

with open('md5.txt',"r") as f:
    MTR_MD5 = f.readlines()[0].strip()

    print("Latest MTR mod MD5:"+MTR_MD5)


with open('md5.txt',"r") as f:

    j_MD5 = f.readlines()[1].strip()

    print("Latest joban mod MD5:"+j_MD5)


with open('MTR.jar',"rb") as f:
    file = f.read()
if hashlib.md5(file).hexdigest() != MTR_MD5:
    print("Server has new MTR mod, downloading...")
    try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/MTR.jar","MTR.jar")
    except Exception as ex:
        print("Error!")
        print(ex)
        input()
        sys.exit()
else:
    print("Your MTR mod is latest")

with open('joban.jar',"rb") as f:
    file = f.read()
if hashlib.md5(file).hexdigest() != j_MD5:
    print("Server has new joban mod, downloading...")
    try:
            urllib.request.urlretrieve("https://yunling.de/files/MTR_Server/joban.jar","joban.jar")
    except Exception as ex:
        print("Error!")
        print(ex)
        input()
        sys.exit()
else:
    print("Your Joban mod is latest")

print("All mods are latest!, Have a fun!")