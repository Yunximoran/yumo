import os
import json

specialList = [
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__"
]   # python代码中一些比较特殊的包


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

    def building(self, currentDir, substructures):
        """
            构建项目底层结构
        :param currentDir: 当前目录
        :param substructures: 构建目标列表
        :return:
        """
        sonDirList = [os.path.join(currentDir, son) for son in os.listdir(currentDir) if
                      (son not in substructures) and os.path.isdir(os.path.join(currentDir, son))]
        """
            sonDirList: 只能存放构建目标之外的目录
        """
        # 怎么判断是否继续遍历下一级目录

        if not sonDirList and currentDir != self.workDir:
            self.__building(currentDir, substructures)
        else:
            for sonDir in sonDirList:
                self.building(sonDir, substructures)

    @staticmethod
    def __building(currentDir, substructures):
        """

        :param currentDir:
        :return:
        """
        os.open(f"{currentDir}/yumo.py", os.O_CREAT | os.O_WRONLY)
        for elem in substructures:
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
            if dump:
                with open("yumo.json", "w", encoding='utf-8') as f:
                    json.dump(frame, f, indent=4, ensure_ascii=False)

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
