import pymysql

def conDb(database:str,host='localhost',port=3306,user='root',password='root',charset='utf8mb4'):
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
    return db,cursor
