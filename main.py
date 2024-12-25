#!/usr/bin/python3
from yt_dlp import YoutubeDL
from gradio_client import Client, handle_file
import sys
import os

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        global status_dict 
        status_dict = d
        
def help_menu():
    print("No options yet lol get rekt")

def main():
    if len(sys.argv) == 1:
        print("Usage: command URL")
        print("For help: command -h")
        return
    if sys.argv[1] == "-h":
        help_menu()
        return
    
    URL = sys.argv[1]
    ytdl_opts = {
        'format': 'worst*[vcodec=none][acodec!=none]',
        'postprocessor_hooks': [my_hook],
        'logger': MyLogger()
    }
    out_file = ""
    with YoutubeDL(ytdl_opts) as ydl:
        result = ydl.download(URL)
        info_dict = ydl.extract_info(URL, download=False)
        out_file = ydl.prepare_filename(info_dict)
    filename, file_extension = os.path.splitext(out_file)
    os.rename(out_file, 'tmp' + file_extension)
    client = Client("Nick088/Fast-Subtitle-Maker")
    result = client.predict(
    input_file=handle_file('tmp' + file_extension),
    prompt="",
    language="en",
    auto_detect_language=True,
    model="whisper-large-v3-turbo",
    include_video=False,
    font_selection="Arial",
    font_file=None,
    font_color="#FFFFFF",
    font_size=24,
    outline_thickness=1,
    outline_color="#000000",
    api_name="/generate_subtitles"
    )
    out_filename, out_fileextension = os.path.splitext(result[0])
    os.replace(result[0], filename + out_fileextension)
    os.remove("tmp" + file_extension)

if __name__ == "__main__":
    main()