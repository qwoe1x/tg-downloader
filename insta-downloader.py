import requests

video_url="https://www.instagram.com/reel/CyovCr1BX3l/?utm_source=ig_web_copy_link"
def download_video(url=''):
    try:
        response = requests.get(url=url)
        with open('req_video.mp4', 'wb') as file:
            file.write(response.content)
        return 'Img downloaded'
    except Exception as ex:
        return 'Error'
def main():
    print(download_video(url=video_url))
main()