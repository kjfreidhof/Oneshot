#!/usr/bin/env python

# Import python modules 
# Importing OS and subprocess 

import os 
import subprocess 

# a varriable for the 3 option if selected 
p = "Enter a number"

# First field of input select an option n,l, or f. 
i = input("Select a option n,l,f,p: ")
# Second field of input enter in the url of the video/audio file 
# you want to download 
url = input("Enter the URL of the video: ")

# If there is an error print this varriable 
e = "An error occured: {e}"

# If there it is successfull print this varriable 
s = "Download successful!"

# Use yt-dlp to download the video

# if input n is selected then run normal yt-dlp command 
if i == "n":
    # This will try to download it 
    try:
        subprocess.run(["yt-dlp", url])
 # if something goes wrong it will give an error 
    except Exception as e:
        print(f"An error occurred: {e}")

# if input l is selected then run then list the format options of the url

elif i == "l":
    try:
        subprocess.run(["yt-dlp", "-F", url])
        print(s)

    except Exception as e:
        print(e)


# if input selected f then print the p varriable give use an input of a 
# number to enter in 
# Then download the video or audio file based on the input 
elif i == "f":
    print(p)
    inp = input()
    try:
        subprocess.run(["yt-dlp", "-f", inp, url])
        print(s)

    except Exception as e:
        print(e)

elif i == "p":
    try: 
        subprocess.run(["yt-dlp", "-o", '%(playlist_title)s/%(title)s.%(ext)s', "-i", "--yes-playlist", url ])

    except Exception as e:
        print(e)


