import hashlib
from random import randint
from citys import city

def makedata_(file_name, x, y):

    # 姓名，性别
    name_ls = []
    with open('Chinese_Names.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for i in range(y-x):
            num=randint(1,1144630)
            line=lines[num].split(',')
            if(line[1]!='未知'):
                name_ls.append([line[0],line[1]])
            else:
                name_ls.append([line[0],'男'])
    #省 市 区
    city_ls=city(y-x)

    #手机号
    phone_ls=[]
    phone1=['130','131','132','133','134','135','136','137','138','139',
            '150','151','158','171','172','177','179','180','181','184',
            '185','186','188','189']
    for i in range(y-x):
        num1=randint(0,23)
        num2=randint(0,9999)
        phone2=str(num2).zfill(4)
        num3 = randint(0, 9999)
        phone3=str(num3).zfill(4)
        phone_ls.append(phone1[num1]+phone2+phone3)
    with open(file_name,'w', encoding='utf-8')as file_:
        for i in range(0,y-x-1):
            email="email"+str(i+1)+'@163.com'
            password="password"+str(i+1)
            obj=hashlib.md5()
            obj.update((email+password).encode())
            token=obj.hexdigest()
            sql="insert into a_p_i2_users values("+str(i+1)+",'"+email+"','"+password+"','"+token+"','"+name_ls[i][0]+"','"+name_ls[i][1]+"','"+phone_ls[i]+"','"+city_ls[i][0]+"','"+city_ls[i][1]+"','"+city_ls[i][2]+"');"
            file_.write(sql+'\n')




makedata_('makedata.txt', 1, 99999)
