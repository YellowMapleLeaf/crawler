import win32api
import win32con
import win32gui



def setWallPaper(path):
    #打开注册表
    reg_key=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)

    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)


path=r'G:\2018千锋Python基础视频源码笔记\res\9.jpg'

setWallPaper(path)



