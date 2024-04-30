import os


__all__ = ['BuildDir']

specialList = [
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__"
]


class BuildDir:
    workDir = os.getcwd()  # 获取工作目录 -> 根目录
    baseName = os.path.basename(workDir)
    f = open(f"{os.path.basename(workDir)}.txt", 'w')

    def __init__(self, substructures):
        """
            搭建 项目结构
        :param substructures: 项目 底层结构
        """
        self.substructures = substructures
        # self.start(self.workDir)
        self.OutTreeFrame()

    def start(self, currentDir):
        """

        :param currentDir: 当前目录
        :return:
        """
        sonDirList = [self.getAbsolutePath(currentDir, son) for son in os.listdir(currentDir) if
                      (son not in self.substructures) and os.path.isdir(self.getAbsolutePath(currentDir, son))]
        """
            sonDirList: 只能存放 底层结构目录之外的文件
        """
        # 怎么判断是否继续遍历下一级目录

        if not sonDirList and currentDir != self.workDir:
            self.building(currentDir)
        else:
            for sonDir in sonDirList:
                self.start(sonDir)

    @staticmethod
    def getAbsolutePath(head, rear):
        return os.path.join(head, rear)

    def building(self, currentDir):
        self.addFile('yumo.py', currentDir)
        # os.open(f"{currentDir}/yumo.py", os.O_CREAT | os.O_WRONLY)
        for elem in self.substructures:
            elem_path = self.getAbsolutePath(currentDir, elem)
            if not os.path.exists(elem_path):
                os.makedirs(elem_path)

    def OutTreeFrame(self, currentDir=workDir, level=0):
        OutFormat = ''.join(['  |' * level])
        if currentDir == self.workDir:
            print(self.baseName)
            self.f.write(self.baseName + "\n")
        sonElemList = os.listdir(currentDir)  # 获取当前目录子元素列表
        if sonElemList:
            for son in sonElemList:
                if son in specialList:
                    continue
                son_path = self.getAbsolutePath(currentDir, son)
                print(OutFormat + son)
                self.f.write(OutFormat + son + "\n")
                if os.path.isdir(son_path):
                    self.OutTreeFrame(son_path, level + 1)

    def addFileInAllDir(self, filename, currentDir=workDir):
        """
            在所有目录下创建文件
        :param currentDir:
        :param filename:
        :return:
        """
        pass
        # sonElemList = os.listdir(currentDir)
        # if not sonElemList:
        #     return
        #
        # if 'yumo.py' in sonElemList:
        #     self.addFile(filename, currentDir)
        # else:
        #     for son in sonElemList:
        #         son_path = self.getAbsolutePath(currentDir, son)
        #         if os.path.isdir(son_path):
        #             self.addFileInAllDir(filename, currentDir)
        #         else:
        #             pass

    @staticmethod
    def addFile(filename, path=workDir):
        """ 添加文件 """  # 在当前目录下添加文件
        os.open(f"{path}/{filename}", os.O_CREAT | os.O_WRONLY)
