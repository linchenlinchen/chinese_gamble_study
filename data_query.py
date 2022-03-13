import pymysql
def get_url():
    # 根据流程
    # 1.我们先建立数据库的连接信息
    host = "ml.a0ab.com"  # 数据库的ip地址
    user = "fraud"  # 数据库的账号
    password = "N0_fr@ud"  # 数据库的密码
    port = 3306  # mysql数据库通用端口号
    mysql = pymysql.connect (host=host, user=user, password=password, port=port)

    #2.新建个查询页面
    cursor = mysql.cursor()


    #3编写sql
    sql = 'select target_url from fraud_detection_v2.datacon_crawler_event where is_gamble=1'

    #4.执行sql
    cursor.execute(sql)

    #5.查看结果
    results = cursor.fetchall() #用于返回多条数据
    print(results)

    #6.关闭查询
    cursor.close()

    #关闭数据库
    mysql.close()
    return results
