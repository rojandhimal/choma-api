import logging
import sys
from flask import Flask, request, send_file
from pytube import YouTube
import numpy as np
 
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
        return {"quality":getUnique(video_resolutions)}
    except:
        logging.exception('Failed download')
        return {"fail":'Video Quality download failed!'}

@app.route('/download_video/<video_id>/<quality>', methods=['GET','POST'])
def download_video(video_id,quality):
    """
    Download video
    """
    try:
        youtube_url = generateUrl()
        my_video = YouTube(youtube_url)
        fname = download_path.split('//')[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception('Failed download')
        return 'Video download failed!'


if __name__ == "__main__":
    app.run()
    get_video_quality("https://www.youtube.com/watch?v=Yb3U2f6K2dI")
