import pytube, os
def arranque():
    os.system("color 4f")
    os.system("title Youtube downloader")
    x = os.path.exists(r'./Videos')
    if x == False:
        os.system("md Videos")
    video_url = input("Insert the link of video: ")
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download(r'./Videos')
    os.system("clear")
    print("The video has been downloaded")
    return arranque()
arranque()