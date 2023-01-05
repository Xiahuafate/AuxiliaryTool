import os
# 利用mode的选择来确定你想实现的功能
# 尽可能的将功能写的具有足够好的适用性
# 找时间可以学习-help的写法
# 应具备同步到GitHub的功能
# 应当为每个mode提供足够多的使用说明
# 应当可以利用cmake实现代码的编译
# 类的定义和功能实现尽可能的放在一起

# mode-1
# 实现文件夹中指定文件后缀的读取，然后保存到一个新建的文件夹
# 新建文件夹的名称默认为Mode1Temp

def OutputMessage(id):
    # 保存所有的输出信息
    message = {1: "请输入所需要采用的mode的id\n",
               2: "mode_id: ",
               3: "paht: ",
               4: "suffix: "}
    return message[id]
class GVMode1():
    # 
    def __init__(self,path,suffix): # 常用变量定义
        self.path = path
        self.suffix = suffix
        self.folder = "Mode1Temp" 
    
    def MkdirFolder(self): # 建立临时文件夹
        self.folder = self.path + "\\" + self.folder
        if (os.path.exists(self.folder)):
            os.removedirs(self.folder)
            os.makedirs(self.folder)
        else:
            os.makedirs(self.folder)
        
    def CopyFile(self): # 复制符合条件的文件
        roots = []
        dirs = []
        files = []
        for root, dir, file in os.walk(self.path):
            roots.append(root)
            dirs.append(dir)
            files.append(file)
        for i in range(len(files)):
            for j in range(len(files[i])):
                file = files[i][j]
                if self.suffix in file:
                    str1 = "copy \"" + roots[i] + "\\\\" + file +"\" " + self.folder
                    print(str1)
                    os.system(str1)
                else:
                    continue
    
def MMode1():
    # Mode1的主函数
    path = input(OutputMessage(3)) # 获得路径
    suffix = input(OutputMessage(4)) # 获得文件标识
    globalvariable = GVMode1(path=path,suffix=suffix)
    globalvariable.MkdirFolder()
    globalvariable.CopyFile()
    pass


def Main():
    # 总的主函数
    print(OutputMessage(1))
    mode_id = int(input(OutputMessage(2)))
    if mode_id == 1:
        MMode1()
    else:
        pass

if __name__ == '__main__':
    Main()