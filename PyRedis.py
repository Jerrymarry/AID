import redis,time

r = redis.StrictRedis(host="127.0.0.1",port=6379)

# 1.hmset/hgetall
# hmset支持将字典作为参数存储,同时hgetall的返回值也是一个字典
r.hmset("dict",{"name":"Bob","age":18})
p = r.hgetall("dict")
print(p)       # {b'age': b'18', b'name': b'Bob'}

# 2.管道(pipeline)
pipe = r.pipeline()
pipe=r.pipeline(transaction=True)

pipe.set('p1','v2')
pipe.set('p2','v3')
pipe.set('p3','v4')
time.sleep(5)
result = pipe.execute()
print(result)

# 3.事务 python中可以使用管道来代替事务：
pipe=r.pipeline()
try:
    # pipe.watch('a')
    pipe.multi()
    pipe.set('here', 'there')
    pipe.set('here1', 'there1')
    pipe.set('here2', 'there2')
    # time.sleep(5)
    pipe.execute()

except redis.exceptions.WatchError as e:
    print("Error")




