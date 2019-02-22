import redis
# 设置数据库连接对象
pool = redis.ConnectionPool(host="127.0.0.1",port="6379",decode_responses=True)
r = redis.StrictRedis(connection_pool=pool)
# 设置发布订阅对象
p = r.pubsub()

# 订阅频道cctv1
p.subscribe("cctv1")

# #监听状态：有消息发布了就拿过来
# l = p.listen()  # 返回值为可迭代对象:
#
# # item数据结构为字典:
# # {'pattern': None, 'type': 'message', 'channel':'频道', 'data':'消息内容'}
# for item in l:
#     # print(item)
#     # 第一次会返回订阅确认信息
#     # {'channel': 'cctv1', 'type': 'subscribe', 'pattern': None, 'data': 1}
#     if item["type"] == "message":
#         data = item["data"]
#         print("从{}收到消息:{}".format(item["channel"],data))
#         if data == "over":
#             print(item["channel"],"停止发布")
#             break
# p.unsubscribe("cctv1")
# print("取消订阅")


msg=p.parse_response()#第一次会返回订阅确认信息
print(msg)
print("订阅成功，开始接收------")
while True:
    msg=p.parse_response()#接收消息
    if msg[2] == "over":
        break
    print("收到消息:",msg[2])#此处的信息格式['消息类型', '频道', '消息']，所以使用[2]来获取