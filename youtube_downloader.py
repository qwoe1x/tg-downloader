from pytube import YouTube
import os

async def yt_downloader(link, message, bot):
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    with open(yt.title + ".mp4", 'rb') as video_file:
        await bot.send_video(message.chat.id,  open(yt.title + ".mp4", 'rb'))
    os.remove(yt.title + ".mp4")