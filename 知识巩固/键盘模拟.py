import win32api
import time
import win32con


win32api.keybd_event(91,0,0,0)
time.sleep(0.1)
win32api.keybd_event(77,0,win32con.KEYEVENTF_KEYUP,0)
Y








