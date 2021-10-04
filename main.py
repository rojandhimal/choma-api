import logging
import sys
from flask import Flask, request, send_file
from pytube import YouTube
 
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)
 
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
 
@app.route('/get-quality/<url>', methods=['GET','POST'])
def download_video(url):
    """
    get all video quality
    """
    try:
        youtube_url = request.form['URL']
        video_resolutions = []
        videos = []
        my_video = YouTube(youtube_url)
        for stream in my_video.streams.order_by('resolution'):
            # print(stream)
            video_resolutions.append(stream.resolution)
            videos.append(stream)
        # print("video_resolutions",video_resolutions)
    #     fname = download_path.split('//')[-1]
    #     return send_file(fname, as_attachment=True)
        return video_resolutions,youtube_url
    except:
        logging.exception('Failed download')
        return 'Video download failed!'

@app.route("/download/<id>")
def galleryrecommend(id):
    print("name",id)
    data=get_recommendation(id)
    return {"data":data}


if __name__ == "__main__":
  app.run()