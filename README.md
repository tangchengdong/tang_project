# 文件结构说明

* Crawl_Python3.5/bin/   定时任务执行代码目录
* Crawl_Python3.5/config-default.json   定时任务时间配置
* Crawl_Python3.5/core/config/\__init__.py   数据库配置文件读取
* Crawl_Python3.5/core/config/db.default.yaml   正式服数据库配置
* Crawl_Python3.5/core/config/db.yaml   本机测试数据库配置
* Crawl_Python3.5/core/data/db   爬虫初始化基类
* Crawl_Python3.5/Crawl_Python3.5/middlewares.py   爬虫中间件
* Crawl_Python3.5/Crawl_Python3.5/middlewares.py   爬虫设置
* Crawl_Python3.5/doc   爬虫中所用到的知识文档，欢迎大家就新技术写文档补充（推荐使用markdown记录）

# 框架使用说明
1. 在db.yaml或者db.default.yaml配置数据库地址
2. 在Crawl_Python3.5/core/data/db文件夹下初始化基类
3. 在Crawl_Python3.5/Crawl_Python3.5/items.py配置将要爬取的数据元素
4. 在Crawl_Python3.5/Crawl_Python3.5/pipelines.py配置处理数据的管道函数
5. 在Crawl_Python3.5/Crawl_Python3.5/Crawl_Python3.5s文件夹下开始写Crawl_Python3.5的解析代码
6. 在Crawl_Python3.5/bin文件夹下写定时任务
7. 在Crawl_Python3.5/config-default.json下写定时任务运行时间

*注意：请保持db.default.yaml、Crawl_Python3.5/core/data/db、Crawl_Python3.5/Crawl_Python3.5/Crawl_Python3.5s这三个文件或者代码中命名一致，这样的话直接可以将数据转换成pandas格式存到数据库*

# 项目部署

* 基于node.js + pm2进行进程管理
* 进入部署目标服务器Crawl_Python3.5/bin/下，运行"pm2 start my-python-script.py(替换文件) -x --interpreter python"
                    pm2 start scrapy_biying_ask.py -x --interpreter C:\Users\Dell\Envs\crawler\Scripts\python
* 用pm2 list查看即可

*注意：部署前最好现在服务器上手动测试一下，确认没问题再部署*

