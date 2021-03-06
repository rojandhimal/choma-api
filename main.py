import logging
import sys
from flask import Flask, request, send_file
from pytube import YouTube
import numpy as np
import os
 
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)


def generateUrl(id):
    return "https://www.youtube.com/watch?v="+id

# function to get unique values
def getUnique(list1):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def send_download_file(file_path):
    return send_file(file_path, as_attachment=True)

def remove_download_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    else:
        print("Can not delete the file as it doesn't exists")
        pass
 
@app.route('/')
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    html_page = f"""<html><head>
                    <Title>YouTube Downloader</Title></head>
                    <body><h2>Enter URL to download YouTube Vids!</h2>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <input type="text" name="URL">
                    <input type="submit" value="Submit">
                    </form></div><br><br>
                    </body></html>"""
    return html_page
 
@app.route('/get-quality/<video_id>', methods=['GET','POST'])
def get_video_quality(video_id):
    """
    input : youtube video id
    output : all available quality list
    get all video quality
    """
    try:
        youtube_url = generateUrl(id=video_id)
        video_resolutions = []
        videos = []
        my_video = YouTube(youtube_url)
        for stream in my_video.streams.filter(only_video=True).order_by('resolution'):
            video_resolutions.append(stream.resolution)
            videos.append(stream)
        return {"quality":getUnique(video_resolutions),"title":my_video.title,"thumbnail":my_video.thumbnail_url,"description":my_video.description,"views":my_video.views,"length":my_video.length/60}
    except:
        logging.exception('Failed download')
        return {"fail":'Video Quality download failed!'}

@app.route('/download_video/<video_id>/<quality>', methods=['GET','POST'])
def download_video(video_id,quality):
    """
    Download video
    """
    try:
        youtube_url = generateUrl(video_id)
        print("youtube_url",youtube_url)
        my_video = YouTube(youtube_url)
        stream = my_video.streams.get_by_resolution(str(quality))
        download_path = "videos"
        print("download_path",download_path)
        stream.download(download_path)
        fname = my_video.title
        video_path = os.getcwd() +'/videos'
        files = os.listdir(video_path)
        file_path = os.path.join(download_path, files[0]) 
        return send_file(file_path, as_attachment=True)
    except:
        logging.exception('Failed download')
        return 'Video download failed!'


if __name__ == "__main__":
    app.run()
    get_video_quality("https://www.youtube.com/watch?v=Yb3U2f6K2dI")
