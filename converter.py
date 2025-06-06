from glob import glob
import subprocess
import os


def convert_to_mp3(input_file):
    """Convert a given audio file to mp3 format using ffmpeg and store them inside a folder."""
    os.makedirs("mp3_files", exist_ok=True)
    # Store the file name without extension
    name = input_file.split("/")[-1].split(".")[0]
    command = [
        "ffmpeg",
        "-i",
        input_file,
        "-acodec",
        "libmp3lame",
        f"mp3_files/{name}.mp3",
    ]
    subprocess.run(command)


if __name__ == "__main__":
    # Get all .m4a, .opus files in the current directory
    files = glob("*.m4a") + glob("*.opus")

    # Convert each file to mp3
    for file in files:
        convert_to_mp3(file)

    print("Conversion completed.")
