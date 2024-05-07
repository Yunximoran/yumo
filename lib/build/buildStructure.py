import os

specialList = [
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__"
]


class BuildStructure:
    """
        项目结构构建工具
    """
    workDir = os.getcwd()  # 获取工作目录绝对路径 -> 根目录
    baseName = os.path.basename(workDir)  # 获取当前目录名称
    dirLevel = [baseName]

    projectFrame = {}

    def __init__(self,
                 substructures=None,
                 mode=None
                 ):
        """
            搭建 项目结构
        :param substructures: 项目 底层结构
        """
        self.substructures = substructures
        # self.start(self.workDir)
        pass

    def buildDir(self, currentDir):
        """

        :param currentDir: 当前目录
        :return:
        """
        sonDirList = [os.path.join(currentDir, son) for son in os.listdir(currentDir) if
                      (son not in self.substructures) and os.path.isdir(os.path.join(currentDir, son))]
        """
            sonDirList: 只能存放 底层结构目录之外的文件
        """
        # 怎么判断是否继续遍历下一级目录

        if not sonDirList and currentDir != self.workDir:
            self.building(currentDir)
        else:
            for sonDir in sonDirList:
                self.buildDir(sonDir)

    def building(self, currentDir):
        with open(f'{currentDir}/yumo.py', 'w') as f:
            pass
        for elem in self.substructures:
            elem_path = os.path.join(currentDir, elem)
            if not os.path.exists(elem_path):
                os.makedirs(elem_path)

    def OutTreeFrame(self, start=workDir, frame=None, dump=False):  # 这里获取应该是当前层级
        """
            输出项目树结构
        :param start:  开始目录
        :param frame: 存储数据
        :param dump: 是否保存到本地
        
        :type frame: dict
        :return: 项目结构
        """
        if frame is None:
            frame = {}

        elemList = os.listdir(start)
        for elem in elemList:
            if elem in specialList:
                continue
            path = os.path.join(start, elem)
            if os.path.isdir(path):
                frame[elem] = {}  # 基于当前目录创建新的字元素
                self.OutTreeFrame(path, frame[elem])

            else:
                if 'file' not in frame:
                    frame['file'] = [elem]
                else:
                    frame['file'].append(elem)
        if start == self.workDir:
            return {self.baseName: frame}


tJson = {
    "d1": {
        "d2": {},
        "d3": {},
        "d4": {},
        "file": {}  # 可以用集合， 同一目录不会出现后缀名一样的同名文件
        # 问题在怎么定位当前层级
    }
}
