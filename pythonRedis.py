import redis 
# r = redis.StrictRedis(host="127.0.0.1",port=6379)

# # 测试连接
# user1 = r.get("user1")
# print(user1) # None


class TestString():
    def __init__(self):
        self.r = redis.StrictRedis(host="127.0.0.1",port=6379)

    def test_set(self):
        rset = self.r.set("user2","Amy")
        print(rest)
        return rest

    def test_get(self):
        rest = self.r.get("user2")
        print(rest)
        return rest   

    def test_mset(self):
        d = {
            "user3":"Bob",
            "user4":"Bobx"
        }
        rest = self.r.mset(d)
        print(rest)
        return rest 

    def test_mget(self):
        L = ["user3","user4"]
        rest = self.r.mget(L)
        print(rest)
        return rest

    def test_del(self):
        rest = self.r.delete("user3")
        print(rest)
        return rest

def main():
    str_obj = TestString()
    # str_obj.test_set()
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    str_obj.test_del()

if __name__ == "__main__":
    main()