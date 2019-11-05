import math


def __delete_line__(file_in,file_out):
    """
    按行读取去空行
    :param file_in:
    :param file_out:
    :return:
    """
    f1 = open(file_in, 'r', encoding='utf-8')
    f2 = open(file_out, 'a', encoding='utf-8')
    try:
        for line in f1.readlines():
            if line=="\n":
                line = line.strip("\n")
            f2.write(line)
    finally:
        f1.close()
        f2.close()


def __delete_space__(file_in, file_out):
    """
    按行读取去空格
    :param file_in:
    :param file_out:
    :return:
    """
    with open(file_in,"r",encoding="utf-8") as f:
        for line in f:
            str = ""
            for char in line:
                if char.isspace() :
                    continue
                str += char
            print(str)
            with open(file_out, 'a', encoding='utf-8') as file_obj:
                file_obj.write(str+'\n')


def __add_space__(file_in,file_out):
    """
    按行读取增加空格
    :param file_in:
    :param file_out:
    :return:
    """
    with open(file_in,"r",encoding="utf-8") as f:
        for line in f:
            line = " ".join(line)
            #print(line)
            with open(file_out, 'a', encoding='utf-8') as file_obj:
                file_obj.write(line)


def __pair2line__(file_in_1, file_in_2, file_out):
    """
    讲分开的对联合并在一起
    :param file_in_1:
    :param file_in_2:
    :param file_out:
    :return:
    """
    f1 = open(file_in_1, 'r', encoding='utf-8')
    f2 = open(file_in_2, 'r', encoding='utf-8')
    try:
        for line1,line2 in zip(f1.readlines(),f2.readlines()):
            with open(file_out,'a',encoding='utf-8') as f:
                f.write(line1)
                f.write(line2)
    finally:
        f1.close()
        f2.close()
        f.close()


def __line2pair__(file_in,file_out_1,file_out_2,symbol):
    """
    将quchong后的上下联拆开到各自的文件中
    :param file_in: "../data/result.txt"
    :param file_out_1: "../data/first.txt"
    :param file_out_2: "../data/second.txt"
    :param symbol 以symbol拆分
    :return:
    """
    with open(file_in, 'r', encoding='utf-8') as f:
        for line in f:
            # line.strip("\n")
            list = line.split(symbol)
            print(list[0])
            print(list[1])
            with open(file_out_1, 'a', encoding='utf-8') as file_obj:
                file_obj.write(list[0] + '\n')
            with open(file_out_2, 'a', encoding='utf-8') as file_obj:
                file_obj.write(list[1])


def __check_zishu__(file_in_1,file_in_2,file_out_1,file_out_2):
    """
    将上下联整合作对比，如果上下联字数不一样，则删去这一副对联
    :param file_in_1:  "../data/first.txt"
    :param file_in_2:  "../data/second.txt"
    :param file_out_1: "../data/first_new.txt"
    :param file_out_2: "../data/second_new.txt"
    :return:
    """
    with open(file_in_1, 'r', encoding='utf-8') as f1:
        with open(file_in_2, 'r', encoding='utf-8') as f2:
            for line1,line2 in zip(f1,f2):
                if( len(line1) == len(line2)):
                    print(line1+line2)
                    with open(file_out_1, 'a', encoding='utf-8') as file_obj:
                        file_obj.write(line1)
                    with open(file_out_2, 'a', encoding='utf-8') as file_obj:
                        file_obj.write(line2)


def __binghang__(file_in, file_out, symbol):
    """
    将上下联合并到一行的操作
    :param file_in:  "../data/others.txt"
    :param file_out: "../data/re1.txt"
    :param symbol: 拼起来的两句按照什么分隔符拼接
    :return:
    """
    try:
        lines = open(file_in, encoding="UTF-8").read()
        fp = open(file_out, "w", encoding="UTF-8")
        liness = lines.split("\n")
        #print(liness)
        # for i in range(0,len(liness)):
        #        fp.write(liness[i].replace("\u3000\u3000",""))
        for i in range(0, len(liness), 2):
            # print(liness[i] + " " + liness[i + 1])
            fp.write(liness[i] + symbol + liness[i + 1] + "\n")
    except IndexError:
        print("Error:",IndexError)
    finally:
        fp.close()


def is_number(s):
    """
    判断一个字符串是否是数字,还可以判断汉字哟
    :param s:
    :return:
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError, ValueError):
    #     pass

    return False


def __spilt_byotherchar__(file_in,file_out):
    """
    去掉文本中出文字以外的信息(目前使用穷举)
    :param file_in: "../data/second_old.txt"
    :param file_out: "../data/second.txt"
    :return:
    """
    with open(file_in, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            i = i + 1
            # print("i="+str(i)+line)
            linea = ""
            for char in line:
                if char == "：" or char == ":" \
                        or char == "/" \
                        or char == "*" \
                        or is_number(char) \
                        or char == "（" or char == ")" \
                        or char == "(" or char == "）" \
                        or char == " " \
                        or char == "!" or char == "！" \
                        or char == "~" \
                        or char == "？" or char == "?" \
                        or char == "“" or char == "\"" \
                        or char == "”" \
                        or char == "。" \
                        or char == "《" or char == "》" \
                        or char == "，" \
                        or char == "、" \
                        or char == "-":
                    continue
                linea += char
            # print("i="+str(i)+linea)
            with open(file_out, 'a', encoding='utf-8') as file_obj:
                file_obj.write(linea)


def __quchong1__(file_in,file_out):
    """
    按行去重 ，在binghang之后使用
    :param file_in: "../data/re1.txt"
    :param file_out:  "../data/result.txt"
    :return:
    """
    outfile = open(file_out, "w", encoding="UTF-8")
    f = open(file_in, "r", encoding="UTF-8")

    lines_seen = set()  # Build an unordered collection of unique elements.

    for line in f:
        line = line.strip('\n')
        if line not in lines_seen:
            outfile.write(line + '\n')
            lines_seen.add(line)
        else:
            print(line)
    outfile.close()
    f.close()


def __quchong2__(file_in_1,file_in_2,file_out_1,file_out_2):
    """
    对联的上下联都不允许重复
    :param file_in_1:
    :param file_in_2:
    :param file_out_1:
    :param file_out_2:
    :return:
    """
    f1 = open(file_in_1, 'r', encoding='utf-8')
    f2 = open(file_in_2, 'r', encoding='utf-8')
    lines_seen = set()

    try:
        for line1, line2 in zip(f1.readlines(), f2.readlines()):
            if line1 not in lines_seen and len(line1)>2:
                with open(file_out_1,'a',encoding='utf-8') as f_obj:
                    f_obj.write(line1)
                with open(file_out_2, 'a', encoding='utf-8') as f_obj:
                    f_obj.write(line2)
                lines_seen.add(line1)
            else:
                print("line1=", line1)
                print("line2=", line2)
                continue

    finally:
        f1.close()
        f2.close()


def __castdown__(file_in, file_out, start, end):
    """
    截断文件的部分行
    :param file_in:
    :param file_out:
    :param start: 起始行
    :param end: 结束行
    :return:
    """
    with open(file_in,'r',encoding='utf-8') as f:
        for ii, line in enumerate(f):
            if ii < start :
                continue
            else:
                if ii == end:
                    break
                with open(file_out,'a',encoding='utf-8') as f_obj:
                    f_obj.write(line)


def __pingjie__(file_in, file_out):
    """
    将两个文件拼在一起
    :param file_in:
    :param file_out:
    :return:
    """
    try:
        with open(file_in,'r',encoding='utf-8') as f:
            for line in f:
                with open(file_out,'a',encoding='utf-8') as f_obj:
                    f_obj.write(line)
    finally:
        f.close()
        f_obj.close()


def __test__(file_in_1, file_in_2, file_out):
    """
    把无情对和对联拼起来
    :param file_in_1: 对联
    :param file_in_2: 无情对
    :param file_out:  结果文件
    :return:
    """
    f1 = open(file_in_1, 'r', encoding='utf-8')
    f2 = open(file_in_2, 'r', encoding='utf-8')
    try:
        for line in f1.readlines():
            line.strip('\n')
            with open(file_out, 'a', encoding='utf-8') as f:
                f.write(line + "||" + "0" + "\n")
        for line2 in f2.readlines():
            line2.strip("\n")
            with open(file_out, 'a', encoding='utf-8') as f:
                f.write(line2 + "||" + "1" + "\n")
    finally:
        f1.close()
        f2.close()
        f.close()


def __count__(file_in):
    try:
        word2count = {}
        with open(file_in,'r',encoding='utf-8') as f:
            for line in f:
                num = len(line.strip('\n'))
                if num not in word2count.keys():
                    word2count[num] = 1
                    # print(num,word2count[num])
                else:
                    word2count[num] = word2count[num] + 1
        # print(word2count)
        sort_word2count = sorted(word2count)
        for c in sort_word2count:
            print(c,'字联',word2count[c],'条')
        z = zip(word2count.values(), word2count.keys())
        a = sorted(z)
        print(a)
        # for c in sort_word2count:
        #     print(c,'字联',word2count[c],'条')
    finally:
        f.close()




if __name__ == '__main__':
    print("start..")
    file_in = "../data/d_duilian_first.txt"
    file_out= "../data/duilian_first.txt"
    file_in_1 = "../data/.txt"
    file_in_2 = "../data/.txt"
    file_out_1 = "../data/d_wuqing_first.txt"
    file_out_2 = "../data/d_wuqing_second.txt"
    # start = 569782-226
    # end = 569782
    # __castdown__(file_in,file_out,start,end)
    # __spilt_byotherchar__(file_in,file_out)
    # __line2pair__(file_in,file_out_1,file_out_2,"||")
    # __quchong2__(file_in_1,file_in_2,file_out_1,file_out_2)
    # __pair2line__(file_in_1,file_in_2,file_out)
    # __binghang__(file_in,file_out,symbol="||")
    # __test__(file_in_1,file_in_2,file_out)
    # __binghang__(file_in, file_out, symbol="")
    # __line2pair__(file_in,file_out_1,file_out_2,symbol="||")
    # __add_space__(file_in,file_out)
    # __count__(file_in)
    print("end...")

