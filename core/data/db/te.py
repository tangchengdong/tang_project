# -*- coding: utf-8 -*-
import re



a = 'https://bing.ioliu.cn/photo/DragonflyMacro_EN-AU9950962027?force=download'

b = re.findall(r'.*/(.*)\?force=download', a)[0]
print(b)