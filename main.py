from pytube import YouTube
from tkinter import *
import tkinter.ttk as ttk
import threading
import os


def progress():
    threading.Thread(target=download_video).start()


def download_video():
    lbl2.configure(text='Процесс...')
    pb['value'] = 10
    link = ent.get("1.0", "end")
    path = os.path.expanduser('~') + '\Downloads'
    pb['value'] = 30
    a = YouTube(link)
    pb['value'] = 50
    a = a.streams.first()
    pb['value'] = 70
    a.download(path)
    pb['value'] = 100
    lbl2.place(x=145,y=125)
    lbl2.configure(text='Загрузка видео завершена')


root = Tk()
root.geometry('550x150')
lbl1 = Label(text='Вставьте ссылку на видео:',font=20)
lbl1.place(x=5,y=5)
lbl2 = Label(text='',font=20)
lbl2.place(x=210,y=125)
ent = Text(font=16,width=250,height=1)
ent.place(x=215,y=5)
btn = Button(text='Скачать',font=22,command=progress)
btn.place(x=215,y=45)
pb = ttk.Progressbar(length=250, mode="determinate")
pb.place(x=120, y=100)
root.title('Скачать видео с YouTube')
root.mainloop()