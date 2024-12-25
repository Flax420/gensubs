# Gensubs
A simple script to automatically feed Youtube videos into [this](https://huggingface.co/spaces/Nick088/Fast-Subtitle-Maker) 
Hugging Face space for generating subtitles using whisper.
This tool is mainly something I'm developing for myself for use in learning Japanese using Youtube.

# Notes
Not tested on MacOS or Linux, besides WSL where it did not work.

# Installation
```bash
git clone https://github.com/Flax420/gensubs
cd gensubs
python -m pip -U -r requirements.txt
```
Feel free to move and rename the file to a PATH directory in *nix operating systems.
```bash
mv ./main.py ~/.local/bin/gensubs
```

# Usage
There are no options to worry about yet. 
```bash
python main.py https://www.youtube.com/watch?v=Xyu5Y293ugU
```

# TODO
* Youtube playlist support
* Windows install support
* Arbitrary/local file support
* Options for downsampling files using FFmpeg
* Language options (currently auto detects)
* Refactoring