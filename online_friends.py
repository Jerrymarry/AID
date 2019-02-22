# -*- coding: utf-8 -*-
import web
import time
import redis

r = redis.StrictRedis(host="127.0.0.1",port=6379)

"""
配置路由规则
"/":   模拟用户的访问
"/online": 查看在线用户
"""
urls = (
    "/","visit",
    "/online","online"
)

app = web.application(urls,globals())

"""
返回当前时间对应的键名
如28分对应的键名是active.users:28
"""
def time_to_key(currrent_time):
    return "active.users:" + time.strftime("%M",time.location(current_time))
# time strftime() 函数接收以时间元组,并返回以可读字符串表示的当地时间,格式由参数format决定
# time.strftime(format[, t])
# format -- 格式字符串。
# t -- 可选的参数t是一个struct_time对象。
"""
返回最近10分钟的键名
结果是列表类型
"""
def keys_in_last_10_minutes():
    now = time.time()
    result = []
    for i in range(10):
        result.append(time_to_key(now - i*60))
    return result