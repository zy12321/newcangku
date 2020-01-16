import pymysql
#连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

#生成游标对象（操作数据库，执行sql语句，获取结果）
cur = db.cursor()

#执行各种sql操作（写）
try:
    sql = "insert into cls(name,age,score) values(\
      %s,%s,%s);"

    cur.execute(sql,["Tom",16,54])

    sql = "update cls set sex = 'm' where name = 'Jame';"
    cur.execute(sql)

    sql = "delete from cls where sex is null;"
    cur.execute(sql)

    db.commit()
except:
    db.rollback()
#关闭游标和数据库连接
cur.close()
db.close()
