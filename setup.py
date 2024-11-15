from setuptools import setup, find_packages

setup(
    name="QuickMediaDL",
    version="0.1.1",
    description="A library for downloading videos or audio from online sources",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Amirhossein bahrami",
    author_email="amirbaahrami@gmail.com",
    url="https://github.com/Amirprx3/QuickMediaDL",
    license="MIT",
    keywords=["python", "Downloader", "ViedoDownloader", "YoutubeDownloader"],
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
