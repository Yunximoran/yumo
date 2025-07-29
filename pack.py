import sys
import subprocess
import platform

from pathlib import Path
from typing import List

# 打包类

class Pack:
    """ # Pyinstaller 帮助文档
    usage: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                    [--add-data <SRC;DEST or SRC:DEST>]
                    [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                    [--hidden-import MODULENAME] [--collect-submodules MODULENAME]
                    [--collect-data MODULENAME] [--collect-binaries MODULENAME]
                    [--collect-all MODULENAME] [--copy-metadata PACKAGENAME]
                    [--recursive-copy-metadata PACKAGENAME]
                    [--additional-hooks-dir HOOKSPATH] [--runtime-hook RUNTIME_HOOKS]
                    [--exclude-module EXCLUDES] [--splash IMAGE_FILE]
                    [-d {all,imports,bootloader,noarchive}]
                    [--python-option PYTHON_OPTION] [-s] [--noupx] [--upx-exclude FILE]
                    [-c] [-w]
                    [-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">]       
                    [--disable-windowed-traceback] [--version-file FILE]
                    [-m <FILE or XML>] [--no-embed-manifest] [-r RESOURCE]
                    [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                    [--win-no-prefer-redirects] [--argv-emulation]
                    [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                    [--target-architecture ARCH] [--codesign-identity IDENTITY]
                    [--osx-entitlements-file FILENAME] [--runtime-tmpdir PATH]
                    [--bootloader-ignore-signals] [--distpath DIR]
                    [--workpath WORKPATH] [-y] [--upx-dir UPX_DIR] [-a] [--clean]        
                    [--log-level LEVEL]
                    scriptname [scriptname ...]
    
    # 常规选项
    --help          -h:         显示帮助信息
    --version      -v:         显示版本信息
    --distpath                  生成可执行文件目录
    --noconfirm -y:         覆盖输出目录
    --workpath: 临时文件存放目录
    --upx-dir: 设置UPX工具目录 默认搜索UPX
    -a, --ascii: 不包含Unicode编码支持
    --clean: 清理临时文件并退出
    --log-level: 设置日志级别 默认INFO

    # 生成选项
    -D, --onedir: 生成一个目录，包含可执行文件和依赖
    -F, --onefile: 生成单个可执行文件
    --specpath: 指定xxx.spec文件存放目录（默认当前目录）
    -n, --name: 设置生成的可执行文件或者目录名称（默认第一个脚本文件名）
    --add-data: 添加数据文件或者目录
    --add-binary: 添加二进制文件（ xxx.so & xxx.dll ）
    -p, --paths: 添加模块搜索路径
    --hidden-import, --hiddenimport: 添加隐式导入的模块
    --additional-hooks-dir: 添加额外的钩子目录
    --runtime-hook: 添加运行时的钩子脚本
    --exclude-mudule: 排除指定的模块
    --key: 用于加密Python字节码的密钥    
    --collect-submodules: 搜索指定模块的所有子模块
    --collect-data, --collect-datas: 搜集指定模块的数据
    --collect-binaries: 收集指定模块的二进制文件
    --collect-all: 收集指定模块的所有数据、二进制文件、子模块

    # 生产过程选项
    -d, --debug: 生成调试版本的可执行文件（对于Windows，会禁用控制台重定向并打印调试信息）
    --python-option: 向Python解释器传递参数
    -s,strip: 对于可执行文件和共享库进行strip(移除符号表)
    --noupx: 禁用UPX压缩
    --upx-exclude: 使用UPX排除指定文件，可使用通配符

    # Windows 
    --version-file 添加版本信息文件 （.rc）
    -m, --manif 添加manifest文件（XML格式）
    -r, --resource 向windows可执行文件添加或更新资源

    --uac-admin 创建一个Manifest, 该Manifest将在程序启动时请求提升
    --uac-uiacc 运行升级的应用程序使用远程桌面
  
    --hide-console: 当程序运行时隐藏控制台（只对窗口模式有效）


    # MAC & Windows 特有参数
    -c, --console, --nowindowed: 控制台模式
    -w, --windowed, --noconsole: 窗口模式（不显示控制台）
    -i, --icon

    """

    # 执行器配置
    __argv__ = ["pyinstaller"]

    # 默认选项
    __spec__ = Path("static/pack/__spec__")     # 工作目录会切换到spec文件所在目录中
    __dist__ = Path("static/pack/__dist__")
    __work__ = Path("static/pack/__work__")

    # {DEBUG, INFO, WRAN, ERROR}
    LOG_DEBUG = "DEBUG"
    LOG_WRAN = "WRAN"
    LOG_INFO = "INFO"
    LOG_ERROR = "ERROR"

    # {all,imports,bootloader,noarchive}
    DEBUG_MOTHED_ALL = "all"
    DEBUG_MOTHED_IMPORT = "import"
    DEBUG_MOTHED_BOOTLOADER = "bootloader"
    DEBUG_MOTHED_NOARCHIVE = "noarchive"

    
    def __init__(self,
            script:Path,                # 打包文件
            *,
            # 常规属性
            name:str=None,              # 输出名称: -n, --name: 设置生成的可执行文件或者目录名称（默认第一个脚本文件名）
            clean:bool=False,
            isone:bool=False,           # 单目录 & 单文件 [-D --onedir & -F --onefile] PS: -D, --onedir: 生成一个目录，包含可执行文件和依赖, -F, --onefile: 生成单个可执行文件
            icon:Path=None,             # 设置图标路径（windows & Mac OS）
            show:bool=True,             # -c [控制台模式] & -w [窗口模式]
            # 工作模式
            confirm:bool=True,          # 覆盖输出: -y, -noconfirm: 覆盖输出目录
            ascii:bool=True,            # 禁用Unicode编码支持: -a, ascii: 不包含Unicode编码支持
            debug:bool=False,           # -d, --debug: 生成调试版本的可执行文件（对于Windows，会禁用控制台重定向并打印调试信息）
            # loglevel:bool=False,      # --log-level: 设置日志级别 默认INFO
            strip:bool=False,           # -s,strip: 对于可执行文件和共享库进行strip(移除符号表)
            noupx:bool=False,           # --noupx: 禁用UPX压缩
            # 输出配置
            dist:Path=None,             # --distpath: 生成可执行文件目录 (./static/pack/__dist__)
            spec:Path=None,             # --specpath: 指定xxx.spec文件存放目录（默认当前目录）(./static/pack__spec__)
            work:Path=None,             # --workpath: 临时文件存放目录 (./static/pack/__work__)
            # 依赖配置
            # upxpath:Path=None,        # UPX路径
            datas:List[Path]=[],        # 额外的资源文件: --add-data: 添加数据文件或者目录
            binaries:List[Path]=[],     # 额外的代码: --add-binary: 添加二进制文件（ xxx.so & xxx.dll ）
            hiddens:List[str]=[],       # 额外的PY库: --hidden-import, --hiddenimport: 添加隐式导入的模块
            excludes:List[str]=[],      # 需要排除的 module: --exclude-mudule: 排除指定的模块
            paths:List[Path]=[],        # 额外的搜索路径: -p, --paths: 添加模块搜索路径
            hookpaths:List[Path]=None,  # 额外的钩子: --additional-hooks-dir: 添加额外的钩子目录
            runhooks:List[Path]=None,   # 运行时的钩子脚本: --runtime-hook: 添加运行时的钩子脚本
        ):
        # 场景一，在根目录中应用
        # 场景二，打包子项目， 可能需要设置工作目录
        # vscode工作目录一定时根目录

        # 区分操作系统，设置 sep
        self.script = self.__check_path__(script, check=True)

        self.__os__ = platform.system()
        if self.__os__ == "Linux":
            self.__sep__ = ":"

        else:
            # Windows & MacOS
            self.__sep__ = ";"
            if show: self.__argv__.append("-c")
            else: self.__argv__.append("-w")

            if icon:    # 设置图标路径， 可用
                icon = self.__check_path__(icon, check=True)
                self.__argv__.append("--icon={}".format(icon.absolute()))

            if self.__os__ == "Windows":
                # Windows Options
                pass
            
            if self.__os__ == "MacOS":
                # MacOS Options
                pass


        if isone: self.__argv__.append("--onefile")
        else: self.__argv__.append("--onedir")    

        if name: self.__argv__.append("--name {}".format(name))
        if clean: self.__argv__.append("--clean")
        if confirm: self.__argv__.append("--noconfirm")
        if debug: self.__argv__.append("--debug all")
        if strip: self.__argv__.append("--strip")
        if noupx: self.__argv__.append("--noupx")

        # 设置输出路径
        if dist: self.__dist__ = self.__check_path__(dist, check=True)
        self.__argv__.append("--distpath {}".format(self.__dist__)) 

        if spec: self.__spec__ = self.__check_path__(spec, check=True)
        self.__argv__.append("--specpath {}".format(self.__spec__))
        
        if work: self.__work__ = self.__check_path__(work, check=True)
        self.__argv__.append("--workpath {}".format(self.__work__))


        # 禁用Unicode编码支持
        if not ascii: self.__argv__.append("--ascii")

        # 资源相关
        if datas: self.__argv__.append(self.__datas__(datas))
        if binaries: self.__argv__.append(self.__binaries__(binaries))

        # 模块相关
        if hiddens:self.__argv__.append(self.__hiddens__(hiddens))  
        if excludes:self.__argv__.append(self.__exclude_module__(excludes))
        if paths:self.__argv__.append(self.__paths__(paths))
        
        # 钩子相关
        if hookpaths:self.__argv__.append(self.__hook_dirs__(hookpaths))
        if runhooks: self.__argv__.append(self.__hook_path__(runhooks))
            
        self.__argv__.append(str(self.script))
        self.__execute__()

    def __execute__(self):
        subprocess.run(" ".join(self.__argv__))

    def __dispath__(self, path):          # 处理 启动路径 输出路径， 资源路径， 模块路径
        # 模块工作目录与Pyinstall工作目录之间的关系
        # 模块工作目录与打包项目之间的关系
        # 导入的资源文件与原文件之间的关系
        """
        资源文件路径应该与项目启动程序在同一目录下
        项目依赖路径可以通过添加搜索路径解决
        
        模块依赖的资源文件使用相对路径查询
        """
        workdir = Path.cwd()
        spec = self.__spec__.absolute()
        script = self.script.absolute()

        path = self.__check_path__(path, check=True)

        # XXXXX
        relative_path_to_cwd = path.absolute().relative_to(script.parent)
    
        # 项目与工作目录之间的相对路径
        relative_spec_to_cwd = spec.relative_to(workdir)
        relative_script_to_cwd = script.relative_to(workdir)


    def __datas__(self, datas:List[Path]):
        targets = []
        for source in datas:
            source = self.__check_path__(source)
            targets.append( "--add-data {}".format(self.__sep__.join((str(source.absolute()), str(source.parent)))))
        return " ".join(targets)
            
    def __binaries__(self, binaries:List[Path]):
        targets = []
        for source in binaries:
            source = self.__check_path__(source, check=True)
            targets.append("--add-binary={}".format(self.__sep__.join((str(source.absolute()), str(source.parent)))))
        return " ".join(targets)
    
    def __paths__(self, paths:List[Path]):
        return " ".join(["--paths={}".format(self.__check_path__(path, check=True))] for path in paths)

    def __hiddens__(self, hiddens:List[str]):
        return " ".join(["--hidden-import={}".format(hidden) for hidden in hiddens])

    def __exclude_module__(self, excludes:List[str]):
        return " ".join(["--exclude-module={}".format(exclude) for exclude in excludes])

    def __exclude_upx__(self, excludes:List[Path]):      # --upx-exclude: 使用UPX排除指定文件，可使用通配符
        return " ".join(["--upx-exclude={}".format(exclude) for exclude in excludes])  

    def __hook_dirs__(self, hooks:List[Path]):
        return " ".join(["--additional-hooks-dir={}".format(hook) for hook in hooks])

    def __hook_path__(self, hooks:Path):
        return " ".join(["--runtime-hook={}".format(hook) for hook in hooks])

    @staticmethod
    def help():                     # -h, --help: 显示帮助信息
        return subprocess.run("pyinstaller --help")
    
    @staticmethod
    def version():                  # -v, --version: 显示版本信息
        return subprocess.run("pyinstaller --version")
    
    def collect_submodules(self):# --collect-submodules: 搜索指定模块的所有子模块
        pass
    def collect_data(self):# --collect-data, --collect-datas: 搜集指定模块的数据
        pass
    def collect_brinaries(self):# --collect-binaries: 收集指定模块的二进制文件
        pass
    def collect_all(self):# --collect-all: 收集指定模块的所有数据、二进制文件、子模块
        pass
    def key(self):                 # --key: 用于加密Python字节码的密钥
        pass
    def python_option(self): # --python-option: 向Python解释器传递参数
        pass
 
    @staticmethod
    def __check_path__(path, check=False) -> Path: # 检查路径参数
        if not isinstance(path, Path):
            path = Path(path)
        
        if check and not path.exists():
            raise FileExistsError(f"Not Found {path}")
        return path
    
    def __check_module__(self, module:str): 
        pass

    def __check_package__(self, package:str):
        pass

if __name__ == "__main__":
    Pack("test.py",
         icon="static\icons\AntDesign\experiment-fill.ico",
         isone=True,
         clean=True,
         datas=[
             "static\icons\AntDesign\experiment-fill.ico",
             "lib/.config.project.xml",
             "lib/_init/.config.xml"
         ],
         hiddens=[
             "lib"
         ]
    )

    
