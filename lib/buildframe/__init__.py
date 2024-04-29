import os


# ?.global:

class BuildDir:
    workDir = os.getcwd()  # 获取工作目录 -> 根目录

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
                      (sun not in self.substructures) and os.path.isdir(os.path.join(currentDir, sun))]
        """
            sunDirList: 只能存放 底层结构目录之外的文件
        """
        # 怎么判断是否继续遍历下一级目录

        if not sunDirList and currentDir != self.workDir:
            self.building(currentDir)
        else:
            for sunDir in sunDirList:
                self.start(sunDir)

    # @staticmethod # 怎么办好像不需要 这个
    # def isAnyDir(PathList):
    #     """
    #         判断子元素列表是否都是dir
    #     :param PathList:
    #     :return:
    #
    #     demo2:  # 第二种方案，如果子元素中存在dir则返回True
    #
    #         for path in PathList:
    #             if os.path.isdir(path):
    #                 return True
    #
    #         return False
    #
    #     """
    #     return any(path for path in PathList if os.path.isdir(path))

    @staticmethod
    def getAbsolutePath(head, rear):
        return os.path.join(head, rear)

    def building(self, currentDir):
        os.open(f"{currentDir}/yumo.py", os.O_CREAT | os.O_WRONLY)
        for elem in self.substructures:
            elem_path = self.getAbsolutePath(currentDir, elem)
            if not os.path.exists(elem_path):
                os.makedirs(elem_path)


"""
从当前目录开始遍历子元素

判断哪些是dir属性
判断dir是否为空， 是 -> 创建新目录， 否 —> 遍历该目录子元素， 是否存在dir -> 
"""
