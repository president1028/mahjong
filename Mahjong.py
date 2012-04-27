#Mahjong
import Tkinter as tk
import MahjongClass as mc
from PIL import Image, ImageTk

class App:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()
##        self.hi_there = tk.Button(frame,text="Hello",command=self.say_hi)
##        self.hi_there.pack(side=tk.LEFT)
##
##    def say_hi(self):
##        print "hello,world"


def sayhello():
    print "hello,world!"


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    
#    imageFolder=r'D:\Code\Python_Code\Mahjong\res\tile'+'\\0'
    imageFolder=r'E:\PythonCode\Mahjong\res\tile'+'\\0'
    imageLast='-3-H.png'
    for i in range(9):
        imageFile = imageFolder + str(i) + imageLast
        print imageFile
        image1 = ImageTk.PhotoImage(Image.open(imageFile))

        w = image1.width()
        h = image1.height()

        x = y = 0
        root.geometry("%dx%d+%d+%d" % (10*w,4*h,x,y))
        button1 = tk.Button(root,command=sayhello,image=image1)
        button1.pack(side='left')
        button1.image = image1
    
    root.mainloop()
