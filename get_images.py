import os
import requests
import random
import shutil
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html,'lxml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")
    return link

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name+".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

if "__main__" == __name__:
    CICLE = 500
    SAVE_DIR = os.getcwd() + "/data/"
    DEFAULT_NAME = "img"
    count = 1

    if not os.path.exists(SAVE_DIR):
        print("cannot found %s.¥n create this directory!" % SAVE_DIR)
        os.mkdir(SAVE_DIR)

    data = input("検索ワード:")
   
    if os.path.exists(SAVE_DIR+"/"+data):
        os.mkdir(SAVE_DIR+"/"+data)
    
    save_path = SAVE_DIR + "/" + data
        
    for _ in range(CICLE):
        try:
            link = image(data)
            download_img(link, save_path+DEFAULT_NAME+str(count))
            print("OK")
            count += 1
        except:
            print("catch exception")
