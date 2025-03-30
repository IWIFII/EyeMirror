

# 播放视频
import cv2
import tkinter as tk
from PIL import ImageTk, Image
import time

class playVideo:
    @staticmethod
    def showImage(filepath):
        root = tk.Tk()
        image = Image.open(filepath)
        image = image.resize((1024, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=img).pack()

        root.after(20000, lambda: root.destroy())
        root.mainloop()
    # @staticmethod
    # def run(video):

        # cap = cv2.VideoCapture(video)     # 读取视频
        # while cap.isOpened():               # 当视频被打开时：
        #     ret, frame = cap.read()         # 读取视频，读取到的某一帧存储到frame，若是读取成功，ret为True，反之为False
        #     if ret:                         # 若是读取成功
        #         cv2.imshow('frame', frame)  # 显示读取到的这一帧画面
        #         key = cv2.waitKey(1)       # 等待一段时间，并且检测键盘输入
        #         if key == ord('q'):         # 若是键盘输入'q',则退出，释放视频
        #             cap.release()           # 释放视频
        #             break
        #     else:
        #         cap.release()
        # cv2.destroyAllWindows()             # 关闭所有窗口


# playVideo.run('/mirror/pycharm_project_365/resoures/eye.mp4')
