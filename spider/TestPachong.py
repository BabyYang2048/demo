from selenium import webdriver

file_name = 'write5.txt'
pattern1 = "([第].*?[擂])"


#if re.search(r"[第].*?[擂]",d.text):
def crow(i):
    # driver = webdriver.PhantomJS()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)


    # url们
    # url = "http://www.zhgc.com/bbs/list.asp?boardid=370&page="+str(i)+"&selTimeLimit=&action=&topicmode=0"
    # 无情对擂台 - 出句区 write5.txt
    #url = "http://www.zhgc.com/dllt_wq/arena.asp?x=cj"
    # 无情对擂台 - 撞句区 write4.txt
    #url = "http://www.zhgc.com/dllt_wq/arena.asp?x=qz"
    # 无情对擂台 - 对句区 write3.txt
    #url = "http://www.zhgc.com/dllt_wq/arena.asp"
    # 无情对擂赛区2（对句半月赛）
    # url = "http://www.zhgc.com/dllt_wq2/arena.asp?qs=" + str(i)
    #无情对擂赛区1（对句半月赛）
    #url = "http://www.zhgc.com/dllt_wq1/arena.asp?qs="+str(i)
    # 贴子主题：[分享] 无情版擂台赛2优秀联集锦 write2.txt
    #url = "http://www.zhgc.com/bbs/dispbbs.asp?boardid=370&star="+str(i)+"&replyid=790427&id=321909&skin=0&page=1"
    # 贴子主题：[分享] 无情版擂台赛1优胜、优秀句集 write.txt
    url = "http://www.zhgc.com/bbs/dispbbs.asp?boardid=370&star="+str(i)+"&replyid=198823&id=215932&skin=0&page=1"

    driver.get(url)
    print(driver.current_url)
    #data = driver.find_elements_by_class_name('tablebody2')
    # data = driver.find_elements_by_id('AutoNumber1')
    # //table[@id="AutoNumber1"]/tbody/tr/td[2]
    data = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td[2]/table[@id="AutoNumber1"]/tbody/tr/td[2]')
    #data = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td[2]/table[5]/tbody/tr/td[2]')
    #data = driver.find_elements_by_xpath('/html/body/table[9]/tbody/tr/td[2]/a')
    print("url",url)
    for d in data:
        print(d.text)
        with open(file_name, 'a' , encoding='utf-8') as file_obj:
            file_obj.write(d.text+'\n')


for i in range(76,77):
    crow(i)