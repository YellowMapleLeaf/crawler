import pygame
import time

path=r'E:\音乐\韩雪 - 飘雪.flac'

#初始化
pygame.mixer.init()

#加载音乐
track=pygame.mixer.music.load(path)

#播放
pygame.mixer.music.play()
time.sleep(100)

#暂停
pygame.mixer.music.pause()

#结束
pygame.mixer.music.stop()




