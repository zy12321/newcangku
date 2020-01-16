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

#执行各种sql操作（读）
sql = "select name,age,score from cls;"
cur.execute(sql)

#获取结果方法1
# for item in cur:
#     print(item)

#获取结果方法2
onedata = cur.fetchone()
print(onedata)

manydata = cur.fetchmany(2)
print(manydata)

alldata = cur.fetchall()
print(alldata)            

#关闭游标和数据库连接
cur.close()
db.close()