from pytube import YouTube


def download_audio(url: str, output_path: str) -> str:
    """Returns the path to the downloaded audio file"""
    yt = YouTube(url)
    return yt.streams.get_audio_only().download(output_path=output_path)
