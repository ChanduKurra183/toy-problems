import LRU_Cache

class LruTest:
    def testcases(self):

        a = lru(2)
        a.put("social_media")
        assert a.get("social_media") == "1"
        print("Testcase passed..!")

        a.put("browser")
        assert a.get("browser") == "2"
        print("Testcase passed..!!")
        print("<< All testcases passed >>")

        lis = a.get_cache()
        for i in lis:
            print(i)

if _name_ == '_main_':
    a = LruTest()
    a.testcases()