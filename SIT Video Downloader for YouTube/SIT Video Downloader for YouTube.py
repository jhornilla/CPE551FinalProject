from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry("600x700")
window.config(bg="maroon")
window.title("SIT Video Downloader on YouTube -- Joshua Hornilla")

sit_logo = PhotoImage(file = "stevenslogo.png")
window.iconphoto(False, sit_logo)

Label(window, text="Video Downloader", font = ("Arial 30 bold"), bg = "white").pack(padx=5, pady=50)

video_link = StringVar()

Label(window, text = "Link: ", font = ("Arial", 25, "bold")).place(x=250, y=110)
entry_link = Entry(window, width = 50, font = 35, textvariable = video_link, bd = 4).place(x = 20, y = 200)

def video_download():
    video_url = YouTube(str(video_link.get()))
    videos = video_url.streams.first()
    videos.download()

    Label(window, text="Finished downloading :)", font = ("Arial", 25, "bold"), bg = "black", fg = "maroon").place(x = 100, y = 400)
    Label(window, text = "Video is in project folder", font = ("Arial", 20, "bold"), bg = "black", fg = "maroon").place(x = 125, y = 500)

Button(window, text = "Download", font = ("Arial", 25, "bold"),bg = "maroon", command = video_download).place(x = 200, y = 300)


window.mainloop()