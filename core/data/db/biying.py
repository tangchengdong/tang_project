# -*- coding: utf-8 -*-
from core.data.db.sqlbase import Base
import os

# 获取当前模块名,做为db.default.yaml 键名
tableName = os.path.basename(__file__).split('.')[0]


class Biying(Base):
    def __init__(self):
        # 初始化父类,把数据库名和表名传进去，self.__class__.__name__ 获取类名
        super(Biying, self).__init__(tableName, self.__class__.__name__)

if __name__ == '__main__':
    pass