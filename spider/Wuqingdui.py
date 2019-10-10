# -*- coding: utf-8 -*-
from urllib import request
from lxml import etree

'''
urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
print(urls)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
'''


def crow(i):
    #url = 'http://www.zhgc.com/dllt_wq1/arena.asp?qs='+str(i)
    url = 'https://movie.douban.com/top250?start=' + str(i * 25)  # 构造第i页的网址
    html = request.urlopen(url).read().decode('gbk')  # 发送请求，获得返回的html代码并保存在变量html中
    html = etree.HTML(html)
    datas = html.xpath('//table[@id="AutoNumber1"][1]/tr/td[2]')
    print("datas:",datas)
    # a = 0
    # for data in datas:
    #     data_title = data.xpath('.//div[@class="hd"]/a/span/text()')
    #     data_info = data.xpath('.//div[@class="bd"]/p[1]/text()')
    #     data_quote = data.xpath('.//div[@class="bd"]/p[2]/span/text()')
    #     data_score = data.xpath('.//div[@class="bd"]/div/span[@class="rating_num"]/text()')
    #     data_num = data.xpath('.//div[@class="bd"]/div/span[4]/text()')
    #     data_picurl = data.xpath('.//div[@class="pic"]/a/img/@src')
    #     print("No: " + str(i * 25 + a + 1))
    #     print(data_title)
    #
    #     with open('douban250.txt', 'a', encoding='utf-8')as f:
    #         # 封面图片保存路径和文件名
    #         picname = 'E:/Python_code/Pachong/250/' + str(i * 25 + a + 1) + '.jpg'
    #         f.write("No: " + str(i * 25 + a + 1) + '\n')
    #         f.write(data_title[0] + '\n')
    #         f.write(str(data_info[0]).strip() + '\n')
    #         f.write(str(data_info[1]).strip() + '\n')
    #         # 因为发现有几部电影没有quote，所以这里加个判断，以免报错
    #         if data_quote:
    #             f.write(data_quote[0] + '\n')
    #         f.write(data_score[0] + '\n')
    #         f.write(data_num[0] + '\n')
    #         f.write('\n' * 3)
    #         # 下载封面图片到本地，路径为picname
    #         request.urlretrieve(data_picurl[0], filename=picname)
    #     a += 1


for i in range(215,217):
    crow(i)

    '''
    #属性多值匹配 <li class = "li li-first"><a></a></li>
    result = html.xpath('//li[contains(@class, "li")]/a/text()')

    #多属性匹配<li class = "li li-first" name = "item"><a></a></li>
    result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')

    #选取特定位置
    result = html.xpath('//li[1]/a/text()')
    result = html.xpath('//li[last()]/a/text()')
    result = html.xpath('//li[position()<3]/a/text()')
    result = html.xpath('//li[last()-2]/a/text()')
    '''