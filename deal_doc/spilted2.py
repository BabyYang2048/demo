import re

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

list_result=[]
def spilt():
    file_name = '../data/write6.txt'
    pattern = '本期出句、对句'
    list_middle = []
    with open(file_name, 'r',encoding='utf-8') as f:
        for line in f:
            if re.match(pattern,line):
                list_result.append(list_middle)
                list_middle=[]
                list_middle.append(line)
                # print(line, end='')
            else :
                list_middle.append(line)
                # print(line, end='')

    # print(list_result)


def check():
    file_name_1 = "../data/first1.txt"
    file_name_2 = "../data/second1.txt"
    file_name_3 = "../data/others.txt"

    if len(list_result):
        print('ok')
        for list_m in list_result:
            print("listtt：",list_m,'\n')
            if len(list_m):
                print(len(list_m))
                print("上联：", list_m[1])
                # with open(file_name_1, 'a', encoding='utf-8') as file_obj:
                #     file_obj.write(list_m[1])
                print("下联：", list_m[2])
                # with open(file_name_2, 'a', encoding='utf-8') as file_obj:
                #     file_obj.write(list_m[2])
                for i in range(3,len(list_m)):
                    # with open(file_name_1, 'a', encoding='utf-8') as file_obj:
                    #     file_obj.write(list_m[1])
                    # with open(file_name_2, 'a', encoding='utf-8') as file_obj:
                    #     file_obj.write(list_m[i])
                    with open(file_name_3, 'a', encoding='utf-8') as file_obj:
                        file_obj.write(list_m[i])
                        file_obj.write(list_m[1])
                    print("其他：",list_m[i])
            else:
                print("这个集合是空的")
    else:
        print('nulllllllll')




if __name__ == '__main__':
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    spilt()
    check()
