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
# with open("下载.jpeg","rb") as f:
#     data = f.read()
#
# try:
#     sql = "update cls set image = %s where name = 'Ameame';"
#     cur.execute(sql,[data])
#
#     db.commit()
# except:
#     db.rollback()


sql = "select image from cls where name = 'Ameame';"
cur.execute(sql)
data = cur.fetchone()
with open("Ame.jpg","wb") as f:
    f.write(data[0])
#关闭游标和数据库连接
cur.close()
db.close()