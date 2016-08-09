#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
破解维吉尼亚密码
"""


def getWords():
    """
    时间复杂度：O(3599)
    """
    filename = "common_English_Word_Dictionary.txt"
    with open(filename, "r") as f:
        data = f.read()
        data = data.upper()
        data = data.split("\n")
        data = set(data)

    return data


def countWords(words, string, string_length):
    """
    时间复杂度：O(3599 * O(findSubStr))
    """
    count_words = 0
    for each in words:
        each_length = len(each)
        if each_length < 2:
            continue
        count_words += findSubStr(each, each_length, string, string_length)

    return count_words


def findSubStr(subString, each_length, fullString, length):
    counts = 0
    result = fullString.find(subString)
    while result != -1:
        counts += 1
        fullString = fullString[result + each_length:]
        result = fullString.find(subString)
    return counts


"""
def findSubStr(subString, each_length, fullString, length):
    counts = 0
    subLength = each_length
    for i in range(length - subLength):
        if fullString[i:i+subLength] == subString:
            counts += 1
    return counts
"""


def createMi_yao(order):
    character = "abcdefghijklmnopqrstuvwxyz".upper()
    mi_yao = ""
    while True:
        mi_yao += character[order % 26]
        order = order // 26
        if order == 0:
            break

    mi_yao = mi_yao[::-1]
    return mi_yao


def create_dict(keys, values):
    temp = zip(keys, values)
    dictionary = dict((key, value) for key, value in temp)
    return dictionary


def formula_two(dictionary, reverse_dictionary, string, miyao):
    count_miyao = 0
    ming_wen = ""
    for each in string:
        if each.isalpha() == False:
            if each != '\n':
                count_miyao += 1
            ming_wen += each
            continue
        miyao_num = dictionary[miyao[count_miyao % len(miyao)]]
        position = (26 - miyao_num + \
                    dictionary[each]) % 26 + 1
        count_miyao += 1
        ming_wen += reverse_dictionary[position]

    return ming_wen


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \
              12, 13, 14, 15, 16, 17, 18, 19, 20, \
              21, 22, 23, 24, 25, 26]
    keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dictionary = create_dict(keys, values)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    words = getWords()

    miwen = """\
EB BMQF KYJRD, IM ICHZZZ YWELXABD, ICCH PVLQ EB PGJS, UEZW PAGE RDS IGJOW QQQNHQO ZU BOTOSNS RD CFU YCFUQA. VGJQP RDWD AKIYWPU HDQ TZXLZSO, AONK CSYHPWHTRL CQ YISCLAWBD FWG ECAB VSIAZQCZ ER CWGH PSDWGICYB PC LRO YDRECYDJ ZZBYHHJ. PVP ENOGHQ CQ WKIYJ WAPUGYOYV SVZ YJGHHPAR WFA NDJH ER OSCYGYS VSNFZXLZ EKC UWRZA.

YRU HSH PFFPNAH VSIAZQQ ID YCOTQ - YRR OD Y QLOJ HZ ZAOC YNAD, PVZXED LUKO HH JSPG; BZW WG D YOWO PC EYPHWH, HSRSCV HKXOEWJAR ZC OCH - MXR O FYHZ WM PPDP HSH XICGCJ ZI W WRLC EZGHWRKR GEUSCUWH, MPDP WY YJR BCWF RSP, "PAXZLAEBR GJ SRNA, SYPWPQR WY RNWMXJWHTRL" - Y GEUSCUWH WULLLOH WFA NRKICY CJSXLCO ZI IOY: PMCDLJM, NKJPURU, GGOSLVC, LQB KLU EHDHJB.

NDL KP DKFRH WULLLOH WFAGP CJSXLCO L ENOYG WBO EHCMDJ OWOGWBNH, BZURD LQB GZXRD, HYOH DLZ HHQP, WFWH FYJ LVQQFP Y AZUC TCXGPTFO HWQH BCC YHZ PYJYTQB? HLJH JRS XZLL WY RDOE FEGERPEQ HDBCCW?

EB WFA WRLC SLQPCCB KT WFA HRPHR, MJZJ Y TPZ CSYHPWHTRLO SDTA MHCJ RUYJHPG PVP PKZP MB OHDABOLLC QUCARZP EB LRO SRSN ZI IOILKQA GYJUPU. W GM BZW OVLQI TCRK HSLQ FPVNKBDLZEZTWW - L SSWFMIS LR. T BK YRR PPOGAJP RDOE YJM RD ID UKIWG ALNKYJUP NHONHQ KTWF OYB KHSHP DPRNHS RP OYB KHSHP UPQCNOELMJ. WFA PQCNUJ, PVP DWWEK, HSH ZSGRRECY UDWNK SS EPEBR RK EKGO PQBAOGRSN HLJH WLEDH RSN NRSJHCB WBO YHZ ZFK DHPRS LR -- YJR WFA ROMS QUMI EKYP QLPA NDL HCXJU WLEDH WFA HRPHR.

DLZ DR, AJ DAZWRU OXHPEQLQQ: LVI BZW SVLW UCFU YCFQRNM FYJ OR BCC WKI - WGV UDOE WKI FYJ OR BCC WKIC AKIYWPU.

XB BSWOMS NLRENPQQ CQ RDS ZMNZO: WGV LKH ZFWH DKAFTFY KTOJ RZ DKF BMQ, ESP HKYP EREAHSHP KP AWB GM TZU PVP DNSPGMI ZI IOY.

DEBLOJU, ZFAHSHP MZX WFP AEHTCCJG RD OXHPEQL MN NLRENPQQ CQ RDS ZMNZO, WGV MB FV PVP QWAP FEUS QPOYGYNRD MB DWPABRWF OYG OONUGBWNH SVTFF KP YOY RD MZX. KTWF O JMKR FMJGNLCJQP MQF RLHM VSNS UCSOCG, KTWF VTVRKFJ RDS IGJOW HQRRH KT RSN OHCZG, JAH XQ UZ DKFEK PC OCWR WFA WDLZ HH HCGH, ODNGJU KGO MOCOGTQE OYG DWD FAZA, XIE IJCHLLC EKYP SHPA ZQ AOCWF UZG'O HRPG XXQP EUSHM EC CFU KKY.
"""
    miwen1 = miwen.split("\n")[0]
    string_length = len(miwen)
    for i in range(0, 26 ** 5):
        mi_yao = createMi_yao(i)
        #        mi_yao = "WOLDY"
        print("string working....i = %d mi_yao = %s" % (i, mi_yao))
        ming_wen = formula_two(dictionary, reverse_dictionary, miwen1, mi_yao)
        count_words = countWords(words, ming_wen, string_length)
        if count_words > 40:
            filename = "result.txt"
            with open(filename, "w+") as f:
                ming_wen = formula_two(dictionary, \
                                       reverse_dictionary, miwen, mi_yao)
                print(ming_wen)
                f.write("mi_yao = " + mi_yao + "\n")
                f.write(ming_wen)

    input("输入任意键结束")
