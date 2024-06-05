import argparse
from yt_dlp import YoutubeDL
from platform import system

def download_file(url: str, ext: str, home: str) -> None:
    if ext == "mp4":
        ydl_opts= {
            "format": f"{ext}",
            "outtmpl": f"{home}%(id)s.%(ext)s",
        }
    else:
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": 'FFmpegExtractAudio',
                "preferredcodec": f"{ext}",
                "preferredquality": "192",
            }],
            "outtmpl": f"{home}%(id)s.%(ext)s",
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    try:
        parser.add_argument("url", type=str)
        parser.add_argument("-f", "--format", type=str, nargs="?", default="mp4")
    except argparse.ArgumentError as e:
        print(e)

    return parser.parse_args()

def set_home(system: str) -> str:
    import os
    from pathlib import Path

    if system == "Windows":
        try:
            os.chdir(f"{Path.home()}\\Videos\\Cuzilloader\\")
            return f"{Path.home()}\\Videos\\Cuzilloader\\"
        except:
            os.makedirs(f"{Path.home()}\\Videos\\Cuzilloader\\")
            return f"{Path.home()}\\Videos\\Cuzilloader\\"
    
    try:
        os.chdir(f"{Path.home()}/Videos/Cuzilloader/")
        return f"{Path.home()}/Videos/Cuzilloader/"
    except:
        os.makedirs(f"{Path.home()}/Videos/Cuzilloader/")
        return f"{Path.home()}/Videos/Cuzilloader/"

def main():
    home = set_home(system())
    args = argparser()
    download_file(args.url, args.format, home)

if __name__ == "__main__":
    main()