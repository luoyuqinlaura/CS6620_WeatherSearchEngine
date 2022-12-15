# -*- coding:utf-8 -*-

__author__ = 'Yuqin_Luo'

from flask import Flask, request, jsonify
from flask import render_template
from esapi import ElasticObj

app = Flask(__name__)


@app.route('/')  # home page address,“decorator”
def index():
    return render_template('/index.html')

@app.route('/getData', methods=["POST"])
def ocrImg1():
    params = request.form if request.form else request.json

    queryStr = ''
    str1 = ''
    str2 = ''
    str3 = ''
    str4 = ''
    str5 = ''
    str6 = ''
    mustarr=[]

    Region = params.get("Region")
    if Region is not None and len(Region) > 0:
        str1 = { 'match': { 'Region': Region } }
        mustarr.append(str1)

    Country = params.get("Country")
    if Country is not None and len(Country) > 0:
        str2 = { 'match': { 'Country': Country } }
        mustarr.append(str2)

    City = params.get("City")
    if City is not None and len(City) > 0:
        str3 = { 'match': { 'City': City } }
        mustarr.append(str3)

    sdate = params.get("sdate")
    syear = ''
    smonth = ''
    sday = ''
    if sdate is not None and len(sdate)>0:
        sarr = sdate.split('/')
        syear = sarr[2]
        smonth = sarr[0]
        sday = sarr[1]
        str4a = { 'range': { 'Year': { 'gte': syear } } }
        str4b = { 'range': { 'Month': { 'gte': smonth } } }
        str4c = { 'range': { 'Day': { 'gte': sday } } }
        mustarr.append(str4a)
        mustarr.append(str4b)
        mustarr.append(str4c)

    edate = params.get("edate")
    eyear = ''
    emonth = ''
    eday = ''
    if edate is not None and len(edate)>0:
        earr = edate.split('/')
        eyear = earr[2]
        emonth = earr[0]
        eday = earr[1]
        str5a = { 'range': { 'Year': { 'lte': eyear } } }
        str5b = { 'range': { 'Month': { 'lte': emonth } } }
        str5c = { 'range': { 'Day': { 'lte': eday } } }
        mustarr.append(str5a)
        mustarr.append(str5b)
        mustarr.append(str5c)

    AvgTemperature = params.get("AvgTemperature")
    if AvgTemperature is not None and len(AvgTemperature) > 0:
        str6 = { 'match': { 'AvgTemperature': AvgTemperature } }
        mustarr.append(str6)

    print(Region,Country,City,sdate,edate,AvgTemperature)


    if len(mustarr)>0:
        print(mustarr)
        queryStr = { 'bool': { 'must': mustarr } }
    print(queryStr)
    try:
        esobj = ElasticObj("ott2", "doc", ip="127.0.0.1")
        list = esobj.Get_Data_By_Body(queryStr)
        res = {"list": list}
        return jsonify(reason='success', status='200', content=res)
    except Exception as e:
        return jsonify(reason='error', status='500', content=e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)  # 127.0.0.1 return

