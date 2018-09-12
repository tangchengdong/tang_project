#-*-coding:utf8-*-


import sys
import os
import json
from apscheduler.schedulers.blocking import BlockingScheduler

sys.path.append('..')
scheduler = BlockingScheduler()


#读取配置信息
BASEPATH = os.path.dirname(__file__)
data = open(os.path.join(BASEPATH, '../config.json'), 'r')
config = json.load(data)
data.close()


@scheduler.scheduled_job("cron", hour=config['task']['biying']['hour'], minute=config['task']['biying']['minute'])
def updateRong360Rate():
    """
    测试定时任务
    """
    os.system('scrapy crawl by')  # 执行爬虫命令


if __name__ == '__main__':
    try:
        print('task start')
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

