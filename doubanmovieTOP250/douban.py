# -*- coding: utf-8 -*-
# Captain_N
 
 
from lxml import etree
import random
import requests
import time
import pymysql   #导入相应库文件
 
conn = pymysql.connect(host='localhost',user='root',password='123456',db='qzpy',port=3306,charset='utf8')
cursor=conn.cursor()    #连接数据库及光标
headers={
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}     #请求头
 
 
 
def get_info(url):
    res=requests.get(url,headers=headers)
    if res.status_code==200:
        selector=etree.HTML(res.text)
        infos=selector.xpath('//div[@class="item"]')
        for info in infos:
            name=info.xpath('div[2]/div[@class="hd"]/a/span[1]/text()')[0]
            url=info.xpath('div[1]/a/@href')[0]
            movies_infos=info.xpath('div[2]/div[@class="bd"]/p[1]/text()')[0].strip('\n').strip('\xa0')
            #movies_infos=info.xpath('div[2]/div[@class="bd"]/p[1]/text()')

            director = movies_infos[:movies_infos.find('主演')].strip()
            actor = movies_infos[movies_infos.find('主演'):].strip()

            ping_infos=info.xpath('div[2]/div[@class="bd"]/p[1]/text()')[1].strip('\n').strip('\xa0')
            year =ping_infos.split('/')[0].strip()
            region =ping_infos.split('/')[1].strip()
            type =ping_infos.split('/')[2].strip()

            rate=info.xpath('div[2]/div[2]/div[@class="star"]/span[2]/text()')[0]
            comments=info.xpath('div[2]/div[2]/p[@class="quote"]/span[1]/text()')
            if len(comments)!=0:
                comment=comments[0]
            else:
                comment='空'       #防止无评论

            #print(comment)
            cursor.execute("insert into doubanmovie(name,url,director,actor,year,region,type,rate,comment) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (str(name),str(url),str(director),str(actor),str(year),str(region),str(type),str(rate),str(comment)))     #按对应字段写入数据库   
            
 
    else:
        print('failed')
    
 

if __name__=='__main__':     #主程序入口
    urls=['https://movie.douban.com/top250?start={}'.format(i*25) for i in range(0,10)]     #构建需要爬去的页面连接
    
    for url in urls:
        get_info(url)  #调用爬去详细信息函数
        time.sleep(random.random()*2)
    conn.commit()