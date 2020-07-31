import requests
import json
import re

def spider(url):
    head = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",'Accept-Language':'zh-CN,zh;q=0.9'}
    cle = re.compile('cb=(.*)\&pn').findall(url)[0] + '('
    response = requests.get(url, headers=head).text.replace(cle , '').replace(');', '')
    datas = json.loads(response)['data']['diff']
    for data in datas:
        stocks = {
            'id': data['f12'],
            'name': data['f14']
            }
        yield stocks

def getcon(name , url):
    with open('{na}.csv'.format(na = name), 'a',encoding='utf-8-sig') as csvfile:
        csvfile.write("股票名称"+','+ "股票代码"+'\n')


    for i in range(1,500):
        # base_url = 'http://23.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124049817041638364135_1596106183230&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152' % i
        base_url = url % i
        try:
            content = spider(base_url)
            for item in content:
                with open('{na}.csv'.format(na = name), 'a', encoding='utf-8-sig') as csv:
                    if ',' in item['name']:
                        csv.write('"{n}"'.format(n=item['name']) + ',' + '\'' + item['id'] + '\n')
                    else:
                        csv.write(item['name'] + ',' + '\'' + item['id'] + '\n')
        except:
            break

if __name__ == "__main__":
    datas = {
        '沪深A股': 'http://23.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124049817041638364135_1596106183230&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '上证A股': 'http://46.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124009031293000165208_1596118189415&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '深证A股': 'http://86.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407457350380701668_1596119908604&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '新股': 'http://6.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112405397270487597778_1596120238598&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f26&fs=m:0+f:8,m:1+f:8&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152',
        '中小板': 'http://16.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124032509633813730043_1596120354712&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:13&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '创业板': 'http://53.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407779542789491651_1596120420060&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '科创板': 'http://54.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406584470348188203_1596120492374&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '沪股通': 'http://90.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124017097709700319252_1596120582495&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f26&fs=b:BK0707&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152',
        '深股通': 'http://92.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124017042542217652934_1596121808693&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f26&fs=b:BK0804&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152',
        'B股': 'http://82.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124014775357878840412_1596121714863&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:7,m:1+t:3&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '风险警示板': 'http://89.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407620956393095255_1596121286468&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+f:4,m:1+f:4&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '两网及退市': 'http://96.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112404500232249674001_1596121384346&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+s:3&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
        '港股': 'http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407391050611333456_1596160009057&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:128+t:3,m:128+t:4,m:128+t:1,m:128+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
        '新三板': 'http://78.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112402802227936487409_1596167887037&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:!4&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111',
        '美股': 'http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406935829251486172_1596168135425&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:105,m:106,m:107&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
        '英股': 'http://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406633179673400491_1596168313222&pn=%d&pz=20&po=1&fid=f3&np=1&ut=fa5fd1943c7b386f172d6893dbfba10b&fs=m:155+t:1,m:155+t:2,m:155+t:3,m:156+t:1,m:156+t:2,m:156+t:5,m:156+t:6,m:156+t:7,m:156+t:8&fields=f1,f14,f2,f4,f3,f17,f15,f16,f18,f20,f115,f13,f12,f152',
        '港股通（沪）':'http://84.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124014471498016782736_1596170655702&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0144&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152',
        '港股通（深）':'http://1.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124005714876874933683_1596170805551&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0146&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152'
        }

    for data in datas:
        getcon(data , datas[data])
        print(data + ' ' + '抓取完成')