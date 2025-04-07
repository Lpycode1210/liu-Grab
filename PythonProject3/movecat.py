from tkinter import Tk, Entry, Button, Label, Text, StringVar, PhotoImage, ttk
from PIL import Image, ImageTk
from pynput import mouse
import time
import threading

def thread_it(func, *args):
    myThread = threading.Thread(target=func, args=args)
    myThread.setDaemon(True)
    myThread.start()

def move():
    control = mouse.Controller()
    global going
    going = True
    while going:
        control.move(-20, 0)
        time.sleep(2)
        control.move(20, 0)
        time.sleep(2)

def end():
    global going
    going = False

def GUI():
    fm_main = Tk()
    fm_main.resizable(False, False)
    fm_main.geometry("250x300+500+200")
    fm_main.title("move cat")
    fm_main.iconbitmap(r"E:\PythonProject3\move cat\image\程序图标.ico")
    btn1 = Button(fm_main, text='开始运行', command=lambda: thread_it(move), font=("华文行楷", 12))
    btn2 = Button(fm_main, text='结束运行', command=lambda: end(), font=("华文行楷", 12))
    btn1.grid(row=1, column=0, columnspan=1, sticky="w", padx=40, pady=9)
    btn2.grid(row=1, column=0, columnspan=1, sticky="e", padx=40, pady=9)

    # 插入图片
    global photo
    image = Image.open(r"E:\PythonProject3\move cat\image\R.jpg")
    image = image.resize((240, 200), Image.Resampling.LANCZOS)  # 替换为 Image.Resampling.LANCZOS
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo
    label.grid(row=2, column=0, padx=2, pady=0)

    fm_main.mainloop()

GUI()