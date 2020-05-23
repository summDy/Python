
# Python2.x 导入方法
# from Tkinter import *           # 导入 Tkinter 库
# Python3.x 导入方法
# from tkinter import * 
import tkinter as tk
# import tkMessageBox
import math

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        pass

    def say_hi(self):
        print("hi there, everyone!")
        pass

content =dir(math)
print (content)
    
root = tk.Tk()    #顶层窗口的对象，用于容纳所有内容
root.title('第一个例程')    #设置标题
app = Application(master=root)
app.mainloop()   #写完窗口以后最后要有这一句才能显示这整个窗口
# app.quit()    #退出窗口