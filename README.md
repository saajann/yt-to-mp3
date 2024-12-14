# YouTube to MP3 Downloader

This is a simple Python application that allows you to download audio from YouTube videos or playlists and save them as MP3 files on your computer.

## Requirements

- Python 3.x
- `yt-dlp` library
- `tkinter` library
- `ffmpeg` (for audio extraction)

## Installation

1. Install `yt-dlp`:
    ```sh
    pip install yt-dlp
    ```

2. Install `tkinter` (if not already installed):
    ```sh
    sudo apt-get install python3-tk
    ```

3. Install `ffmpeg`:
    ```sh
    sudo apt-get install ffmpeg
    ```

## Usage

1. Clone this repository or download the script to your local machine.
2. Declare the path where you want to download the MP3 files in `yt-to-mp3.py`.
3. Run the script:
    ```sh
    python yt-to-mp3.py
    ```

4. Enter the YouTube video or playlist URL in the provided input field.
5. Click the "Download" button to start downloading the audio.

## License

This project is licensed under the MIT License.