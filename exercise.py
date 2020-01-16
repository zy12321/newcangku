# import pymysql
#
# # 连接数据库
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user="root",
#                      password="123456",
#                      database="stu",
#                      charset="utf8")
#
# # 生成游标对象（操作数据库，执行sql语句，获取结果）
# cur = db.cursor()
# inputname = input("请输入姓名：")
#
# # 执行各种sql操作（读）
# sql = "select name,age,score from interest where score > %s and age >= %s;"
# cur.execute(sql,[inputname])
#
# # 获取结果方法1
# for item in cur:
#     print(item)
#
# # 获取结果方法2
# # onedata = cur.fetchone()
# # print(onedata)
#
# # manydata = cur.fetchmany(2)
# # print(manydata)
# #
# # alldata = cur.fetchall()
# # print(alldata)
#
# # 关闭游标和数据库连接
# cur.close()
# db.close()



import pymysql
#连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

#生成游标对象（操作数据库，执行sql语句，获取结果）
cur = db.cursor()
fr = open("/home/tarena/month02/day16/dict.txt","r+")
#执行各种sql操作（写）
while True:
    data = fr.readline()
    if not data:
        break
    word = data.split(" ")[0]
    mean = data.split(" ",1)[-1]
    print([(word,mean)])
    try:
        sql = "insert into dict (word,mean) values (%s,%s);"
        cur.executemany(sql,[(word,mean)])
        db.commit()
    except:
        db.rollback()

fr.close()

#关闭游标和数据库连接
cur.close()
db.close()