import os
from tkinter import *

import ttkbootstrap as ttk
from pytube import YouTube, exceptions


def search_btn():
    link = url.get()
    try:
        link = YouTube(link)
        output_string.set(link.title)
    except exceptions.RegexMatchError:
        output_string.set("This isn't a valid url")


def download_mp3():
    try:
        link = url.get()
        link = YouTube(link)
        download_audio = link.streams.filter(only_audio=True).first()
        out_file = download_audio.download(output_path=r'C:\Users\lovey\Music')

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        output_string.set(
            'Downloaded Successfully - saved in "C:\\Users\\lovey\\Music".')

    except exceptions:
        output_string.set("For some reason we can't download this MP3.")


def download_mp4():
    try:
        link = url.get()
        link = YouTube(link)
        download_video = link.streams.get_highest_resolution()
        download_video.download(output_path=r'C:\Users\lovey\Videos')
        output_string.set(
            'Downloaded Successfully - saved in "C:\\Users\\lovey\\Videos".')
    except:
        output_string.set("For some reason we can't download this MP3.")


window = ttk.Window(themename='journal')
window.title('YouTube Downloader')
window.geometry('600x400')

title_label = ttk.Label(master=window,
                        text='YouTube Downloader',
                        font='Candara 44')
title_label.pack()

url_label = ttk.Label(master=window,
                      text='Enter the URL here:',
                      font='Candara 18')
url_label.pack(pady=15)

url = StringVar(value='URL')
url_entry = ttk.Entry(master=window,
                      textvariable=url,
                      font='Candara 12',
                      width=50)
url_entry.pack()

search_button = ttk.Button(master=window,
                           text='Search URL',
                           command=search_btn)
search_button.pack(pady=15)

out_label = ttk.Label(master=window,
                      text='The video to download is:',
                      font='Candara 14')
out_label.pack()

output_string = StringVar(value='')
output_label = ttk.Label(master=window,
                         font='Candara 14 italic',
                         textvariable=output_string)
output_label.pack(pady=5)

audio_button = ttk.Button(master=window,
                          text='Download MP3',
                          command=download_mp3)

video_button = ttk.Button(master=window,
                          text='Download MP4',
                          command=download_mp4)

audio_button.pack(side='left', padx=130)
video_button.pack(side='left')

window.mainloop()
