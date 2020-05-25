# 查看pyserial是否安装    pip list
# pip install pyserial     #安装serial
import serial
# 这里使用的是Windows
import serial.tools.list_ports_windows
import serial.tools.list_ports

try:
    # plist = list(serial.tools.list_ports.comports())
    plist = list(serial.tools.list_ports.comports())
    # print(plist)
    if len(plist) <= 0:
        print("The serial port can't find")
    else:
        for i in list(plist):
            pass
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 9600, timeout=60)
        # serialFd.baudrate(115200)
        # serialFd.open()
        serialFd.close()
        print("usede com name>>", serialFd.name)
except Exception as e:
    print("used com", e)
