# -*- coding:utf-8 -*-

__author__ = 'zhennehz'

import os
import xmltodict
from esapi import ElasticObj

dataPath = '/Users/zhennehz/Documents/PycharmPorjects/esdoc/datas/AP_DATA/ap89_collection'
dataPath2 = '/Users/biubiubiu/Desktop/city_temperature.csv'


def start2():
    list = []
    with open(dataPath2, 'rb') as f:  # rb方式最快
        sb = ''
        next(f)
        for line in f:
            li = line.strip()
            lstr = li.decode('gb2312', 'ignore')
            arr = lstr.split(',')
            Region = arr[0]
            Country = arr[1]
            State = arr[2]
            City = arr[3]
            Month = int(arr[4])
            Day = int(arr[5])
            Year = int(arr[6])
            AvgTemperature = float(arr[7])

            obj = {"Region":Region,"Country":Country,"State":State,"City":City,"Month":Month,"Day":Day,"Year":Year,"AvgTemperature":AvgTemperature}
            list.append(obj)
            if len(list) == 1000:
                insertEs(list)
                print(str(len(list)) + ' insert')
                list.clear()

        if len(list)>0:
            insertEs(list)
            print(str(len(list))+' for end insert')
            list.clear()



def start():
    list = os.listdir(dataPath)  # 列出文件夹下所有的目录与文件
    print(list)
    files = []
    filenames = []
    for i in range(0, len(list)):
        path = os.path.join(dataPath, list[i])
        if os.path.isfile(path):
            # 你想对文件的操作
            files.append(path)
            filenames.append(list[i])

    for index, file in enumerate(files):
        fileName = filenames[index]
        getData(file, fileName)


def getData(path,fileName):
    list = []
    with open(path, 'rb') as f:  # rb方式最快
        sb = ''
        for line in f:
            li = line.strip()
            lstr = li.decode('gb2312', 'ignore')
            if lstr.find('<DOC>') > -1:
                sb = sb + lstr
            elif lstr.find('</DOC>') > -1:
                sb = sb + lstr
                # print(sb)
                try:
                    parser_data = xmltodict.parse(sb.replace('&',''))
                    docdata = parser_data['DOC']
                    # json = json.dumps(docdata)  # 将python对象编码成Json字符串
                    # print(docdata)
                    list.append(docdata)
                    if len(list) == 500:
                        insertEs(list)
                        print(str(len(list))+' insert')
                        list.clear()
                except Exception as e:
                    print(sb)
                finally:
                    sb = ''
            else:
                sb = sb + lstr

        if len(list)>0:
            insertEs(list)
            print(str(len(list))+' for end insert')
            list.clear()

    if len(list) > 0:
        insertEs(list)
        print(str(len(list))+' file end insert')
        list.clear()

esobj =ElasticObj("ott2","doc",ip ="127.0.0.1")
def insertEs(list):
    esobj.bulk_Index_Data(list)


if __name__ == '__main__':
    # start()
    start2()