# -*- coding:utf-8 -*-
import sys
import os
from chardet import detect

p = '中文'
print p
env = os.environ
print env['TMP']
print detect(str(env['TMP']))    #可以用detect确定字符的编码，用于解决编码问题
print str(env['TMP']).decode('gbk')
