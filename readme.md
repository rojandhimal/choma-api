# Video downloader 
## Description

Choma is Software as a Service(SaaS) product developed with the motive to download playlist vides. 

## Getting Started
### Dependencies
* Python 3.5+
* Flask
* Pytube
* Numpy

### Installing
To clone the git repository:
```
git clone https://github.com/rojandhimal/choma-api
```
### Executing Program:

1. Run the following command in the app's directory to run your web app.
    `python main.py`

2. Go to http://0.0.0.0:3001/

3. Get video details
```http://localhost:5000/get-quality/youtube_video_id```

This returns video detail 
  * title 
  * description
  * views count 
  * thumnailurl
4. Download view
  ``` http://localhost:5000/get-quality/youtube_video_id/quality ```


## Authors

* [Rojan Dhimal](https://github.com/rojandhimal)

<a name="license"></a>
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<a name="acknowledgement"></a>

## Future Enhancement 
Download video from other platform like facebook, twitter, instagram
