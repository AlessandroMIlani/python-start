# move downloaded files to a specified directory


import os
import watchdog

down_folder = "/home/ale/Scaricati"
img_folder = "/home/ale/Immagini"
vid_folder = "/home/ale/Video"
music_folder = "/home/ale/Musica"

#scan for files in download folder
with os.scandir(down_folder) as entries:
    for i in entries:
        print(i.name)



