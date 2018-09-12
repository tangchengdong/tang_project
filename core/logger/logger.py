# -*- coding: utf-8 -*-

import logging
import os


# 方法一：
# 输出格式
LOG_FORMAT = "%(asctime)s- %(lineno)s,  %(levelname)s,  - %(message)s"
# 输出时间格式
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# filename 输出指定文件，没有指定文件名就不会写到文件里，而是打印（二选一）
# level  设置日志最低级别输出，低于设置级别就不会输出（以下是从上到下，级别从小到高）
# format 格式化格式
# log = logging.basicConfig(filename='error.log', level=logging.INFO, format=LOG_FORMAT)
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")


# 方法二：

# 输出格式
# LOG_FORMAT = "%(asctime)s- %(lineno)s,  %(levelname)s,  - %(message)s"
# # 输出时间格式
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# log = logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
# logger = logging.getLogger(__name__)
# logger.info('Start reading database')
# name = os.path.join(os.path.dirname,)


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class Loggl():
    def __init__(self,name = None):
        if name is not None:
            LOG_FORMAT = "{}   {}%(asctime)s,   {}%(lineno)s{},  {}%(message)s ".format(name, "time:", "in:", " line", "error in:")
        else:
            # 输出格式
            LOG_FORMAT = "{}%(asctime)s,   {}%(lineno)s{},  {}%(message)s ".format("time:", "in:", " line", "error in:")
        # 输出时间格式
        # DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
        DATE_FORMAT = "%m/%d/%Y %H:%M:%S "
        self.log = logging.basicConfig(filename='%s/error.log' % PATH, level=logging.INFO, format=LOG_FORMAT)
        self.logger = logging.getLogger(__name__)
        # logger.info('Start reading database')


if __name__ == '__main__':
    print()
    # 异常的所在的行数
    # try:
    #     a+2
    # except:
    #     s = sys.exc_info()
    #     print(s)
    # print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
    pass

# 使用说明：
# from core.logger import Loggl
# log = Loggl(name =__file__ )
# try:
#     pass
# except Exception as e:
#     log.logger.error('%s'%e)