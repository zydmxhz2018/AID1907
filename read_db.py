"""
read_db.py
pymysql 读数据库  select
"""

import  pymysql

#  链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 生成游标对象 (用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# select操作
sql = "select name,age,score from cls1 \
where score>60 order by score desc;"
cur.execute(sql) # 执行语句

# cur 可迭代对象，通过迭代获取select结果
# for i in cur:
#     print(i)

print("=================================")
# 获取一个结果
print(cur.fetchone())

# 获取多个查询结果
print(cur.fetchmany(3))

# 获取所有查询结果
print(cur.fetchall())

# 关闭游标和数据库链接
cur.close()
db.close()
