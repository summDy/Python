# 这个语句导入tkinter模块，但为方便，为它定义了一个别名tk。
import tkinter as tk
"""
主体程序
"""


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # 显示窗口并使用grid布局，grid方法是从Frame继承来的，Tkinter中有一个概念叫布局（layout），就是控件的排列方式。除了grid还有pack灯布局
        self.grid()  # 网格
        # self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        # self.QUIT.pack({"side": "left"})
        self.QUIT.grid(row=50, column=200)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        # self.hi_there.pack({"side": "left"})
        self.hi_there.grid(row=20, column=40)

        self.hui = tk.Button(self, text='hui', command=self.say_hui)
        # self.hui["text"] = "hui"
        # self.hui["command"] = self.say_hui
        # self.hui.pack({"side": "right"})
        self.hui.grid(row=40, column=50)

        self.lable_com = tk.Label(self)
        self.lable_com["text"] = "COM"

    def say_hi(self):
        print("hi there, everyone!")

    def say_hui(self):
        print("hui")


root = tk.Tk()
app = Application(master=root)
# 设置窗口标题
app.master.title("First Tkinter")
# 设置窗口大小
app.master.geometry("380x300")
app.mainloop()
