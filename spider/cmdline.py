import scrapy.cmdline

if __name__ == '__main__':
    #scrapy.cmdline.execute(argv=['scrapy','crawl','dmoz'])
    # scrapy.cmdline.execute("scrapy crawl by --nolog".split())
    scrapy.cmdline.execute("scrapy crawl by".split())