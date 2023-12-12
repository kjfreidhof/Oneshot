# Importing Python modules 
import os
import subprocess

# A function for converting wma into mp3 give the input path and output path
def convert_wma_to_mp3(input_file, output_file):
    
# The ffmpeg command 
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]

# going to try to run the command to convert the file 
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Converted Successfully")

# otherwise if not then error 
    except subprocess.CalledProcessError as e:
        print("Not converted Successfully")

# Giving The input and output directory. 
input_dir = input("Enter the input directory path: ")
output_dir = input("Enter the output directory path: ")

# Then convert the file or files 
for filename in os.listdir(input_dir):
    if filename.endswith(".wma"):
