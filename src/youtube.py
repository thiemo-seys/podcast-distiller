from pytube import YouTube


def download_audio(url: str, output_path: str) -> str:
    """Returns the path to the downloaded audio file"""
    yt = YouTube(url)
    return yt.streams.filter(only_audio=True).first().download(output_path=output_path)
