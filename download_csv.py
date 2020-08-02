import requests
import os
import time

class BaseInfo:
    def __init__(self):
        self.id_list = []
        self.name_list = []

    def parse_txt(self , path):
        with open('{pa}'.format(pa = path), 'r', encoding='utf-8') as f:
            data_list = f.readlines()
            for data in data_list:
                baselist = data.split(',')
                self.id_list.append(baselist[1])
                self.name_list.append(baselist[3].replace('\n', ''))

class download:
    def __init__(self , stock_name , stock_id):
        self.name = stock_name
        self.id =stock_id

    def spider(self):
        head = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",'Accept-Language':'zh-CN,zh;q=0.9'}

        base_url_list = {
            'zycwzb': 'http://quotes.money.163.com/service/zycwzb_%s.html?type=report',
            'ylnl': 'http://quotes.money.163.com/service/zycwzb_%s.html?type=report&part=ylnl',
            'chnl': 'http://quotes.money.163.com/service/zycwzb_%s.html?type=report&part=chnl',
            'cznl': 'http://quotes.money.163.com/service/zycwzb_%s.html?type=report&part=cznl',
            'yynl': 'http://quotes.money.163.com/service/zycwzb_%s.html?type=report&part=yynl',
            'cwbbzy': 'http://quotes.money.163.com/service/cwbbzy_%s.html',
            'zcfzb': 'http://quotes.money.163.com/service/zcfzb_%s.html',
            'lrb': 'http://quotes.money.163.com/service/lrb_%s.html',
            'xjllb': 'http://quotes.money.163.com/service/xjllb_%s.html'
            }
        try:

            for url in base_url_list:
                base_url = base_url_list[url] % self.id
                response = requests.get(base_url, headers=head)
                path = 'C:/Users/yewei/Desktop/stock/%s'% self.id
                if not os.path.exists(path):
                    os.makedirs(path)
                    print(self.id + '文件夹创建成功')
                else:
                    print(self.id + '文件夹已存在')
                f = open("{pa}/{na}.csv".format(pa = path , na = self.id + '-' + url) , "wb")
                f.write(response.content)
                f.close

                print(self.name + '-' + url + ' ' + "下载完成")
                response.close()

        except:
            time.sleep(10)
            self.spider()


if __name__ == "__main__":
    # download("N江航" , 688586).spider()
    baseinfo = BaseInfo()
    baseinfo.parse_txt('C:\\Users\\yewei\\Desktop\\all_stock.txt')
    for i in range(3427 ,len(baseinfo.id_list)):
        print(i , '/' , len(baseinfo.id_list))
        download(baseinfo.name_list[i] , baseinfo.id_list[i]).spider()
        time.sleep(2)
    # download("*ST金洲", '000587').spider()

