from moviepy.editor import AudioFileClip
import glob
import os

def cut_audio_into_parts(input_audio_file, num_parts):
    try:
        audio_clip = AudioFileClip(input_audio_file)

        part_duration = audio_clip.duration / num_parts

        output_directory = f"./output_samples/"
        os.makedirs(output_directory, exist_ok=True)

        for i in range(num_parts):
            start_time = i * part_duration
            end_time = (i + 1) * part_duration
            output_part_file = os.path.join(output_directory, f"part_{i + 1}.mp3")
            audio_segment = audio_clip.subclip(start_time, end_time)
            audio_segment.write_audiofile(output_part_file)

        audio_clip.close()
        print(f"Audio split into {num_parts} parts successfully.")
    except Exception as e:
        print(f"Error cutting audio: {str(e)}")

audio_directory = "./output/"
num_parts = 10

audio_files = glob.glob(os.path.join(audio_directory, "*.mp3"))

if audio_files:
    input_audio_file = audio_files[0]
    cut_audio_into_parts(input_audio_file, num_parts)
else:
    print("No audio files found in the directory.")
