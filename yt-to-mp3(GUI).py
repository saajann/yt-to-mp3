import ssl
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

ssl._create_default_https_context = ssl._create_unverified_context

def download_audio():
    url = url_input.text()
    path = path_input.text()
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download(output_path=path)
    mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
    AudioFileClip(audio_file).write_audiofile(mp3_file)
    os.remove(audio_file)  # remove the original mp4 file

app = QApplication([])
window = QWidget()
url_label = QLabel("Enter the YouTube URL:")
url_input = QLineEdit()

path_label = QLabel("Enter the output path:")
path_input = QLineEdit()

download_button = QPushButton("Download")
download_button.clicked.connect(download_audio)

layout = QVBoxLayout()
layout.addWidget(url_label)
layout.addWidget(url_input)
layout.addWidget(path_label)
layout.addWidget(path_input)
layout.addWidget(download_button)
 
window.setLayout(layout)
window.show()

app.exec_()
