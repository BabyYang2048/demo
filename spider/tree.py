import requests
# etree 解析dom
from lxml import etree

url = 'http://www.zhgc.com/bbs/dispbbs.asp?boardID=370&ID=215932&page=1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) C\
                                    hrome/73.0.3683.103 Safari/537.36'}
if __name__ == "__main__":

    ### 发起http请求，返回response
    response = requests.get(url=url, headers=headers)

    ### content属性中包含http请求的信息（这里得到的是html，动态加载的部分可能返回的是json）
    content = response.text

    ### 转换成dom树，可以用xpath定位元素
    dom = etree.HTML(content)

    ### 通过浏览器的开发者工具定位元素位置，构造xpath（推荐使用chrom浏览器）
    ### 获取到电影对应的元素
    li_lists = dom.xpath('.//table[@class="tablebody2"]/tbody/tr/td')
    print('li_lists:',li_lists)

    ### 得到电影的名称
    for li in li_lists:
        ### title是一个list
        title = li.xpath('.//text()')
        # print(title,'\n',''.join(title))
        print(''.join(title))