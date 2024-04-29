import os

specialList = [
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__"
]


class BuildDir:
    workDir = os.getcwd()  # 获取工作目录 -> 根目录
    baseName = os.path.basename(workDir)

    def __init__(self, substructures):
        """
            搭建 项目结构
        :param substructures: 项目 底层结构
        """
        self.substructures = substructures
        self.start(self.workDir)

    def start(self, currentDir):
        """

        :param currentDir: 当前目录
        :return:
        """
        sunDirList = [self.getAbsolutePath(currentDir, sun) for sun in os.listdir(currentDir) if
                      (sun not in self.substructures) and os.path.isdir(self.getAbsolutePath(currentDir, sun))]
        """
            sunDirList: 只能存放 底层结构目录之外的文件
        """
        # 怎么判断是否继续遍历下一级目录

        if not sunDirList and currentDir != self.workDir:
            self.building(currentDir)
        else:
            for sunDir in sunDirList:
                self.start(sunDir)

    @staticmethod
    def getAbsolutePath(head, rear):
        return os.path.join(head, rear)

    def building(self, currentDir):
        os.open(f"{currentDir}/yumo.py", os.O_CREAT | os.O_WRONLY)
        for elem in self.substructures:
            elem_path = self.getAbsolutePath(currentDir, elem)
            if not os.path.exists(elem_path):
                os.makedirs(elem_path)

    def OutTreeFrame(self, currentDir=workDir, level=0):
        OutFormat = ''.join(['\t' * level])

        if currentDir == self.workDir:
            print(self.baseName)
        sunElemList = os.listdir(currentDir)  # 获取当前目录子元素列表
        if sunElemList:
            for sun in sunElemList:
                if sun in specialList:
                    continue
                sun_path = self.getAbsolutePath(currentDir, sun)
                print(OutFormat + sun)
                if os.path.isdir(sun_path):
                    self.OutTreeFrame(sun_path, level + 1)
        else:
            pass

    def build_md(self):
        pass

