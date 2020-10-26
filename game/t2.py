import numpy as np
import pandas as pd
import joblib
import os

def q(n):
   n[n>0.5]=1
   n[n<=0.5]=0
   return pd.DataFrame(n)

def w(a):
    temm=[]
    s=a.values.shape[0]
    a=np.array(a.values,dtype=np.int32)
    for i in range(s):
        tem=np.argmax(np.bincount(a[i,:]))
        temm.append(tem)
    return pd.DataFrame(temm,columns=["out"])
    
def predic(cs):
    aa=cs
    p=['专利', '主营业务收入', '从业人数', '企业类型', '债权融资成本', '债权融资额度',
      '内部融资和贸易融资成本', '内部融资和贸易融资额度', '净利润', '利润总额', '区域', '商标', '所有者权益合计',
     '控制人持股比例', '控制人类型', '注册时间', '注册资本', '纳税总额', '股权融资成本', '股权融资额度', '营业总收入',
      '著作权', '行业', '负债总额', '资产总额', '项目融资和政策融资成本', '项目融资和政策融资额度']
    clf5=joblib.load(r'no_ID/RandomForestClassifier.pkl')
    a5=clf5.predict(cs[p])
    a5=q(a5)
    t=a5
    t=w(t)
    t_c=list(t.columns)
    t_c.extend(aa.columns)
    a_a=aa.values
    t_a=t.values
    u=np.hstack((t_a,a_a))
    aa=pd.DataFrame(u,columns=t_c)
    return aa
    
    
def pro(csv):
    s1=set(csv["行业"])
    if '交通运输业' in s1:
        csv.loc[csv["行业"]=='交通运输业','行业']=0
    if '服务业' in s1:   
        csv.loc[csv["行业"]=='服务业','行业']=1
    if '工业' in s1:   
        csv.loc[csv["行业"]=='工业','行业']=2
    if '社区服务' in s1:  
        csv.loc[csv["行业"]=='社区服务','行业']=3
    if '零售业' in s1:     
        csv.loc[csv["行业"]=='零售业','行业']=4
    if '商业服务业' in s1: 
        csv.loc[csv["行业"]=='商业服务业','行业']=5
    
    s2=set(csv["区域"])
    if '福建' in s2: 
        csv.loc[csv["区域"]=='福建','区域']=0
    if '广东' in s2: 
        csv.loc[csv["区域"]=='广东','区域']=1
    if '江西' in s2:     
        csv.loc[csv["区域"]=='江西','区域']=2
    if '山东' in s2:     
        csv.loc[csv["区域"]=='山东','区域']=3
    if '广西' in s2:     
        csv.loc[csv["区域"]=='广西','区域']=4
    if '湖南' in s2:     
        csv.loc[csv["区域"]=='湖南','区域']=5
    if '湖北' in s2:     
        csv.loc[csv["区域"]=='湖北','区域']=6
        
    s3=set(csv["企业类型"])
    if '农民专业合作社' in s3:
        csv.loc[csv["企业类型"]=='农民专业合作社','企业类型']=0
    if '集体所有制企业' in s3:    
        csv.loc[csv["企业类型"]=='集体所有制企业','企业类型']=1
    if '股份有限公司' in s3:    
        csv.loc[csv["企业类型"]=='股份有限公司','企业类型']=2
    if '有限责任公司' in s3:   
        csv.loc[csv["企业类型"]=='有限责任公司','企业类型']=3
    if '合伙企业' in s3:   
        csv.loc[csv["企业类型"]=='合伙企业','企业类型']=4
     
    s4=set(csv["控制人类型"])
    if '企业法人' in s4:   
        csv.loc[csv["控制人类型"]=='企业法人',"控制人类型"]=0
    if '自然人' in s4:   
        csv.loc[csv["控制人类型"]=='自然人',"控制人类型"]=1
    csv["注册资本"]=csv["注册资本"].fillna(5027.667386609071)
    csv["注册时间"]=csv["注册时间"].fillna(2008)
    csv["控制人持股比例"]=csv["控制人持股比例"].fillna(0.7547622787579623)
    csv["行业"]=csv["行业"].fillna(5)
    csv["区域"]=csv["区域"].fillna(4)
    csv["企业类型"]=csv["企业类型"].fillna(0)
    csv["控制人类型"]=csv["控制人类型"].fillna(1)
    csv["债权融资额度"]=csv["债权融资额度"].fillna(3249.57546)
    csv["债权融资成本"]=csv["债权融资成本"].fillna(260.256957168)
    csv["股权融资额度"]=csv["股权融资额度"].fillna(4968.317573838778)
    csv["股权融资成本"]=csv["股权融资成本"].fillna(198.92291653901867)
    csv["内部融资和贸易融资额度"]=csv["内部融资和贸易融资额度"].fillna(25525.513921909685)
    csv["内部融资和贸易融资成本"]=csv["内部融资和贸易融资成本"].fillna(1528.3626466101935)
    csv["项目融资和政策融资额度"]=csv["项目融资和政策融资额度"].fillna(998.0509550460752)  
    csv["项目融资和政策融资成本"]=csv["项目融资和政策融资成本"].fillna(59.90220185689055)
    csv["从业人数"]=csv["从业人数"].fillna(510)                                             
    csv["资产总额"]=csv["资产总额"].fillna(133646.93822060764)
    csv["负债总额"]=csv["负债总额"].fillna(160340.74159219087) 
    csv["营业总收入"]=csv["营业总收入"].fillna(339831.4344164056) 
    csv["主营业务收入"]=csv["主营业务收入"].fillna(203427.00849747626)
    csv["所有者权益合计"]=csv["所有者权益合计"].fillna(-26649.339562757297)
    csv["利润总额"]=csv["利润总额"].fillna(101429.15395812289)
    csv["净利润"]=csv["净利润"].fillna(-30252.11723959263)
    csv["纳税总额"]=csv["纳税总额"].fillna(0)     
    csv["专利"]=csv["专利"].fillna(0)
    csv["商标"]=csv["商标"].fillna(0)
    csv["著作权"]=csv["著作权"].fillna(0)
    csv=pd.DataFrame(csv.groupby('ID').mean())
    csv["ID"]=csv.index
    cc=csv
    cc.reset_index(drop=True)
    return cc

    
def geta(a):
    b=pd.merge(a[0],a[1],how='outer',on='ID')
    a=pd.merge(a[2],a[3],how='outer',on=['ID','year'])
    
    c=pd.merge(a,b,how='outer',on='ID')

    return c

def do(a):
    f=open(a,'r+',encoding='utf-8')
    csv=pd.read_csv(f)
    f.close()
    csv=pd.DataFrame(csv)
    return csv

def final(a,b,c,d):
    t=list([a,b,c,d])
    for i in range(len(t)):
        t[i]=do(t[i])
    csv=geta(t)
    out=pro(csv)

    out=predic(out)
    out["分类结果"]=out["out"]
    out.loc[out["out"]==1,'out']='僵尸企业'
    out.loc[out["out"]==0,'out']='非僵尸企业'
    file_path1 = os.path.join('file/down',"1900824-凤飞千仞.csv")
    out[["out","ID"]].to_csv(file_path1,index=False,header=True,encoding='gbk')
  
    file_path2 = os.path.join('file/down',"1900824-凤飞千仞-【A09】僵尸企业画像及分类【科创信息】-测试结果.csv")
    out[["ID","分类结果"]].astype(int).to_csv(file_path2,index=False,header=True,encoding='utf-8')



def fin(a,b,c,d):
    t = list([a, b, c, d])
    for i in range(len(t)):
        t[i] = do(t[i])
    csv = geta(t)