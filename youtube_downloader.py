import tkinter as tk
from tkinter import messagebox
from tkinter . filedialog import askdirectory
from pytube import YouTube
from tkinter import ttk
import os
from time import sleep
from threading import Thread


window = tk.Tk()
window.title('Youtube Downloader')
window.minsize(450,200)


def widget():
    link_label = tk.Label(window,text='video link')
    link_label.grid(row=0,column=0,padx=20 ,pady=20)
    link_label.config(font=("None",15),fg='green')


    link_input =tk.Entry(window , width = 40 , textvariable = video_link)
    link_input.grid(row=0,column=1)

    place_label = tk.Label(window,text='Directory')
    place_label.grid(row=1,column=0)
    place_label.config(font=("None",15),fg='green')
 
    place_input =tk.Entry(window , width = 30 , textvariable = download_dir )
    place_input.grid(row=1,column=1 , sticky = "w")


    place_btn = tk.Button(window , text='Open' , width ='10' , bg='green', fg = 'white' , command=browse) 
    place_btn.grid(row=1 , column=2)


    download_btn = tk.Button( text='Download Now' , command= download )
    download_btn.grid(row =2,column=1 , pady = "20")
    download_btn.config(height=3 , width = 20 , bg = 'green' , fg = 'white')
       

def browse():
    directory=askdirectory(initialdir=" Your Directory Path " , title="save")
    download_dir.set(directory)

def download():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download(save_dir)
    messagebox.showinfo(title="Success" , message="Your video download succesfully ")

download_dir = tk.StringVar()
video_link = tk.StringVar()


widget()


window.mainloop()