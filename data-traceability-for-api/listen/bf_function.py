import bloom_filter
import array
import base64
import json
from listen.data_function import db_login
hong_url='GET/vapi/api2/user/search/%'
c = bloom_filter.BloomFilter(max_elements=50000, error_rate=0.005)
b = bloom_filter.BloomFilter(max_elements=50000, error_rate=0.005)
'''
把单引号转化为双引号
'''
def change_yinghao(str):
    str=str.replace('\'','\"')
    return str

'''
#bytes类型to string类型，string用于存入数据库
'''
def my_b_to_str(b):
    e = base64.b64encode(b)
    str = e.decode('utf-8')
    return str

'''
#string类型to bytes类型，bytes用于frombytes转化为array
'''
def my_str_to_b(str):
    q = str.encode('utf-8')
    b = base64.b64decode(q)
    return b

'''
把message插入token的bf_set中
先查数据库，有无token的bf_set
    如果没有，就创建一个
    如果有，就取出来，转换
然后加进去，转换，放回去
'''
def my_bf_token_insert(db,cursor,token,message):
    flag=1
    sql_1="SELECT HashSet FROM bf_set WHERE TOKEN = '"+token+"'; "
    cursor.execute(sql_1)
    re_=cursor.fetchone()
    b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.1)
    if(re_==None):
        flag=0
    elif(re_!=None):
        array_ = array.array('L', [])
        array_str=re_[0]
        array_bytes=my_str_to_b(array_str)
        array_.frombytes(array_bytes)
        b.backend.array_=array_
    b.add(message)
    array_=b.backend.array_
    array_bytes=array_.tobytes()
    array_str=my_b_to_str(array_bytes)
    if(flag==0):
        sql_2= "INSERT INTO bf_set VALUES ('"+token+"','"+array_str+"');"
    elif(flag==1):
        sql_2= "UPDATE bf_set SET HashSet = '"+array_str+"' WHERE TOKEN = '"+token+"';"
    cursor.execute(sql_2)
    db.commit()

'''
把泄露数据读取出来
'''
def my_file_read(file_name):
    with open(file_name,'r') as file:
        lines = file.readlines()
        return lines

'''
把数据库中的数据取出来，按group by token.:group_lines()
然后按pattern处理数据：my_db_pattern()
根据每个token，做完hash_set,存入数据库bf_set:
'''
def my_db_pattern(lines_j,num,arges,pattern):
    lines_l=json.loads(lines_j)
    data_lines=my_file_read('../file_.txt')
    count=0
    for i in range(lines_l.__len__()):
        line_d=lines_l[i]
        str=line_d.get(arges[0])
        for j in range(1,num):
            str=str+' '+line_d.get(arges[j])
        print(str)
        b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.1)
        b.add(str)
    for i in range(data_lines.__len__()):
        if(data_lines[i] in b):
            count=count+1
    print("this percent ="+str(count)+"/"+str(data_lines.__len__()))

'''
先把文件中的数据拿出来
把token取出来
按照token取出一组json_s
把json_s一条一条转化为dictionary
然后通过参数构造字符串
将字符串存入token的bf_set
然后拿文件的比对bf_set
'''
def my_audit_full(file_name, nums, arges):
    print('bloom filter的全集方法')
    #先把文件拿出来
    #以免后面多次读
    with open(file_name,'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    #取数据库中的token
    login_re=db_login()
    db=login_re[0]
    cursor=login_re[1]
    sql_1= "select distinct TOKEN from log where URL like '"+hong_url+"';"
    cursor.execute(sql_1)
    db_re=cursor.fetchall()
    #每个token都要进行这个循环
    #取出token对应的json集合
    for i in range(db_re.__len__()):
        token_=db_re[i][0]
        b.intersection(c)
        #循环次数，offset=x*100
        x=0
        while(1):
            sql_2="select JSON from log where TOKEN = '"+token_+"' AND ACK=-1 limit 100 offset "+str(x*100)+";"
            cursor.execute(sql_2)
            # b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.005)
            json_s=cursor.fetchall()
            x=x+1
            if(json_s.__len__()==0):
                break
            # print(json_s)
            for j in range(json_s.__len__()):
                temp_kk = change_yinghao(json_s[j][0])
                dic_ = json.loads(temp_kk)
                line = dic_.get(arges[0])
                if(nums==1):
                    pass
                else:
                    for k in range(1,nums):
                        line=line+' '+dic_.get(arges[k])
                # print(token_+":"+line)
                b.add(line)
        #到这里可以获得该token对应的bf_set
        #接下来是把文件中的每行数据拿出来比对
        count=0
        for line in leak_lines:
            if(line in b):
                count=count+1
        if(count>=1):
            print("token:"+token_+"\t\t"+str(count)+"/"+str(leak_lines.__len__()))

def original_full(file_name, nums, arges):
    # 先把文件拿出来
    # 以免后面多次读
    with open(file_name, 'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    # 取数据库中的token
    login_re = db_login()
    db = login_re[0]
    cursor = login_re[1]
    sql_1 = "select distinct TOKEN from log where URL like '" + hong_url + "';"
    cursor.execute(sql_1)
    db_re = cursor.fetchall()
    # 每个token都要进行这个循环
    # 取出token对应的json集合
    for i in range(db_re.__len__()):
        token_ = db_re[i][0]
        count=0
        for line in leak_lines:
            line=line.split(' ')
            json_str="JSON->>'$."+arges[0]+"'='"+line[0]+"'"
            for num in range(1,nums):
                json_str=json_str+" and "+"JSON->>'$."+arges[num]+"'='"+line[num]+"'"
            sql_2 = "select * from log where TOKEN = '" + token_ + "' and ack=-1 and "+json_str+";"
            cursor.execute(sql_2)
            check_re=cursor.fetchall()
            if(check_re.__len__()>=1):
                count=count+1
        if(count>=1):
            print("token:" + token_ + "\n" + str(count) + "/" + str(leak_lines.__len__()))

'''
先查出flag为1的数据，
把数据按token分类
对token构造bf_set
如果有命中，就打印；没有命中，就跳过
'''
def my_audit_distinct(file_name, nums, arges):
    print("bloom filter 差集")
    with open(file_name, 'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    login_re = db_login()
    db = login_re[0]
    cursor = login_re[1]
    sql_1= "select distinct TOKEN from log_distinct where FLAG=1 and URL like '"+hong_url+"';"
    cursor.execute(sql_1)
    db_re=cursor.fetchall()
    # print(db_re)
    for i in range(db_re.__len__()):
        token_ = db_re[i][0]
        b.intersection(c)
        x = 0
        while( 1 ):
            sql_2="select JSON from log_distinct where flag=1 and ack=-1 and TOKEN='"+token_+"' limit 100 offset "+str(x*100)+";"
            cursor.execute(sql_2)
            # b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.005)
            json_s = cursor.fetchall()
            x=x+1
            if(json_s.__len__()==0):
                break
            # print(json_s)
            for j in range(json_s.__len__()):
                dic_ = json.loads(json_s[j][0])
                line = dic_.get(arges[0])
                if (nums == 1):
                    pass
                else:
                    for k in range(1, nums):
                        line = line + ' ' + dic_.get(arges[k])
                # print(token_+":"+line)
                b.add(line)
        # 到这里可以获得该token对应的bf_set
        # 接下来是把文件中的每行数据拿出来比对
        count = 0
        for line in leak_lines:
            if (line in b):
                count = count + 1
        if(count>=1):
            print("token:" + token_ + "\t\t" + str(count) + "/" + str(leak_lines.__len__()))


def original_distinct(file_name,nums,arges):
    print("mysql 差集")
    with open(file_name, 'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    login_re = db_login()
    db = login_re[0]
    cursor = login_re[1]
    sql_1= "select distinct TOKEN from log_distinct where FLAG=1 and URL like '"+hong_url+"';"
    cursor.execute(sql_1)
    db_re=cursor.fetchall()
    # print(db_re)
    for i in range(db_re.__len__()):
        token_ = db_re[i][0]
        count = 0
        for line in leak_lines:
            line = line.split(' ')
            json_str = "JSON->>'$." + arges[0] + "'='" + line[0] + "'"
            for num in range(1, nums):
                json_str = json_str + " and " + "JSON->>'$.\"" + arges[num] + "\"'='" + line[num] + "'"
            sql_2 = "select * from log_distinct where FLAG=1 and ack=-1 and TOKEN = '" + token_ + "' and " + json_str + ";"
            cursor.execute(sql_2)
            check_re = cursor.fetchall()
            if (check_re.__len__() >= 1):
                count = count + 1
        if (count >= 1):
            print("token:" + token_ + "\t\t" + str(count) + "/" + str(leak_lines.__len__()))

def for_distinct(file_name, nums, arges):
    print("in list 差集")
    with open(file_name, 'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    login_re = db_login()
    db = login_re[0]
    cursor = login_re[1]
    sql_1= "select distinct TOKEN from log_distinct where FLAG=1 and URL like '"+hong_url+"';"
    cursor.execute(sql_1)
    db_re=cursor.fetchall()
    # print(db_re)
    for i in range(db_re.__len__()):
        token_ = db_re[i][0]
        list=[]
        x = 0
        while( 1 ):
            sql_2="select JSON from log_distinct where flag=1 and ack=-1 and TOKEN='"+token_+"' limit 100 offset "+str(x*100)+";"
            cursor.execute(sql_2)
            # b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.005)
            json_s = cursor.fetchall()
            x=x+1
            if(json_s.__len__()==0):
                break
            # print(json_s)
            for j in range(json_s.__len__()):
                dic_ = json.loads(json_s[j][0])
                line = dic_.get(arges[0])
                if (nums == 1):
                    pass
                else:
                    for k in range(1, nums):
                        line = line + ' ' + dic_.get(arges[k])
                # print(token_+":"+line)
                list.append(line)
        # 到这里可以获得该token对应的bf_set
        # 接下来是把文件中的每行数据拿出来比对
        count = 0
        for line in leak_lines:
            if (line in list):
                count = count + 1

        print("token:" + token_ + "\t\t" + str(count) + "/" + str(leak_lines.__len__()))

def for_full(file_name, nums, arges):
    print("in list 的全集方法：")
    #先把文件拿出来
    #以免后面多次读
    with open(file_name,'r',encoding='UTF-8') as file:
        leak_lines = file.read().splitlines()
    #取数据库中的token
    login_re=db_login()
    db=login_re[0]
    cursor=login_re[1]
    sql_1= "select distinct TOKEN from log where URL like '"+hong_url+"';"
    cursor.execute(sql_1)
    db_re=cursor.fetchall()
    #每个token都要进行这个循环
    #取出token对应的json集合
    for i in range(db_re.__len__()):
        token_=db_re[i][0]
        list=[]
        #循环次数，offset=x*100
        x=0
        while(1):
            sql_2="select JSON from log where TOKEN = '"+token_+"' and ack=-1 limit 100 offset "+str(x*100)+";"
            cursor.execute(sql_2)
            # b = bloom_filter.BloomFilter(max_elements=1000, error_rate=0.005)
            json_s=cursor.fetchall()
            x=x+1
            if(json_s.__len__()==0):
                break
            # print(json_s)
            for j in range(json_s.__len__()):
                temp_kk=change_yinghao(json_s[j][0])
                dic_=json.loads(temp_kk)
                line = dic_.get(arges[0])
                if(nums==1):
                    pass
                else:
                    for k in range(1,nums):
                        line=line+' '+dic_.get(arges[k])
                # print(token_+":"+line)
                list.append(line)
        #到这里可以获得该token对应的bf_set
        #接下来是把文件中的每行数据拿出来比对
        count=0
        for line in leak_lines:
            if(line in list):
                count=count+1
        if(count>=1):
            print("token:"+token_+"\t\t"+str(count)+"/"+str(leak_lines.__len__()))





