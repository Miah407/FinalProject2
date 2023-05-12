from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, window):
        self.window = window
        window['bg'] = 'grey'

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        self.b1 = Button(self.window, text='Power', command=self.power, bg='red', width=5, height=1)
        self.b1.place(x=50, y=150)

        self.b2 = Button(window, text='Mute', command=self.mute,width=5, height=1)
        self.b2.place(x=100, y=150)

        self.b3 = Button(window, text='+', command=self.volume_up,width=2, height=1)
        self.b3.place(x=60, y=200)

        self.b4 = Button(window, text='⇧', command=self.channel_up, width=2, height=1)
        self.b4.place(x=110, y=200)

        self.b5 = Button(window, text='-', command=self.volume_down,width=2, height=1)
        self.b5.place(x=60, y=225)

        self.b6 = Button(window, text='⇩', command=self.channel_down,width=2, height=1)
        self.b6.place(x=110, y=225)

        self.progressbar = ttk.Progressbar(window, orient=tk.VERTICAL, length=95, mode='determinate')
        self.progressbar.place(x=220, y=160)

        self.frame = Frame(window, width=200, height=150)
        self.frame.pack()
        self.frame.place(x=250, y=150)

        self.Ch1 = ImageTk.PhotoImage(Image.open(r"assets/Ch1.jpg"))
        self.Ch2 = ImageTk.PhotoImage(Image.open(r"assets/Ch2.jpg"))
        self.Ch3 = ImageTk.PhotoImage(Image.open(r"assets/Ch3.jpg"))
        self.Ch4 = ImageTk.PhotoImage(Image.open(r"assets/Ch4.png"))

        self.off = ImageTk.PhotoImage(Image.open(r"assets/off.png"))
        label = Label(self.frame, image=self.off)
        label.pack()

    def power(self):
        self.__status = not self.__status
        if self.__status:
            for widgets in self.frame.winfo_children():  # https://www.tutorialspoint.com/how-to-clear-out-a-frame-in-the-tkinter
                widgets.destroy()
            self.Ch1 = ImageTk.PhotoImage(Image.open(r"assets/Ch1.jpg"))
            self.__channel = 3
            label = Label(self.frame, image=self.Ch1)
            label.pack()
        else:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            self.off = ImageTk.PhotoImage(Image.open(r"assets/off.png"))
            label = Label(self.frame, image=self.off)
            label.pack()
        self.window.update_idletasks()
        time.sleep(1)

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.b3["state"] == NORMAL:
                self.b3["state"] = DISABLED
                self.b5["state"] = DISABLED
                self.__volume = 0
                self.progressbar['value'] = 0
                self.window.update_idletasks()
            else:
                self.b3["state"] = NORMAL
                self.b5["state"] = NORMAL
                self.window.update_idletasks()

    #
    def channel_up(self):
        if self.__status:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
                if self.__channel != Television.MAX_CHANNEL:
                    self.__channel += 1
                else:
                    self.__channel = Television.MIN_CHANNEL
            if self.__channel == 0:
                label = Label(self.frame, image=self.Ch2)
                label.pack()
            elif self.__channel == 1:
                label = Label(self.frame, image=self.Ch3)
                label.pack()
            elif self.__channel == 2:
                label = Label(self.frame, image=self.Ch4)
                label.pack()
            elif self.__channel == 3:
                label = Label(self.frame, image=self.Ch1)
                label.pack()

    def channel_down(self):
        if self.__status:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
                if self.__channel != Television.MIN_CHANNEL:
                    self.__channel -= 1
                else:
                    self.__channel = Television.MAX_CHANNEL
            if self.__channel == 0:
                label = Label(self.frame, image=self.Ch2)
                label.pack()
            elif self.__channel == 1:
                label = Label(self.frame, image=self.Ch3)
                label.pack()
            elif self.__channel == 2:
                label = Label(self.frame, image=self.Ch4)
                label.pack()
            elif self.__channel == 3:
                label = Label(self.frame, image=self.Ch1)
                label.pack()

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                self.__volume += 1
                self.progressbar['value'] = 50
                self.window.update_idletasks()
                time.sleep(1)
            elif self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
                self.progressbar['value'] = 99.9
                self.window.update_idletasks()
                time.sleep(1)

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                self.__volume -= 1
                self.progressbar['value'] = 50
                self.window.update_idletasks()
                time.sleep(1)
            elif self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
                self.progressbar['value'] = 0
                self.window.update_idletasks()
                time.sleep(1)

    def __str__(self):
        if self.__muted:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
