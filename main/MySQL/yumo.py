from lib.yumodb.mysql.workbench import WorkBench

with WorkBench() as ud:
    dbn = "yumo"

    ud.use(dbn)

    usingDB = ud.getUsingDB()
    print("using db is ", usingDB)  # OUT: UsingDB

    tbn = 'yuanshen'
    ud.ctb(tbn,
           {
               'uid': 'int',
               'name': 'varchar(255)',
               'day': 'datetime',
               'level': 'float'},
           primary='uid',
           unique='name',
           )

    version = ud.version()
    print(f"mysql run success version: {version}")
