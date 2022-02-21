from bs4 import BeautifulSoup
import requests
import lxml
import os
import json
from unittest import result
import pyrebase
# from firebase import firebase

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
    'http': os.getenv('HTTP_PROXY')
}

# params = {
#    "hl": "th",
#     "user": "CcfsliIAAAAJ"
# }


def get_articles(params):
    html = requests.get('https://scholar.google.com/citations',
                        headers=headers, params=params, proxies=proxies).text
    soup = BeautifulSoup(html, 'lxml')
    data = []
    print('Article info:')
    for article_info in soup.select('#gsc_a_b .gsc_a_t'):
        title = article_info.select_one('.gsc_a_at').text
        title_link = f"https://scholar.google.com{article_info.select_one('.gsc_a_at')['href']}"
        authors = article_info.select_one('.gsc_a_at+ .gs_gray').text
        publications = article_info.select_one('.gs_gray+ .gs_gray').text

        data.append({
            'title': title,
            'title_link': title_link,
            'authors': authors,
            'publications': publications,
        })
    # print(f'Title: {title}\nTitle link: {title_link}\nArticle Author(s): {authors}\nArticle Publication(s): {publications}\n')
    return data


def get_timetable1(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'html.parser', from_encoding="windows-874")
    # soup.encode("windows-874")
    tb = soup.find_all(
        "table", {"border": "1", "cellspacing": "0", "cellpadding": "0"})
    return str(tb[0]).replace("¨Ñ¹·Ãì", "จันทร์").replace("ÍÑ§¤ÒÃ", "อังคาร").replace("¾Ø¸", "พุธ").replace("¾ÄËÑÊº´Õ","พฤหัสบดี").replace("ÈØ¡Ãì","ศุกร์").replace("ÍÒ·ÔµÂì","อาทิตย์").replace("àÊÒÃì","เสาร์")

def getData():
    config = {
        "apiKey": "AIzaSyA952ethtCSD2FZsX2rABd6FzsPttYX0ws",
        "authDomain": "csitproject-a3814.firebaseapp.com",
        "databaseURL": "https://csitproject-a3814-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "csitproject-a3814",
        "storageBucket": "csitproject-a3814.appspot.com",
        "messagingSenderId": "26361500700",
        "appId": "1:26361500700:web:0420b0ff86d117748d3bd9",
        "measurementId": "G-VZQ1RJDWVC"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    result = db.child("Wansuree_Massagram").child("status").get().val()
    return result
# article = get_articles()
# print(len(data))
# print(data)
# print(json.dumps(article, indent = 2, ensure_ascii = False))
