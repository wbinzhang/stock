import pandas as pd
import glob

def merge(address):
    data_list = glob.glob('{}/*.csv'.format(address))
    print(u'共发现%s个CSV文件'% len(data_list))
    for data in data_list:
        fr = open(data,'rb').read()
        with open('{}/Stock.csv'.format(address),'ab') as f:
            f.write(fr)
    print(u'合并完毕！')


def clean(file):
    data = pd.read_csv(file , delimiter="," , header=0)
    data_clean = data.drop_duplicates()
    data_clean.to_csv(file , encoding='utf-8-sig' , index=False)
    print('数据去重完成')

if __name__ == "__main__":
    merge('C:/Users/yewei/Desktop/stock')
    clean('C:/Users/yewei/Desktop/stock/Stock.csv')