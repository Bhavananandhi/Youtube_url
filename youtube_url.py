import yt_dlp
import os
# Function to download a video
def download_video(video_url):
    if not os.path.exists('MyVideos'):
        os.makedirs('MyVideos')
    customname=input("Enter the custom filename")
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': f'MyVideos/{customname}%(title)s.%(ext)s',# Save the file with the video's title as the filename is we remove customname else we can save with our customname
        'subtitleslangs': ['en'],#save with sutitles
        'noplaylist':True #if we have accidentally provided the url of a playlist the it makes sure it only a video nor entire playlist
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {video_url}")
            ydl.download([video_url])
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")
video_url =input("Enter the URL of the video:")
download_video(video_url)


""" ##*Downloading multiple videos at one simultaneously using threats*##
-----------------------
import threading
import yt_dlp
def download_video(vd_urls):
    yt_out={
       'format':'best'
    }
    try:
        with yt_dlp.YoutubeDL(yt_out) as yt:
            print(f"Downloading: {vd_urls}")
            yt.download([vd_urls])
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

threads=[]
urls=['vd_url1','vd_url2','vd_url3']
for url in urls:
    thrd=threading.Thread(target=download_video,args=(url,))
    threads.append(thrd)
    thrd.start()
for thread in threads:
    thread.join()

    """
































