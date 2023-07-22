import os
import glob
from moviepy.editor import VideoFileClip

def extract_audio_from_mp4(mp4_file, output_audio_file):
    try:
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio_file)
        audio_clip.close()
        video_clip.close()
        print(f"Audio extracted from {mp4_file} successfully.")
    except Exception as e:
        print(f"Error extracting audio from {mp4_file}: {str(e)}")

input_directory = "./input/"
output_directory = "./output/"

os.makedirs(output_directory, exist_ok=True)

mp4_files = glob.glob(os.path.join(input_directory, "*.mp4"))

for mp4_file in mp4_files:
    mp4_filename = os.path.basename(mp4_file)
    output_filename = os.path.join(output_directory, f"{mp4_filename[:-4]}_output.mp3")
    extract_audio_from_mp4(mp4_file, output_filename)
