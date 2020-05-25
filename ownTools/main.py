# 这个语句导入tkinter模块，但为方便，为它定义了一个别名tk。
import tkinter as tk
"""
主体程序
"""


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # 显示窗口并使用grid布局，grid方法是从Frame继承来的，Tkinter中有一个概念叫布局（layout），就是控件的排列方式。除了grid还有pack灯布局
        # self.grid()  # 网格
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        HEIGHT = 200
        WIDTH = 100
        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        frame = tk.Frame(self, bg='#80c1ff')
        frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        frame.QUIT = tk.Button(frame)
        frame.QUIT["text"] = "QUIT"
        frame.QUIT["fg"] = "red"
        frame.QUIT["command"] = self.quit

        frame.QUIT.pack()
        # self.QUIT.grid(row=50, column=200)

        self.hi_there = tk.Button(frame)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack()
        # self.hi_there.grid(row=2, column=4)

        self.hui = tk.Button(self, text='hui', command=self.say_hui)
        # self.hui["text"] = "hui"
        # self.hui["command"] = self.say_hui
        self.hui.pack({"side": "right"})
        # self.hui.grid(row=40, column=50)

        self.la = tk.Label(frame, width=30, height=2, fg="red", bg="blue")
        self.la["text"] = "COM"

        # self.la.grid(row=3, column=6)
        self.la.pack()

    def say_hi(self):
        print("hi there, everyone!")

    def say_hui(self):
        print("hui")


root = tk.Tk()
app = Application(master=root)
# 设置窗口标题
app.master.title("First Tkinter")
# 设置窗口大小
app.master.geometry("500x300")
# app.master.rowconfigure(0, minsize=800, weight=1)
# app.master.columnconfigure(0, minsize=800, weight=1)
app.mainloop()
