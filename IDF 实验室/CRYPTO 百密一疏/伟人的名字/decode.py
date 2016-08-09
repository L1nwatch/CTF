#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
破解维吉尼亚密码
"""
def create_dict(keys,values):
    temp = zip(keys, values)
    dictionary = dict((key, value) for key, value in temp)
    return dictionary

def formula_one(dictionary, string, miyao):
    pass

#    for each in string:
#    print((dictionary[string] + dictionary[miyao]) % 26 - 1)
#        continue

def formula_two(dictionary, string, miyao):
    string = string.upper()
    miyao = miyao.upper()
    reverse_dict = dict(zip(dictionary.values(), dictionary.keys()))
    count_miyao = 0

    for each in string:
        if each.isalpha() == False:
            if each != '\n':
                count_miyao += 1
            print(each, end = "")
#            print("\t %d \t", ord(each))
            continue
        miyao_num = dictionary[miyao[count_miyao % len(miyao)]]
        position = (26 - miyao_num + \
                    dictionary[each]) % 26 + 1
        count_miyao += 1
        print(reverse_dict[position], end = "")

    return None

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \
              12, 13, 14, 15, 16, 17, 18, 19, 20, \
              21, 22, 23, 24, 25, 26]
    keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dictionary = create_dict(keys, values)

    miwen = """\
EB BMQF KYJRD, IM ICHZZZ YWELXABD, ICCH PVLQ EB PGJS, UEZW PAGE RDS IGJOW QQQNHQO ZU BOTOSNS RD CFU YCFUQA. VGJQP RDWD AKIYWPU HDQ TZXLZSO, AONK CSYHPWHTRL CQ YISCLAWBD FWG ECAB VSIAZQCZ ER CWGH PSDWGICYB PC LRO YDRECYDJ ZZBYHHJ. PVP ENOGHQ CQ WKIYJ WAPUGYOYV SVZ YJGHHPAR WFA NDJH ER OSCYGYS VSNFZXLZ EKC UWRZA.

YRU HSH PFFPNAH VSIAZQQ ID YCOTQ - YRR OD Y QLOJ HZ ZAOC YNAD, PVZXED LUKO HH JSPG; BZW WG D YOWO PC EYPHWH, HSRSCV HKXOEWJAR ZC OCH - MXR O FYHZ WM PPDP HSH XICGCJ ZI W WRLC EZGHWRKR GEUSCUWH, MPDP WY YJR BCWF RSP, "PAXZLAEBR GJ SRNA, SYPWPQR WY RNWMXJWHTRL" - Y GEUSCUWH WULLLOH WFA NRKICY CJSXLCO ZI IOY: PMCDLJM, NKJPURU, GGOSLVC, LQB KLU EHDHJB.

NDL KP DKFRH WULLLOH WFAGP CJSXLCO L ENOYG WBO EHCMDJ OWOGWBNH, BZURD LQB GZXRD, HYOH DLZ HHQP, WFWH FYJ LVQQFP Y AZUC TCXGPTFO HWQH BCC YHZ PYJYTQB? HLJH JRS XZLL WY RDOE FEGERPEQ HDBCCW?

EB WFA WRLC SLQPCCB KT WFA HRPHR, MJZJ Y TPZ CSYHPWHTRLO SDTA MHCJ RUYJHPG PVP PKZP MB OHDABOLLC QUCARZP EB LRO SRSN ZI IOILKQA GYJUPU. W GM BZW OVLQI TCRK HSLQ FPVNKBDLZEZTWW - L SSWFMIS LR. T BK YRR PPOGAJP RDOE YJM RD ID UKIWG ALNKYJUP NHONHQ KTWF OYB KHSHP DPRNHS RP OYB KHSHP UPQCNOELMJ. WFA PQCNUJ, PVP DWWEK, HSH ZSGRRECY UDWNK SS EPEBR RK EKGO PQBAOGRSN HLJH WLEDH RSN NRSJHCB WBO YHZ ZFK DHPRS LR -- YJR WFA ROMS QUMI EKYP QLPA NDL HCXJU WLEDH WFA HRPHR.

DLZ DR, AJ DAZWRU OXHPEQLQQ: LVI BZW SVLW UCFU YCFQRNM FYJ OR BCC WKI - WGV UDOE WKI FYJ OR BCC WKIC AKIYWPU.

XB BSWOMS NLRENPQQ CQ RDS ZMNZO: WGV LKH ZFWH DKAFTFY KTOJ RZ DKF BMQ, ESP HKYP EREAHSHP KP AWB GM TZU PVP DNSPGMI ZI IOY.

DEBLOJU, ZFAHSHP MZX WFP AEHTCCJG RD OXHPEQL MN NLRENPQQ CQ RDS ZMNZO, WGV MB FV PVP QWAP FEUS QPOYGYNRD MB DWPABRWF OYG OONUGBWNH SVTFF KP YOY RD MZX. KTWF O JMKR FMJGNLCJQP MQF RLHM VSNS UCSOCG, KTWF VTVRKFJ RDS IGJOW HQRRH KT RSN OHCZG, JAH XQ UZ DKFEK PC OCWR WFA WDLZ HH HCGH, ODNGJU KGO MOCOGTQE OYG DWD FAZA, XIE IJCHLLC EKYP SHPA ZQ AOCWF UZG'O HRPG XXQP EUSHM EC CFU KKY.
"""
    formula_two(dictionary, miwen, "woldy")

def test_one():
    pass
#    string = "B H Q V O M G L W L P P H C I V O M G H".split(" ")
#    formula_one(dictionary, string, "THE")
#    formula_two(dictionary, string, "THE")

def test_two():
    pass
"""
    miyao = "RELAT IONSR ELATI ONSRE LATIO NSREL".replace(" ", "")  #删除空格
    miwen = "KSMEH ZBBLK SMEMP OGAJX SEJCS FLZSY"
    formula_two(dictionary, miwen, miyao)
"""

"""
密钥THE
明文B H Q V O M G L W L P P H C I V O M G H
提示一下，这是用公式一加密的，所以只要用公式二来破解就行了。
答案是 I am Chiness ,I love China
"""

"""
密钥:RELAT IONSR ELATI ONSRE LATIO NSREL
明文:TOBEO RNOTT OBETH ATIST HEQUE STION
密文:KSMEH ZBBLK SMEMP OGAJX SEJCS FLZSY
"""