import datetime
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import FileResponse
from game.t2 import final
import pandas as pd
import joblib
import re
import numpy as np
# Create your views here.

def start(request):
    html = get_template("快速.html")
    html = html.render()
    return HttpResponse(html)
def 开始说明(request):
    html = get_template("快速.html")
    html = html.render()
    return HttpResponse(html)
def start_(request):
    html=get_template("快速1.html")
    str1=request.GET['word']
    st,b=stary_ut(str1)
    a=list()
    x=0
    y=0
    for i in range(len(st)):
        a.append(predictt(st[i]))
        if predictt(st[i])=='僵尸企业':
            x=x+1
        else:
            y=y+1
    c=dict()
    for i in range(len(a)):
        c[b[i]]=a[i]
    l1=['无','无','无','无','无','无','无','无','无','无','无','无','无']
    l2=['无','无','无','无','无','无','无','无','无','无','无','无','无']
    if len(b) >=len(l1):
        l1=b[0:5]
        l2=a[0:5]
    else:
        for i in range(len(b)):
            l1[i]=b[i]
            l2[i]=a[i]
    html=html.render({"oo":'结果显示 (ID:结果)','list1':l1,'list2':l2,'x':x,'y':y})
    return HttpResponse(html)

def 单个查询(request):
    html = get_template("单个查询.html")
    html = html.render()
    return HttpResponse(html)


# 分析#
def make(c):
    c = np.array(c)
    c = c.reshape((1, 27))
    return c


def q(n):
    if n > 0.5:
        n = 1
    else:
        n = 0
    return n


def predictt(cs):
    cs = list(map(float, cs))
    cs = make(cs)

    clf5 = joblib.load(r'no_ID/RandomForestClassifier.pkl')
   
    a5 = clf5.predict(cs)
    a5 = q(a5)
    sum = a5
    if sum >= 1:
        sum = "僵尸企业"
    else:
        sum = "非僵尸企业"
    return sum


def l(q):
    c = []
    t = [0, 203427, 510, 0, 260, 4968, 1528, 25525, 00, 101429, 4, 0, -26649, 0.7, 1, 2008, 5027, 000, 198, 4968,
         339831, 0, 5, 160340, 133646, 59, 998]
    for i in range(len(q)):
        if q[i] == 'NA':
            c.append(t[i])
        else:
            c.append(float(q[i]))
    return c


def ll(q):
    c = []
    t = [0, 203427, 510, 0, 260, 4968, 1528, 25525, 00, 101429, 4, 0, -26649, 0.7, 1, 2008, 5027, 000, 198, 4968,
         339831, 0, 5, 160340, 133646, 59, 998]
    for i in range(len(q)):
        if q[i] == '':
            c.append(t[i])
        else:
            c.append(float(q[i]))
    return c


def stary_ut(str1):
    str1.replace('交通运输业', '0')
    str1.replace('服务业', '1')
    str1.replace('工业', '2')
    str1.replace('社区服务', '3')
    str1.replace('零售业', '4')
    str1.replace('商业服务业', '5')
    str1.replace('福建', '0')
    str1.replace('广东', '1')
    str1.replace('江西', '2')
    str1.replace('山东', '3')
    str1.replace('广西', '4')
    str1.replace('湖南', '5')
    str1.replace('湖北', '6')
    str1.replace('农民专业合作社', '0')
    str1.replace('集体所有制企业', '1')
    str1.replace('股份有限公司', '2')
    str1.replace('有限责任公司', '3')
    str1.replace('合伙企业', '4')
    str1.replace('企业法人', '0')
    str1.replace('自然人', '1')

    l1 = str1.split(';')
    list2 = list()
    list4 = list()
    if l1 != ['']:
        for i in l1:
            list3 = list()
            list4.append(re.sub(r'[^\d]', '', str(re.findall(r'ID\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'专利\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'主营业务收入\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'从业人数\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'企业类型\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'债权融资成本\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'债权融资额度\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'内部融资和贸易融资成本\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'内部融资和贸易融资额度\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'净利润\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'利润总额\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'区域\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'商标\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'所有者权益合计\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'控制人持股比例\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'控制人类型\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'注册时间\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'注册资本\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'纳税总额\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'股权融资成本\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'股权融资额度\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'营业总收入\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'著作权\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'行业\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'负债总额\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'资产总额\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'项目融资和政策融资成本\d+', i))))
            list3.append(re.sub(r'[^\d]', '', str(re.findall(r'项目融资和政策融资额度\d+', i))))
            tmp = ll(list3)
            list2.append(tmp)
    return list2, list4


def start_(request):
    html = get_template("快速1.html")
    str1 = request.GET['word']
    st, b = stary_ut(str1)
    a = list()
    x = 0
    y = 0
    for i in range(len(st)):
        a.append(predictt(st[i]))
        if predictt(st[i]) == '僵尸企业':
            x = x + 1
        else:
            y = y + 1
    c = dict()
    for i in range(len(a)):
        c[b[i]] = a[i]
    l1 = ['无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无']
    l2 = ['无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无', '无']
    if len(b) >= len(l1):
        l1 = b[0:5]
        l2 = a[0:5]
    else:
        for i in range(len(b)):
            l1[i] = b[i]
            l2[i] = a[i]
    html = html.render({"oo": '结果显示 (ID:结果)', 'list1': l1, 'list2': l2, 'x': x, 'y': y})
    return HttpResponse(html)


def nn(request):
    html = get_template("new.html")
    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])
    cqq = dict()
    for i in range(len(a)):
        cqq[a[i]] = b[i]
    html = html.render({'a': cqq})
    return HttpResponse(html)


def nn1(request):
    html = get_template("new.html")
    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])
    cqq = dict()
    for i in range(len(a)):
        cqq[a[i]] = b[i]
    str1 = request.GET['word']
    if str1 == '':
        html = html.render({'a': cqq})
        return HttpResponse(html)
    if int(str1) in cqq.keys():
        t = cqq[int(str1)]
    else:
        t = 'ID错误'
    html = html.render({'a': cqq, 'b': t})
    return HttpResponse(html)
def d(request):
   file = open(r'file/down/1900824-凤飞千仞.csv', 'rb')
   response = FileResponse(file)
   return response

def nn2(request):
    html = get_template("new1.html")
    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])
    cqq = dict()
    for i in range(len(a)):
        cqq[a[i]] = b[i]
    html = html.render({'a': cqq})
    return HttpResponse(html)


def 单查(request):
    html = get_template("单查1.html")
    html = html.render()
    return HttpResponse(html)


def 批量(request):
    aa = "未上传"
    bb = "未上传"
    cc = "未上传"
    dd = "未上传"
    html = get_template("批量1.html")
    html = html.render({"an": aa, "bn": bb, "cn": cc, "dn": dd})
    return HttpResponse(html)
def l3(q):
    c=[]
    x=0
    for i in range(len(q)):
        if q[i]=='NA':
            c.append(0.0)
        else:
            x=x+1
            c.append(float(q[i]))
    return c,x

def 查找(request):
    temp = []
    message = ''
    if 1:
        for i in range(98, 123):
            str = chr(i)
            if request.GET[str] == '':
                message = "NA"
                temp.append(message)
            else:
                message = request.GET[str]
                temp.append(message)

        if request.GET['aa'] == '':
            message = "NA"
            temp.append(message)
        else:
            message = request.GET['aa']
            temp.append(message)

        if request.GET['ab'] == '':
            message = "NA"
            temp.append(message)
        else:
            message = request.GET['ab']
            temp.append(message)
        q = l(temp)
        temp1, n = l3(temp)
        starttime = datetime.datetime.now()
        a = predictt(q)
        out1 = 0
        out3 = a
        if a == '僵尸企业':
            out1 = '僵尸企业'
        else:
            out1 = '非僵尸企业'
        endtime = datetime.datetime.now()
        n = n / 27 * 100
        if n < 33:
            m = '偏低'
        elif n < 70:
            m = '中等'
        elif n < 80:
            m = '较好'
        else:
            m = '很好'

        x = endtime - starttime

        html = get_template("单查2.html")
        html = html.render(
            {'zai': '再次', 'input': temp, 'out1': out1, 'out3': out3, 'm': n, 'mm': m,
             'time': x})
    return HttpResponse(html)
# {=========================批量===============================}
def 批量(request):
    html = get_template("批量查询.html")
    html = html.render()
    return HttpResponse(html)
@csrf_exempt
def 批量1(request):
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        obj1 = request.FILES.get('f1')  # 上传文件是用files获取，是一个对象
        obj2 = request.FILES.get('f2')
        obj3 = request.FILES.get('f3')
        obj4 = request.FILES.get('f4')
        if obj1:
            c1 = 1
            file_path1 = os.path.join('file\\up', "base_sum.csv")
            f = open(file_path1, 'wb')
            for i in obj1.chunks():  # chunks方法是一点点获取上传的文件内容
                f.write(i)
            f.close()
            aa = "成功上传"
            # file_data=obj1.read().decode("utf-8")
            # lines=file_data.split("\n")
            # for line in lines[1:]:
            #     feild=line.split(",")
            #     data_dict={}
            #     data_dict["ID1"]=feild[0]
            #     data_dict["in_time"]=feild[1]
            #     data_dict["capital"]=feild[2]
            #     data_dict["work"]=feild[3]
            #     data_dict["area"]=feild[4]
            #     data_dict["compy_kind"]=feild[5]
            #     data_dict["peo_kind"]=feild[6]
            #     data_dict["ratio"]=feild[7]
            #     fm=base(data_dict)
            #     fm.save()
        else:
            aa = "上传失败"
        if obj2:
            c2 = 1
            file_path2 = os.path.join('file/up', 'knowledge_sum.csv')
            f = open(file_path2, 'wb')
            for i in obj2.chunks():  # chunks方法是一点点获取上传的文件内容
                f.write(i)
            f.close()
            bb = "成功上传"
        #      file_data=obj2.read().decode("utf-8")
        #      lines=file_data.split("\n")
        #      for line in lines[1:]:
        #          feild=line.split(",")
        #          data_dict={}
        #          data_dict["ID2"]=feild[0]
        #           fm=know(data_dict)
        #           fm.save()
        else:
            bb = "上传失败"
        if obj3:
            c3 = 1
            file_path3 = os.path.join('file/up', 'money_report_sum1.csv')
            f = open(file_path3, 'wb')
            for i in obj3.chunks():  # chunks方法是一点点获取上传的文件内容
                f.write(i)
            f.close()
            cc = "成功上传"
        #        file_data=obj3.read().decode("utf-8")
        #       lines=file_data.split("\n")
        #       for line in lines[1:]:
        #           feild=line.split(",")
        #           data_dict={}
        #          data_dict["x"]=feild[0]
        #          fm=money(data_dict)
        #          fm.save()
        else:
            cc = "上传失败"
        if obj4:
            c4 = 1
            file_path4 = os.path.join('file/up', 'year_report_sum.csv')
            f = open(file_path4, 'wb')
            for i in obj4.chunks():  # chunks方法是一点点获取上传的文件内容
                f.write(i)
            f.close()
            dd = "成功上传"
        #     file_data=obj4.read().decode("utf-8")
        #     lines=file_data.split("\n")
        #     for line in lines[1:]:
        ##         feild=line.split(",")
        #         data_dict={}
        #         data_dict["x"]=feild[0]
        #         fm=year(data_dict)
        #         fm.save()
        else:
            dd = "上传失败"
        k = "失败"
        if c1 == 1 and c2 == 1 and c3 == 1 and c4 == 1:
            k = "成功"
        kk = "文件规格比较大，分析时间可能会更长"
        if k == "失败":
            html = get_template("批量查询.html")
            html = html.render({"jul": k, "an": aa, "bn": bb, "cn": cc, "dn": dd})
            return HttpResponse(html)
        else:
            html = get_template("批量1.html")
            html = html.render({"jul": k, "an": aa, "bn": bb, "cn": cc, "dn": dd, 'al': kk})
            return HttpResponse(html)
@csrf_exempt
def 批量2(request):
    file_path1 = os.path.join('file/up', "base_sum.csv")
    file_path2 = os.path.join('file/up', 'knowledge_sum.csv')
    file_path3 = os.path.join('file/up', 'money_report_sum1.csv')
    file_path4 = os.path.join('file/up', 'year_report_sum.csv')
    starttime = datetime.datetime.now()
    final(file_path1, file_path2, file_path3, file_path4)
    endtime = datetime.datetime.now()
    xx = endtime - starttime

    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])

    c = dict()

    ff=[]
    for i in range(len(a)):
        tem = dict()
        c[a[i]] = b[i]
        if b[i] == "僵尸企业":
            tem = {'num': i, 'ID': int(a[i]), 'name': '僵尸企业'}
            ff.append(tem)
        if b[i] == "非僵尸企业":
            tem = {'num': i, 'ID': int(a[i]), 'name': '非僵尸企业'}
            ff.append(tem)

    a1 = 0
    b1 = 0
    for i in b:
        if i == "僵尸企业":
            a1 = a1 + 1
        if i == "非僵尸企业":
            b1 = b1 + 1
    html = get_template("批量2.html")
    html = html.render(
        {'jj':ff, 'time': xx,  'x': a1,'y': b1,})
    return HttpResponse(html)

@csrf_exempt
def 批量3(request):
    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])


    c = dict()

    ff=[]
    for i in range(len(a)):
        tem = dict()
        c[a[i]] = b[i]
        if b[i] == "僵尸企业":
            tem = {'num': i, 'ID': int(a[i]), 'name': '僵尸企业'}
            ff.append(tem)
        if b[i] == "非僵尸企业":
            tem = {'num': i, 'ID': int(a[i]), 'name': '非僵尸企业'}
            ff.append(tem)

    a1 = 0
    b1 = 0
    for i in b:
        if i == "僵尸企业":
            a1 = a1 + 1
        if i == "非僵尸企业":
            b1 = b1 + 1
    ini = request.GET['lll']

    if ini == '':
        oou = '输入错误'
        xx = 'NO'
    else:
        if int(ini) in c.keys():
            xx = int(ini)
            oou = c[int(ini)]
        else:
            xx = int(ini)
            oou = '输入错误'
    html = get_template("批量3.html")
    html = html.render(
        {'jj':ff,  'x': a1,'y': b1,'out':str(xx)+':'+oou})
    return HttpResponse(html)

@csrf_exempt
def 批量32(request):
    f = open(r'file/down/out.csv', 'r')
    csv = pd.read_csv(f)
    f.close()
    a = list(csv["ID"])
    b = list(csv["out"])
    c = dict()

    x=0
    y=0
    ff=[]
    for i in range(len(a)):
        tem = dict()
        c[a[i]] = b[i]
        if b[i]=="僵尸企业":
            x=x+1
            tem={'num':i,'ID':int(a[i]),'name':'僵尸企业'}
            ff.append(tem)

        if b[i]=="非僵尸企业":
            y=y+1
            tem={'num':i,'ID':int(a[i]),'name':'非僵尸企业'}
            ff.append(tem)

    ini=request.GET['lll']

    if ini=='':
        oou = '输入错误'
        xx='NO'
    else:
        if int(ini)  in c.keys():
            xx=int(ini)
            oou = c[int(ini)]
        else:
            xx = int(ini)
            oou='输入错误'
    html = get_template("批量3.html")
    html = html.render({'ouo1':xx,'ouo':oou,'jj':ff,'x':x,'y':y})
    return HttpResponse(html)

def oo(request):
    html = get_template("zz.html")
    html = html.render()
    return HttpResponse(html)