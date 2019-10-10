from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

#driver.get("http://www.zhgc.com/dllt_wq1/arena.asp")
driver.get("http://www.zhgc.com/dllt_wq2/arena.asp")
file_name = 'write7.txt'

#for i in range(75,217):
for i in range(13,70):
    print("Page No.", i)
    btn = driver.find_element_by_partial_link_text(str(i))
    btn.click()
    data = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td[2]/table[@id="AutoNumber1"]/tbody/tr/td[2]')
    for d in data:
        print(d.text)
        with open(file_name, 'a' , encoding='utf-8') as file_obj:
            file_obj.write(d.text+'\n')

