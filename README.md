### Cuzilloader
Simple script to download videos in mp4/mp3 using ytdlp.

## Example usage

Download video in 480p or worse: <br />
cuzilloader {url}

Download video in the highest possible quality: <br />
cuzilloader -q best {url}

Download audio: <br />
cuzilloader -f mp3 {url}

Note: <br />
To download a video as a audio file you need ffmpeg, you can get it here https://github.com/FFmpeg/FFmpeg

There's also scripts that downloads and sets up ffmpeg:

for Windows: https://github.com/Crozzers/ffmpeg-installer # Tested <br />
for Linux: https://gist.github.com/maxwelleite/bcb4604ef827742b9a38cced04018aff # Old script, didnt tested
