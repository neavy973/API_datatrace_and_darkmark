import json
import pymysql

def conDb(database:str,host='192.168.209.1',port=3306,user='root',password='root',charset='utf8mb4'):
    db = pymysql.connect(
    host=host,
    port=port,
    user=user,  # 在这里输入用户名
    password=password,  # 在这里输入密码
    charset=charset,
    database=database
    )
    return db
def db_login():
    db = conDb(database='mytest', password='root')
    cursor = db.cursor()
    print("yeye")
    return db,cursor

def make_watermark(data,token):
    #查token数据库
    login_re=db_login()
    db=login_re[0]
    cursor=login_re[1]
    sql_1='select array from watermark where token="'+token+'";'
    cursor.execute(sql_1)
    db_re=cursor.fetchone()
    if(db_re==None):
        sql_2 = 'select max(id) from watermark;'
        cursor.execute(sql_2)
        id_=cursor.fetchone()[0]+1
        locate=bin(id_)
        locate=locate[2:]
        len_=locate.__len__()
        array_=[]
        for i in range(len_):
            if(locate[len_-i-1]=='1'):
                array_.append(i)

        sql_3  ='insert into watermark values('+str(id_)+',"'+token+'","'+str(array_)+'");'
        cursor.execute(sql_3)
        db.commit()
    else:
        array_=eval(db_re[0])
    #拿到array了
    my_data = data.decode()
    json_ = json.loads(data.decode())
    str1 = json_.get('\u533a\u6216\u53bf')
    int2 = ord(str1[0])
    location = int2 % 16
    if(location in array_):
        json_['\u533a\u6216\u53bf']=str1+'市'
        temp_data = json.dumps(json_)
        data = temp_data.encode()
        print(1)
    else:
        print(2)
    return data
