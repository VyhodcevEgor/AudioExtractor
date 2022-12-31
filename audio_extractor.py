import moviepy.editor
from pathlib import Path


if __name__ == '__main__':
    video_path = Path('')  # Path here

    video = moviepy.editor.VideoFileClip(f'{video_path}')
    audio = video.audio
    audio.write_audiofile(f'{video_path.stem}.mp3')
