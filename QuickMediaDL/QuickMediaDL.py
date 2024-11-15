import yt_dlp
import os
from tqdm import tqdm

class VideoDownloader:
    """
    A library for downloading videos or audio from online sources such as YouTube.
    """

    def __init__(self, url, download_path="downloads"):
        """
        Initializes the downloader with the video URL and download path.
        
        :param url: URL of the video or audio to download
        :param download_path: Path where the file will be saved
        """
        self.url = url
        self.download_path = download_path
        
        # Options for yt-dlp, defining output template and loggers
        self.ytdl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Default path and filename template
            'noplaylist': True,  # Don't download playlist (just the video or audio)
            'quiet': False,  # Show output logs
            'logger': self.Logger(),  # Custom logger to display messages
            'progress_hooks': [self.progress_hook],  # Hook for progress updates
            'writesubtitles': True,  # Enable subtitle download
            'subtitleslangs': ['en']  # Default language for subtitles (change as needed)
        }

        # Create download path if it doesn't exist
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Initialize progress bar
        self.progress_bar = None

    class Logger:
        def debug(self, msg):
            print(f"DEBUG: {msg}")
        
        def warning(self, msg):
            print(f"WARNING: {msg}")
        
        def error(self, msg):            
            print(f"ERROR: {msg}")

        def info(self, msg):
            print(f"INFO: {msg}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if self.progress_bar is None:
                total_size = d.get('total_bytes', 1)
                self.progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading")
            self.progress_bar.update(d['downloaded_bytes'] - self.progress_bar.n)
        elif d['status'] == 'finished':
            self.progress_bar.n = self.progress_bar.total
            self.progress_bar.last_print_n = self.progress_bar.total
            self.progress_bar.update(0)
            self.progress_bar.set_postfix({"status": "Done"})
            self.progress_bar.close()

    def get_available_formats(self):
        try:
            with yt_dlp.YoutubeDL(self.ytdl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                formats = info_dict.get('formats', [])
                available_formats = []
                for fmt in formats:
                    format_id = fmt.get('format_id')
                    resolution = fmt.get('height', 'N/A')
                    ext = fmt.get('ext')
                    available_formats.append(f"{resolution}p: {format_id} ({ext})")
                return available_formats

        except Exception as e:
            print(f"Error while fetching formats: {str(e)}")
            return []

    def download_video(self, quality="480p", audio_only=False, filename=None, subtitle_langs=None):
        """
        Downloads the video or audio in the specified quality, with options for custom filename and subtitles.
        
        :param quality: Desired quality for the video (e.g., "480p")
        :param audio_only: Whether to download audio only (True) or video (False)
        :param filename: Custom filename for the downloaded file (without extension)
        :param subtitle_langs: List of languages for subtitles (e.g., ["en", "fa"])
        """
        # Update output filename if custom filename is provided
        if filename:
            self.ytdl_opts['outtmpl'] = os.path.join(self.download_path, f"{filename}.%(ext)s")

        # Set subtitle languages if specified
        if subtitle_langs:
            self.ytdl_opts['subtitleslangs'] = subtitle_langs

        if audio_only:
            format_id = 'bestaudio'
        else:
            format_id = {
                '360p': '18',
                '480p': '135',
                '720p': '22',
                '1080p': '137',
                '1440p': '264',
                '2160p': '313'
            }.get(quality, '135')

        self.ytdl_opts['format'] = format_id

        try:
            with yt_dlp.YoutubeDL(self.ytdl_opts) as ydl:
                print(f"Starting {'audio' if audio_only else 'video'} download at {quality}...")
                ydl.download([self.url])
                print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def set_output_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        self.download_path = path
        self.ytdl_opts['outtmpl'] = os.path.join(path, '%(title)s.%(ext)s')