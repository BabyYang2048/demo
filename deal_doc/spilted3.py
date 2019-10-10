list_result = []

file_name_1 = '上联'
file_name_2 = '下联'


def spilt():
    file_name = 'write2_1.txt'
    # pattern = '作品'
    list_middle = []
    with open(file_name, 'r',encoding='utf-8') as f:
        for line in f:
            list_result.append(line)

    for i in range(0,len(list_result)):
        if i % 3 == 0:
            print("下联：", "i=", i, "list=", list_result[i])
            with open(file_name_1, 'a', encoding='utf-8') as file_obj:
                file_obj.write(list_result[i])

        elif i % 3 == 1:
            print("下联：", "i=", i, "list=", list_result[i])
            with open(file_name_2, 'a', encoding='utf-8') as file_obj:
                file_obj.write(list_result[i])
        else:
            print("这是空行")
    # print(list_result)


def check():
    file_name_1 = "上联"
    file_name_2 = "下联"
    file_name_3 = "其他"

    list_re = []
    if len(list_result):
        print('ok')
        for list_m in list_result:
            # print("listtt：",list_m,'\n')
            if len(list_m):
                #print(len(list_m))
                for i in range(1,len(list_m)):
                    # print("i=",i,"list=",list_m[i])
                    if i % 3 == 1:
                        print("上联：","i=",i,"list=",list_m[i])
                        shanglian = list_m[i]
                        list_re.append(shanglian)
                        # with open(file_name_1, 'a', encoding='utf-8') as file_obj:
                        #     file_obj.write(list_m[i])
                    elif i % 3 == 2:
                        print("下联：","i=",i,"list=",list_m[i])
                        xialian = list_m[i]
                        list_re.append(xialian)
                    else:
                        print("这是空行")
                    if len(list_re) == 2:
                        # print("上联：", shanglian)
                        # print("下联：", xialian)
                        print(len(list_re))
                        if len(list_re[0]) and len(list_re[1]) :
                            print("上联：", list_re[0])
                            print("下联：", list_re[1])
                            # with open(file_name_1, 'a', encoding='utf-8') as file_obj:
                            #     file_obj.write(list_re[0])
                            # with open(file_name_2, 'a', encoding='utf-8') as file_obj:
                            #     file_obj.write(list_re[1])
                            list_re = []
            else:
                print("这个集合是空的")
    else:
        print('nulllllllll')




if __name__ == '__main__':
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    spilt()
    # check()
