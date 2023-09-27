import json
from time import sleep
from scapy.all import *
from scapy.layers import http

from listen.bf_function import change_yinghao
from listen.data_function import db_login

#宏定义
P_NUM=20
SERVER_IP="192.168.209.130"
filter_="host "+SERVER_IP+" and port 80"

'''
持续抓包_全集模式
'''
def my_listen_full():
    pkts = sniff(filter=filter_, session=TCPSession, iface='VMware Virtual Ethernet Adapter for VMnet8 #2', prn = my_response_full)

'''
持续抓包_差集模式
'''
def my_listen_distinct():
    pkts = sniff(filter=filter_, session=TCPSession, iface='VMware Virtual Ethernet Adapter for VMnet8 #2', prn = my_response_distinct)

'''
抓包
'''
def my_pcap():
    pkts = sniff(count=P_NUM,filter="host 192.168.209.128 and port 80" ,iface='VMware Virtual Ethernet Adapter for VMnet8 #2')
    return pkts

'''
处理一下字符串字段，就处理一下,在双引号前加转移字符
"INSERT INTO log VALUES ('192.168.255.129','2553578','http://baidu.com','yaoakjsdhwdhkjs','{\"name\":\"zhangsan\",\"flag\":-1}'"
'''
def my_translate(str):
    restr=re.compile('\"')
    b=restr.sub('\\"',str)
    return b

'''
过滤出需要的http包，并返回需要字段
如果http在数据包里，进行下一步，否则返回[-1,-1]
如果是发往服务器的，filter_re={1,ip,ack,url,auth_token}, {ip,ack,url,auth_token}
如果是服务器返回的第一个分片，filter_re={2,ip,seq,lenth}      {ip,ack+lenth,url,auth_token}
如果的服务器返回的，filter_re={3,ip,seq,json}            {ip,-1,url,auth_token,json}
流程：如果是请求的，就直接返回，然后存入数据库
    如果是第一个分片，就返回seq（ack），lenth，然后去数据库里查ack，然后把ack加上lenth
    如果是第二个分片，就返回，然后查ip，seq（ack），然后把json存进去
'''
def my_filter(pkt):
    print("**************************************************************************************")
    if(http.HTTP in pkt):
        p=pkt['TCP'].payload.payload
        if(pkt['IP'].dst==SERVER_IP):
            ip=pkt['IP'].src
            try:
                url=p.Method.decode()+p.Path.decode()
            except Exception as e:
                url=''
                print(repr(e))
            try:
                token=p.Authorization_Token.decode()
            except Exception as e:
                token=''
                print(repr(e))

            ack=pkt['TCP'].ack
            # print("mf1")
            return 1,ip,ack,url,token
        elif(pkt['IP'].src==SERVER_IP):
            ip = pkt['IP'].dst
            seq=pkt['TCP'].seq
            if(pkt.haslayer('Raw')):
                message = p.load.decode()
                # print("mf3")
                try:
                    json_ = json.loads(message)
                    message = str(json_)
                    message = change_yinghao(message)
                except Exception as e:
                    print(repr(e))
                return 3,ip,seq,message
            else:
                len_=len(pkt['TCP'].payload)
                # print("mf2")
                return 2,ip,seq,len_
        else:
            # print("mf-1")
            return -1, -1

    else:
        # print("mf-1")
        return -1,-1

'''
完成对数据包的处理，存入数据库
'''
def my_response_full(pkt):
    filter_re=my_filter(pkt)
    # print(0)
    if(filter_re[0]==-1):
        pass
    else:
        if (filter_re[0] == 1):
            print(1)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            sql = "INSERT INTO log (IP,ACK,URL,TOKEN) VALUES ('"+filter_re[1]+"','"+str(filter_re[2])+"','"+filter_re[3]+"','"+filter_re[4]+"');"
            cursor.execute(sql)
            db.commit()
            print("1finish")
        elif (filter_re[0] == 2):
            print(2)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            sql_1 = "SELECT ACK FROM log WHERE ACK ='" +str(filter_re[2])+"' and IP = '"+filter_re[1]+"';"
            # print("ack1:"+str(filter_re[2]))
            cursor.execute(sql_1)
            fetch_ = cursor.fetchone()
            if(fetch_==None):
                print("error:no such ack for this seq:"+str(filter_re[2]))
            else:
                ack=fetch_[0]
                ack_2=int(ack)+filter_re[3]
                # print("ack2:" + str(ack_2))
                sql_2="UPDATE log SET ACK = '"+str(ack_2) +"' where ACK = '"+ack +"';"
                # sleep(1)
                cursor.execute(sql_2)
                db.commit()
                print("2finish")
        elif (filter_re[0] == 3):
            print(3)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            # print("ack3:"+str(filter_re[2]))
            sql_1 = 'UPDATE log SET JSON = \''+filter_re[3]+'\' where ACK="'+str(filter_re[2])+'" and IP="'+filter_re[1]+'";'
            cursor.execute(sql_1)
            sql_2 = "UPDATE log SET ACK = '-1' where ACK='"+str(filter_re[2])+"' and IP='"+filter_re[1]+"';"
            cursor.execute(sql_2)
            db.commit()
            print("3finish")
    return

'''
检查是否是重复的token+url
是返回1，不是返回0
'''
def if_repeat_token_url(token,url):
    login_re = db_login()
    db = login_re[0]
    cursor = login_re[1]
    sql="SELECT * FROM log WHERE TOKEN = '"+token+"' and URL = '"+url+"';"
    re_=cursor.execute(sql)
    db.commit()
    if(re_>=1):
        return 1
    elif(re==0):
        return 0


'''
判断是否是独一无二的包再存入，减小日志存储压力
***
表：log_distinct(IP, ACK, FLAG, URL, TOKEN, JSON)
***
拿到包，先获取要的东西
如果http在数据包里，进行下一步，否则返回[-1,-1]
如果是发往服务器的，filter_re={1,ip,ack,url,auth_token}, {ip,ack,url,auth_token}
如果是服务器返回的第一个分片，filter_re={2,ip,seq,lenth}      {ip,ack+lenth,url,auth_token}
如果的服务器返回的，filter_re={3,ip,seq,json}            {ip,-1,url,auth_token,json}
***
前面处理不变，但是在第三个分片处
我先查这个json在数据库中是否有重复（非同一个json）
如果有重复，就把重复的那个标记为-1
把当前这个删掉
'''
def my_response_distinct(pkt):
    filter_re=my_filter(pkt)
    if (filter_re[0] == -1):
        # print(-1)
        pass
    else:
        if (filter_re[0] == 1):
            # print(1)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            sql = "INSERT INTO log_distinct (IP,ACK,URL,TOKEN) VALUES ('"+filter_re[1]+"','"+str(filter_re[2])+"','"+filter_re[3]+"','"+filter_re[4]+"');"
            cursor.execute(sql)
            db.commit()
            # print("1finish")
        elif (filter_re[0] == 2):
            # print(2)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            sql_1 = "SELECT ACK FROM log_distinct WHERE ACK ='" +str(filter_re[2])+"' and IP = '"+filter_re[1]+"';"
            # print("ack1:"+str(filter_re[2]))
            cursor.execute(sql_1)
            fetch_ = cursor.fetchone()
            if(fetch_==None):
                print("error:no such ack for this seq:"+str(filter_re[2]))
            else:
                ack=fetch_[0]
                ack_2=int(ack)+filter_re[3]
                # print("ack2:" + str(ack_2))
                sql_2="UPDATE log_distinct SET ACK = '"+str(ack_2) +"' where ACK = '"+ack +"';"
                # sleep(1)
                cursor.execute(sql_2)
                db.commit()
                # print("2finish")
        elif (filter_re[0] == 3):
            # print(3)
            login_re = db_login()
            db = login_re[0]
            cursor = login_re[1]
            #检查是否是重复的
            # json重复了
            sql_1 = "SELECT * FROM log_distinct where JSON='"+filter_re[3]+"';"
            cursor.execute(sql_1)
            db_re=cursor.fetchall()
            # json重合了
            if(db_re.__len__()>=1):
                #这个是目前只有一个人请求的
                #flag=1
                if(db_re[0][2]==1):
                    #把当前处理请求的ack拿出来比对当前正在写的行的token
                    sql_4 = "select TOKEN from log_distinct where ACK= '"+str(filter_re[2])+"';"
                    cursor.execute(sql_4)
                    token_re=cursor.fetchall()
                    # 如果之前请求的不是当前的用户就标记为-1
                    # 如果是这个用户请求过的就不用管
                    if(token_re.__len__()==0):
                        print("error,no this line")
                    elif(token_re[0][0]!=db_re[0][4]):
                        sql_2 = "UPDATE log_distinct SET FLAG = -1,TOKEN='' WHERE JSON = '"+filter_re[3]+"';"
                        cursor.execute(sql_2)
                    # 把当前的这条删掉
                    sql_3 = "DELETE FROM log_distinct WHERE ACK= '" + str(filter_re[2]) + "' and IP ='" + filter_re[
                        1] + "';"
                    cursor.execute(sql_3)
                # 已经有大于两个人请求过了
                # 把当前的删掉就好
                elif(db_re[0][2]==-1):
                    sql_2 = "DELETE FROM log_distinct WHERE ACK= '"+str(filter_re[2])+"' and IP ='"+filter_re[1]+"';"
                    cursor.execute(sql_2)
            # json没有重合，直接插入就好
            else:
                sql_3 = "UPDATE log_distinct SET JSON = '" + filter_re[3] + "' ,ACK = '-1' where ACK='" + str(
                    filter_re[2]) + "' and IP='" + filter_re[1] + "';"
                cursor.execute(sql_3)
            # print("ack3:"+str(filter_re[2]))
            db.commit()
            print("3finish")
    return









