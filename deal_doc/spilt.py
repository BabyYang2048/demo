# import re
#
# list_result = []
#
#
# def spilt():
#     file_name = 'write.txt'
#     pattern = '[第].*?([擂]|[期])'
#     list_middle = []
#     with open(file_name, 'r',encoding='utf-8') as f:
#         for line in f:
#             # print(line, end='')
#             if re.match(pattern,line) :
#                 list_middle=[]
#                 list_middle.append(line)
#             elif re.match('-------------',line):
#                 if re.match(pattern,list_middle[0]):
#                     list_middle.append(line)
#                     list_result.append(list_middle)
#                     list_middle = []
#                 else:
#                     list_middle = []
#             else :
#                 list_middle.append(line)
#     # print(list_result)
#
#
# def check():
#     file_name_1 = "shanglian"
#     file_name_2 = "xialian"
#     pattern_a = '擂句.*?'
#     pattern_b = '出句.*?'
#
#     if len(list_result):
#         print('ok')
#         for list_b in list_result:
#             # print('list:',list_b,'\n')
#             if re.match('.*?(守擂成功)',list_b[0]):
#                 # print(list_b)
#                 pattern2 = '守擂.*?'
#             else:
#                 pattern2 = '胜句.*?'
#                 pattern2_b = '胜出句.*?'
#             for str in list_b:
#                 if re.match(pattern_a, str) or re.match(pattern_b,str):
#                     print('?', str)
#                     with open(file_name_1, 'a' , encoding='utf-8') as file_obj:
#                         file_obj.write(str)
#
#                 if re.match(pattern2, str) or re.match(pattern2_b,str):
#                     print('!', str)
#                     with open(file_name_2, 'a', encoding='utf-8') as file_obj:
#                         file_obj.write(str)
#                 # else:
#                 #     if re.match():
#
#             print('------------')
#
#     else:
#         print('nulllllllll')
#
#
#
#
# if __name__ == '__main__':
#     print('+++++++++++++++++++++++++++++++++++++++++++++')
#     spilt()
#     check()

file_name_1 = "上联"
file_name_2 = "下联"
file_name = "all"

list_1 = []
list_2 = []
with open(file_name_1, 'r', encoding='utf-8') as f1:
    for line in f1:
        list_1.append(line)


with open(file_name_2, 'r', encoding='utf-8') as f2:
    for line in f2:
        list_2.append(line)

list_all = []
l_str1=''
l_str2=''
for i in range(0,len(list_1)):
    # if "(" in list_1[i]:
    #     list_line1 = list_1[i].split('(')
    #     print(list_line1[0])
    #     l_str1 = list_line1[0].strip()
    # if "(" in list_2[i]:
    #     list_line2 = list_2[i].split('(')
    #     print(list_line2[0])
    #     l_str2 = list_line2[0].strip()
    l2 = list_2[i].strip()
    l1 = list_1[i].strip()
    string = l2 + "\n" + l1
    list_all.append(string)
    list_line1=[]
    list_line2=[]

for line in list_all:
    with open(file_name, 'a', encoding='utf-8') as file_obj:
        file_obj.write(line+"\n")
    print(line)



# with open('all', 'r', encoding='utf-8') as fr, open('out.txt', 'w', encoding='utf-8') as fd:
#     for text in fr.readlines():
#         if text.split():
#             fd.write(text)
#     print('输出成功....')