import os
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
import matplotlib.cm as pcm
import numpy as np
# 利用mode的选择来确定你想实现的功能
# 尽可能的将功能写的具有足够好的适用性
# 找时间可以学习-help的写法
# 应具备同步到GitHub的功能
# 应当为每个mode提供足够多的使用说明
# 应当可以利用cmake实现代码的编译
# 类的定义和功能实现尽可能的放在一起



def OutputMessage(id):
    # 保存所有的输出信息
    message = {1: "请输入所需要采用的mode的id\n",
               2: "mode_id: ",
               3: "paht: ",
               4: "suffix: ",
               5: "numring: ",
               6: "type: "}
                
    return message[id]

# mode-1
# 实现文件夹中指定文件后缀的读取，然后保存到一个新建的文件夹
# 新建文件夹的名称默认为Mode1Temp
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
    path = input(OutputMessage(5)) # 获得路径
    suffix = input(OutputMessage(4)) # 获得文件标识
    globalvariable = GVMode1(path=path,suffix=suffix)
    globalvariable.MkdirFolder()
    globalvariable.CopyFile()
    pass

# mode-2
# 从data.txt中读取指定环数的数据按照，暂时先按照六边形的规律画出来
# 默认输出文件为figure.jpg

class GVmode2():
    
    def __init__(self,numring,type):
         self.pitch = 1.0
         self.filename = "data.txt"
         self.ouputname = "figure.jpg"
         self.dpi = 300
         self.numdata = 0
         self.value = []
         self.numring = numring
         self.type = type
    
    def InitVariables(self):
        numring = self.numring
        pitch = self.pitch
        xcoord = []
        ycoord = []
        hcoord = []
        vcoord = []
        
        if self.type == "hex":
            self.numdata = 6 * (numring - 1) + 1
            for i in range(1,2*numring):
                if (i <= numring):
                    temp = numring + i -1
                else:
                    temp = 3*numring - i - 1
                for j in range(1,temp+1):
                    xcoord.append(i)
                    ycoord.append(j)
            for i in range(len(xcoord)):
                hcoord.append(np.abs((xcoord[i]-numring)*2*np.sin(np.radians(60))*pitch*np.cos(np.radians(60))) + (ycoord[i]-1)*2*np.sin(np.radians(60))*pitch)
                vcoord.append((xcoord[i]-numring)*2*np.sin(np.radians(60))*pitch*np.sin(np.radians(60)))

        elif self.type == "rec":
            self.numdata = (numring + 1)**2
        else:
            pass
        self.x_min = min(hcoord) - pitch
        self.x_max = max(hcoord) + pitch
        self.y_min = min(vcoord) - pitch
        self.y_max = max(vcoord) + pitch
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.hcoord = hcoord
        self.vcoord = vcoord
         
    def DataRead(self):
        temp_int = 0
        temp_logic = 0
        filename = self.filename
        f = open(filename,"r")
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            line = lines[-1 - i].strip("\n").split()
            for j in range(len(line)):
                temp_int = temp_int + 1
                self.value.append(float(line[j]))
                if (temp_int == self.numdata):
                    temp_logic = 1
                    break
                else:
                    continue
            if (temp_logic):
                break
            else:
                continue
    
    def FigPlot(self):
        hcoord = self.hcoord
        vcoord = self.vcoord
        values = self.value
        pitch = self.pitch
        x_min = self.x_min
        x_max = self.x_max
        y_min = self.y_min
        y_max = self.y_max
        ouputname = self.ouputname 
        fig, ax = plt.subplots(1)
        ax.set_aspect('equal')
        patches = []
        for x, y in zip(hcoord, vcoord):
            hex = RegularPolygon((x, y), numVertices=6, radius=pitch,orientation=np.radians(0))
            patches.append(hex)
        p = PatchCollection(patches,cmap=pcm.jet,alpha=0.3,edgecolor="k",linewidth=0.5)
        p.set_array(np.array(values))
        ax.add_collection(p)
        plt.colorbar(p,shrink=0.72,extend="neither",extendfrac=0.0,format="$%.2f$")
        plt.axis("off")
        plt.xlim(x_min,x_max)
        plt.ylim(y_min,y_max)
        plt.savefig(ouputname,dpi=self.dpi,bbox_inches="tight")


def MMode2():
    # Mode2的主函数
    numring = input(OutputMessage(5)) # 获得环数
    yype = input(OutputMessage(6)) # 获得type
    globalvariable = GVmode2(numring=numring,type=type)
    globalvariable.InitVariables()
    globalvariable.DataRead()
    globalvariable.FigPlot()
    pass

def Main():
    # 总的主函数
    print(OutputMessage(1))
    mode_id = int(input(OutputMessage(2)))
    if mode_id == 1:
        MMode1()
    elif mode_id == 2:
        MMode2()
    else:
        pass

if __name__ == '__main__':
    Main()