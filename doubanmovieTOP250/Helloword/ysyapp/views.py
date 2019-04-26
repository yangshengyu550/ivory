from django.shortcuts import render
#from django_tables2 import RequestConfig
from ysyapp import models
#from ysyapp.models import Doubanmovie
#from ysyapp.tables import Showlist

#def show(request):
    #table = Showlist(Doubanmovie.objects.all())
    #RequestConfig(request, paginate={'per_page': 25}).configure(table) #分页
    #return render(request, 'templates/index.html', {'table': table}) #导入


# Create your views here.
import MySQLdb
def get_data(sql):#获取数据库的数据
    conn = MySQLdb.connect('127.0.0.1','root','123456','qzpy',port=3306)   #test为数据库名
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall() # 搜取所有结果
    cur.close()
    conn.close()
    return results
def order(request):# 向页面输出订单
    sql = "select * from doubanmovie" 
    m_data = get_data(sql)
    return render(request,'index.html',{'order':m_data})

