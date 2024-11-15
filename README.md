# VideoDownloader

**VideoDownloader** is a Python library designed to simplify the process of downloading videos and audio files from various online sources, such as YouTube. It leverages `yt-dlp` to offer a customizable experience with options for setting video quality, downloading subtitles, renaming files, and more.

## Features

- **Download Video or Audio**: Download high-quality video or audio files with a choice of resolution or bitrate.
- **Custom Filename**: Specify a custom name for downloaded files.
- **Subtitle Support**: Download subtitles in multiple languages.
- **Quality Selection**: Choose from popular resolutions (360p, 480p, 720p, etc.).
- **Download Progress**: Real-time progress bar using `tqdm`.
- **Logger for Feedback**: Custom logging for debug, warning, and error messages.
- **Easy-to-Use Output Path**: Save files in a specified directory.

## Installation

To install the package and its dependencies, simply use pip:

```bash
pip install VideoDownloader
```
## requirements:
- yt-dlp: Core library for downloading videos and audio.
- tqdm: For displaying progress during downloads.

```bash
pip install yt-dlp tqdm
```

## Usage
### Basic Setup

```python
from QuickMediaDL import VideoDownloader

# Specify the URL of the video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Initialize the downloader
downloader = VideoDownloader(url)
```

## Downloading Video or Audio
- Download a Video
```python
Download the video in 720p quality
downloader.download_video(quality="720p")
```
- Download Audio Only
```python
# Download the audio only
downloader.download_video(audio_only=True)
```
- Custom Filename and Subtitle Language
```python
# Download video with custom filename and subtitles in both English and Persian
downloader.download_video(quality="1080p", filename="MyCustomFile", subtitle_langs=["en", "fa"])
```
- Setting Output Directory
```python
# Change the default download directory
downloader.set_output_directory("my_downloads")
```
# Class and Method Descriptions

`VideoDownloader` :
The main class for managing downloads.

`__init__(url, download_path="downloads")` :
- **url**: URL of the video or audio to download.
- **download_path**: Directory to save downloaded files. Defaults to "downloads".

`download_video(quality="480p", audio_only=False, filename=None, subtitle_langs=None)` :
- **quality**: Video quality to download ("360p", "480p", "720p", etc.). Default is "480p".
- **audio_only**: Set `True` to download audio only.
- **filename**: Custom filename for the downloaded file.
- **subtitle_langs**: List of languages for subtitles (e.g., ["en", "fa"]).

`get_available_formats()` :
Returns a list of available formats and resolutions for the video, allowing you to choose based on your preference.

`set_output_directory(path)` : Sets the download path and adjusts settings accordingly.

- **path**: New directory path for saving downloaded files.

# Progress and Logging
The library uses `tqdm` to display a progress bar during downloads, giving you real-time feedback on the download process. Additionally, a custom logger (`Logger` class) is used for handling debug, warning, and error messages.

# Example
Here’s an example of downloading a video in `720p`, saving it to a custom directory with subtitles in English and Persian, and using a custom filename:

```python
from VideoDownloader import VideoDownloader

# Initialize downloader with URL
url = "https://www.youtube.com/watch?v=example"
downloader = VideoDownloader(url, download_path="my_downloads")

# Download video in 720p quality with specified subtitle languages
downloader.download_video(quality="720p", filename="MyCustomVideo", subtitle_langs=["en", "fa"])
```

# License
This project is licensed under the MIT License.

## Thank you
This project relies on the excellent [yt-dlp](https://github.com/yt-dlp/yt-dlp) library for handling video and audio downloads. Thanks to the `yt-dlp` community for their hard work!


---

**Happy downloading!** 🎉 If you like this project, consider giving it a star on GitHub and sharing it with others who may find it useful.

[![GitHub Stars](https://img.shields.io/github/stars/Amirprx3/QuickMediaDL?style=social)](https://github.com/Amirprx3/QuickMediaDL)