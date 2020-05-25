import tkinter as tk
import serial
import serial.tools.list_ports_windows

try:
    # plist = list(serial.tools.list_ports.comports())
    plist = list(serial.tools.list_ports.comports())
    if (plist) <= 0:
        print("no found com")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 9600, timeout=60)
        print("usede com name>>", serialFd.name)
except Exception as e:
    print("---“Ï≥£---£∫", e)


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        pass

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
