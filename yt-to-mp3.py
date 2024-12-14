import os
from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import messagebox

def download_audio(url):
    output_path = "/Users/saajan/Desktop/musica" # Replace with you path
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Allow downloading playlists
    }

    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Audio downloaded and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_download_button_click():
    url = url_entry.get()
    if url:
        download_audio(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a YouTube video or playlist URL")

# Create the main window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")

# Create and place the URL entry
url_label = tk.Label(root, text="Enter the YouTube video or playlist URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=on_download_button_click)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()