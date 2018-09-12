# -*- coding: utf-8 -*-

from core.mysql import Mysql


class Base(object):
    def __init__(self, dbName, tableName):
        self._conn = Mysql(dbName)
        self._tableName = tableName

    def getData(self, sql=None, kind=None, count=None):
        conn = self._conn
        if sql is None:
            sql = """SELECT * FROM %s""" % (self._tableName)
        result = conn.select(sql=sql, kind=kind, count=count)
        return result

    def insertData(self, data,kind =None, if_exists='append', chunksize=None):
        conn = self._conn
        conn.insert(data, table=self._tableName, kind=kind, if_exists=if_exists, chunksize=chunksize)
        pass


if __name__ == '__main__':
    B = Base('biying', 'new')
    print(B.getData())