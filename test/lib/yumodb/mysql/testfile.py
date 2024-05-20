from lib.yumodb.mysql.workbench import WorkBench
from lib.yumodb.mysql.basic.connector import Connector
from lib.yumodb.mysql.basic.information import Information
from lib.yumodb.mysql.dispose.construction import Construction
from lib.yumodb.mysql.dispose.formation import FormatPackage
from lib.yumodb.mysql.dispose.check import Check
from lib.yumodb.mysql.err.log import LogManger


class TestClient:
    client = WorkBench("test_db")  # 连接客户端, 指定库 test_db 启动
    connector = Connector()
    information = Information()
    construction = Construction()
    formation = FormatPackage()
    check = Check()
    log = LogManger("test_client", ".yumodb.mysql.test_client")

    def test_Client(self, nodb=False):
        if nodb:
            self.client = WorkBench()
            self.client.use("test_db")

        print("\nTEST CLIENT\n")

        print("test context manger")
        with WorkBench("test_db") as client:
            # 测试客户端show功能
            result = client.show(isDB=False)
            print("result:", result)

        # 创建 ‘test_1’ 表 属性： id, name, age | PS: 不指定特殊键
        self.client.ctb("test_1", {"id": "int", "name": "varchar(255)", "age": "int"})

        # 创建 ‘test_2’ 表 属性： id, name, age | PS: 指定id为主键（primary）， 指定name为唯一键（unique）
        self.client.ctb("test_2", {'id': 'int', 'name': 'varchar(255)', 'age': 'int'},
                        primary="id", unique="name")

        """
        create table test result:
            ~ 为指定数据库前，无法创建表
            ~ 数据库无法再次创建同名表
        
        优化目标：
            添加err捕获功能 —— 定位异常位置
            在未指定数据时应该执行什么操作
        """

        print("test_insert data")
        # 获取测试数据
        td1, td2, ts1, ts2 = self.getInsertData()
        # self.client.insert("test_1", [], ignore=False)
        self.client.insert("test_2", td1, ignore=True)
        self.client.insert("test_2", td2, ignore=True)
        self.client.insert("test_2", ts1, ignore=True)
        self.client.insert("test_2", ts2, ignore=True)
        """
        测试结果：
            格式数据时需要考虑 四种情况 字典格式插入单条数据， 元祖格式插入单条数据， 字典格式插入多条数据， 元祖格式插入多条数据
            标准化数据格式： 字典， 可迭代容器
        """

        print("test_update")
        self.client.update("test_2", {'id': [1, 2, 3], 'name': ["yunximoran", "yumonotes", "杨天华"], "age": [18, 20, 22]})
        self.client.update("test_2",
                           vals=(4, "云曦墨染", 232),
                           keys=('id', 'name', "age")
                           )
        self.client.update("test_2",
                           vals=((4, "云曦墨染", 232), (5, "花前月下", 118)),
                           keys=('id', 'name', "age")
                           )

        print("test delete")
        self.client.delete("test_2", id=1)

        print("test_select")
        result = self.client.select("test_2", "age", condition="id = 2")
        print(result)
        print("using db", self.client.getUsingDB())
        self.client.init()
        print("using db", self.client.getUsingDB())

        self.client.close()

    def test_Connector(self):
        pass

    def test_Information(self):
        print("\nTEST INFORMATION\n")
        databases = self.information.getDataBases()
        tables = self.information.getTables("test_db")
        columns, num = self.information.getColumns('test_db', 'test_2')
        counts = self.information.getCounts('test_db', 'test_1')

        print("databases", databases)
        print("tables", tables)
        print(f"columns: {columns}\nnum: {num}")
        print("count:", counts)

    def test_Construction(self):
        print("\n==== 测试语句 ====\n")

        ndb = self.construction.ndb("test", isExists=True)
        print(ndb)

        ntb = self.construction.create("test", {"id": "int", "name": "varchar(255)", "age": "int"}, primary="id",
                                       unique="name")
        print(ntb)

        show = self.construction.show()
        print(show)

        drop = self.construction.drop("test2", isExists=True)
        print(drop)

        insert = self.construction.insert("test2", (1, 'name', 18), ("id", "name", "age"), ignore=True)
        print(insert)

        select = self.construction.select("test2", fondKey=('name', "age"))
        print(select)

        update = self.construction.update("test2", ("test", 18), ("name", "age"), "id=1")
        print(update)

        delete = self.construction.delete("test2", "id=1")
        print(delete)

    def test_formation(self):
        testDict = {
            'id': [1, 2, 3, 4, 5],
            'name': ["Y", "T", "H", "X", "M"],
            'age': [18, 20, 21, 19, 18]
        }
        testSeries = [[1, "Y", 18], [2, "T", 20], [3, "H", 21], [4, "X", 19], [5, "M", 18]]
        resultDict = self.formation.formatDict(testDict)
        resultSeries = self.formation.formatSeries(testSeries)
        print("result\t Dict:", resultDict)
        print("result\t Series:", resultSeries)

    def test_Check(self):
        print("\nTEST CHECK\n")

        testData = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]
        print("test success data")
        print("result:\t", self.check.checkLen(testData))

        print("\n")
        testData = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4],
            [1, 2, 3]
        ]
        print("test error data")
        print("result:\t", self.check.checkLen(testData))

        print("test check KeyValNumEquality", self.check.checkKeyValNumEquality('test_db', 'test_1', 3))
        print("test check KeyValNumEquality", self.check.checkKeyValNumEquality('test_db', 'test_1', 4))

        tu1 = [1, "Y", 22]
        tu2 = [
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
        ]
        tu3 = [
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1, "Y", 22],
            [1.22, 22, "Y"],
        ]
        print("test check Uniformity", self.check.checkUniformity(tu1))
        print("test check Uniformity", self.check.checkUniformity(tu2))
        print("test check Uniformity", self.check.checkUniformity(tu3))

        res1 = self.check.isPRI('test_db', 'test_2', 'id')
        res2 = self.check.isUNI('test_db', 'test_2', 'name')
        print("id is PRI", res1)
        print("name is UNI", res2)

    def test_LogManger(self):
        print("\nTEST LOG\n")
        self.log.getDebug("test debug log")
        self.log.getInfo("test info log")
        self.log.getWarning("test warning log")
        self.log.getError("test error log")
        self.log.getCritical("test critical log")

    def test_python(self):
        print(self.is_nested_container([1, 2, [3, 4]]))  # True
        print(self.is_nested_container([1, 2, [3, 4]]))  # True
        print(self.is_nested_container([1, 2, [3, 4]]))  # True
        print(self.is_nested_container([1, 2, 3, 4]))  # True

        test_1 = [1, 2, 3, 4]
        test_2 = (1, 2, 3, 4)
        test_3 = {
            1: 1,
            2: 2,
            3: 3,
            4: 4
        }
        print(isinstance(test_1, (dict, tuple, list)))
        print(isinstance(test_2, (dict, tuple, list)))
        print(isinstance(test_3, (dict, tuple, list)))

        for i in "云溪默然":
            print(i)

        tdict_1 = {
            "id": 1,
            "name": "yumonotes",
            "age": 18
        }
        print(tuple(tdict_1.values()))

    @staticmethod
    def getInsertData():
        tdict_1 = {
            "id": 1,
            "name": "yumonotes",
            "age": 18
        }

        tdict_2 = {
            'id': [1, 2, 3, 4, 5],
            'name': [
                "Y",
                "T",
                "H",
                "X",
                "M"],
            'age': [18, 20, 21, 19, 18]
        }
        tseries_1 = [1, "yumonotes", 18]
        tseries_2 = [
            [1, "Y", 18],
            [2, "T", 20],
            [3, "H", 21],
            [4, "X", 19],
            [5, "M", 18]
        ]
        return tdict_1, tdict_2, tseries_1, tseries_2

    @staticmethod
    def is_nested_container(obj):
        if isinstance(obj, (list, tuple, set, dict)):
            if all(isinstance(sub_obj, (list, tuple, set, dict)) for sub_obj in obj):
                return True
        return False
