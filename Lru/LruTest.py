from LRU_Cache import LRU_Cache

class LruTest:
    def testcases(self):

        a = LRU_Cache(2)
        a.put("social_media")
        assert a.get("social_media") == "social_media","Testcase  failed"
        print("Testcase passed..!")

        a.put("browser")
        assert a.get("browser") == "browser","Testcase  failed"
        print("Testcase passed..!!")
        print("<< All testcases passed >>")

        lis = a.get_cache()
        for i in lis:
            print(i)

if __name__ == "__main__":
    a = LruTest()
    a.testcases()