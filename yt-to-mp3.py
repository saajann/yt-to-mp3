import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_audio(url, path):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download(output_path=path)
    mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
    AudioFileClip(audio_file).write_audiofile(mp3_file)
    os.remove(audio_file)  # remove the original mp4 file

# Prompt the user for the YouTube URL and output path
url = input("Enter the YouTube URL: ")

default_path = ""  # Set your default path here

path = input("Enter the output path (leave blank for default path): ")
if not path:
    path = default_path

# Call the download_audio function
download_audio(url, path)