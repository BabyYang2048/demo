# _*_ coding: utf-8 _*_

# time 2018/3/28
# target url 'http://jinyici.xpcha.com/'
# use requests lxml
# 多进程 反义词和近义词同时爬取
# 使用Manager 数据共享

import json

import requests
import sys
import multiprocessing
from multiprocessing import Process, Manager
#from lxml import etree
from lxml import html
etree = html.etree


def headers():
    return {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/62.0.3202.94 Safari/537.36"}


def get_url(url="http://jinyici.xpcha.com/list_0.html"):
    try:
        response = requests.get(url, headers=headers())
    except Exception as f:
        print("出现错误1")
        print(f.args)
        sys.exit(1)

    if response.status_code != 200:
        print(url)
        print("出现错误2")
        sys.exit(1)

    html = response.text
    etree_html = etree.HTML(html)
    all_a = etree_html.xpath("//dl[@class='shaixuan_5']/dd/a")
    head = url.split("com")[0] + "com/"
    words_link = {a.xpath("./text()")[0]: head + a.xpath('./@href')[0] for a in all_a}
    return words_link


def write_json(words_link):
    dict_store = dict()
    for word, link in words_link.items():
        print(word, link)
        try:
            response = requests.get(link, headers=headers())
        except Exception as f:
            print("出现错误3")
            print(f.args)
            sys.exit(1)

        if response.status_code != 200:
            print("出现错误4")
            sys.exit(1)
        etree_html = etree.HTML(response.text)
        all_span = etree_html.xpath("//dl[@class='shaixuan_1']/dd/span")
        all_words = [span.xpath("./text()")[0].strip("：") for span in all_span]
        dict_store[word] = all_words
    return dict_store


def jyc(words_store, maxPage):
    words_list = []
    for page in range(1, maxPage):
        url = "http://jinyici.xpcha.com/list_0_{}.html".format(page)

        words_link = get_url(url=url)
        dict_store = write_json(words_link)
        words_list.append({'page{}'.format(page): dict_store})
        words_store['近义词'] = words_list


def fyc(words_store, maxPage):
    words_list = []
    for page in range(1, maxPage):
        url = "http://fanyici.xpcha.com/list_0_{}.html".format(page)

        words_link = get_url(url=url)
        dict_store = write_json(words_link)
        words_list.append({'page{}'.format(page): dict_store})
    words_store['反义词'] = words_list


if __name__ == "__main__":
    multiprocessing.freeze_support()
    all_words = Manager().dict()

    count = input("Please input the number of the pages:")
    count = int(count)
    count = count+1
    #count = 2  # 5为4页以此类推 反义词和近义词共同的页数

    p_jyc = Process(target=jyc, args=(all_words, count))
    p_fyc = Process(target=fyc, args=(all_words, count))

    p_fyc.start()
    p_jyc.start()

    p_fyc.join()
    p_jyc.join()
    all_words = dict(all_words)
    with open("words.txt", "wb+") as f:
        f.write(json.dumps(all_words, ensure_ascii=False).encode("utf-8"))

print("\n\n完成!!!!")
