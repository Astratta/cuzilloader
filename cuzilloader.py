import argparse
from yt_dlp import YoutubeDL
from platform import system
from urllib.parse import urlparse

def download_file(url: str, ext: str, home: str, quality: str) -> None:
    if ext == "mp4":
        def extract_domain(url: str) -> str:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            if domain.startswith("www."):
                domain = domain[4:]
            if domain.endswith(".com"):
                domain = domain[:-4]
            return domain
        
        if quality == "worst":
            ydl_opts= {
                "format": "bv*[height<=480][ext=mp4]+ba[ext=m4a]/b[height<=480][ext=mp4] / wv*+ba/w",
                "outtmpl": f"{home}%(id)s.%(ext)s",
                "extractor": "twitter" if extract_domain(url) == "x" else extract_domain(url),
            }
        else:
            ydl_opts= {
                "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b",
                "outtmpl": f"{home}%(id)s.%(ext)s",
                "extractor": "twitter" if extract_domain(url) == "x" else extract_domain(url),
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
        parser.add_argument("-q", "--quality", type=str, nargs="?", default="worst")
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
    download_file(args.url, args.format, home, args.quality)

if __name__ == "__main__":
    main()