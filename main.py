import tkinter
import pytube
import time

queued_url = []

def show_queue():
    msg_splash = tkinter.Tk()
    root.title("MSG Splash")
    for x in range(len(queued_url)):
        l = tkinter.Label(msg_splash, text=queued_url[x])
        l.pack()
    m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
    m.pack()

def clear_queue():
    queued_url.clear()
    root.title("MSG Splash")
    msg_splash = tkinter.Tk()
    l = tkinter.Label(msg_splash, text='Queue cleared')
    l.pack()
    m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
    m.pack()

def add_to_queued_downl():
    url = entry.get()
    queued_url.append(url)
    msg_splash = tkinter.Tk()
    root.title("MSG Splash")
    l = tkinter.Label(msg_splash, text="Url added to queue!")
    l.pack()
    m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
    m.pack()

def queued_downl():
    path = entry2.get()
    for url in queued_url:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        print(path)
        print(video.title)
        video.download(path)
        msg_splash = tkinter.Tk()
        root.title("MSG Splash")
        l = tkinter.Label(msg_splash, text="Downloaded to " + path + "\n" + video.title)
        l.pack()
        m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
        m.pack()

def downl_vid():
    url = entry.get()
    path = entry2.get()
    print(url)
    print(path)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(path)
    print(video.title)
    video.download(path)
    msg_splash = tkinter.Tk()
    l = tkinter.Label(msg_splash, text="Downloaded to " + path + "\n" + video.title)
    l.pack()
    m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
    m.pack()

root = tkinter.Tk()
root.title("YT Downloader")
root.geometry('302x150')

l = tkinter.Label(root, text='Easy Youtube Downloader 0.1 by ndi')
l.pack()
l = tkinter.Label(root, text='Video url')
l.pack()
entry = tkinter.Entry(width=230)
entry.pack()
l = tkinter.Label(root, text='Download path')
l.pack()
entry2 = tkinter.Entry(width=230)
entry2.pack()

m = tkinter.Button(root, text = 'Download', command=downl_vid, bg='grey')
m.place(x=0,y=100)
m = tkinter.Button(root, text = 'Add to queue', command=add_to_queued_downl, bg='grey')
m.place(x=82,y=100)
m = tkinter.Button(root, text = 'Queue download', command=queued_downl, bg='grey')
m.place(x=182,y=100)
m = tkinter.Button(root, text = 'Clear queue', command=clear_queue, bg='grey')
m.place(x=0,y=125)
m = tkinter.Button(root, text = 'Show queue', command=show_queue, bg='grey')
m.place(x=82,y=125)

root.mainloop()