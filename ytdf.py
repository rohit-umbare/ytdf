#!/usr/bin/env python3

import os
import sys
import subprocess

def download_video_audio(url):
    video_output = os.path.expanduser("~/Videos/%(title)s.%(ext)s")
    audio_output = os.path.expanduser("~/Videos/%(title)s_audio.%(ext)s")

    # Download the video
    video_command = [
        'yt-dlp',
        '-f', 'bv+ba/b',
        '--merge-output-format', 'mp4',
        '-o', video_output,
        url
    ]
    
    # Download video and audio
    subprocess.run(video_command, check=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: ytfd <YouTube URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Download video and audio
    download_video_audio(url)

if __name__ == "__main__":
    main()
