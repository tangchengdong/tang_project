# -*- coding: utf-8 -*-

from core.logger.logger import Loggl
from core.config import dbConfig
import pymysql
import pandas as pd


# 日志信息
log = Loggl(name=__file__)


class Mysql(object):
    def __init__(self, dbName):
        self.config = dbConfig()[dbName]
        self.host = self.config['host']
        self.user = self.config['user']
        self.passwd = self.config['passwd']
        self.db = self.config['db']
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, db=self.db, charset='utf8')

    # 保存数据
    def insert(self, data, sql=None, table=None, kind=None, if_exists='append', flavor='mysql', chunksize=None):
        try:
            con = self.conn
            if kind == 'pandas' and table:
                data.to_sql(con=con, name=table, index=False, if_exists=if_exists, flavor=flavor, chunksize=chunksize)
                print(u'插入数据成功')
            else:
                conn = self.conn
                cur = conn.cursor()
                cur.executemany(sql, data)
                self.conn.commit()
                cur.close()
                self.conn.close()
                print(u'成功关闭数据库')
        except Exception as e:
            log.logger.error('%s' % e)
            print(e)

    # 查询数据库 count=1返回数据库中条数, kind ='panads'返回panads格式的数据
    def select(self, sql, kind=None, index=None, count=None):
        try:
            con = self.conn
            if kind == 'panads':
                df = pd.read_sql(sql, con, index_col=index)
                return df
            elif count == 1:
                conn = self.conn
                cur = conn.cursor()
                results = cur.execute(sql)
                return results
            else:
                conn = self.conn
                cur = conn.cursor()
                cur.execute(sql)
                results = cur.fetchall()
                return results
        except Exception as e:
            log.logger.error('%s' % e)
            print(e)


if __name__ == '__main__':
    # sql = """INSERT INTO new VALUES(%s,%s,%s) """
    # data = [['你好', '就哦哦哦', '2018年02月02日 16:52']]
    # mysql = Mysql('biying').insert( data,sql=sql)
    # print(mysql)
    pass