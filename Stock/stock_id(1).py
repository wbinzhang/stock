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
            'id': data['f201'],
            'name': data['f203']
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
        '上证AB股比价': 'http://73.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112409974387917013923_1596121444951&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f199&fs=m:1+b:BK0498&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f201,f202,f203,f196,f197,f199,f195,f200',
        '深证AB股比价': 'http://83.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112401260218555308643_1596121593880&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f199&fs=m:0+b:BK0498&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f201,f202,f203,f196,f197,f199,f195,f200',
        }

    for data in datas:
        getcon(data , datas[data])
        print(data + ' ' + '抓取完成')