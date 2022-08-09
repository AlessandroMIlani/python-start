# move downloaded files to a specified directory


import os
import subprocess
import sys
import sys
import logging
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

down_folder = "/home/ale/Scaricati"
img_folder = "/home/ale/Immagini"
vid_folder = "/home/ale/Video"
music_folder = "/home/ale/Musica"
doc_folder = "/home/ale/Documenti"


def move(entries):
    for entry in entries:
        if entry.is_file():
            if entry.name.endswith(".jpg") or entry.name.endswith(".png"):
                subprocess.call(["mv", entry.path, img_folder])
            elif entry.name.endswith(".mp4") or entry.name.endswith(".mkv"):
                subprocess.call(["mv", entry.path, vid_folder])
            elif entry.name.endswith(".mp3") or entry.name.endswith(".wav"):
                subprocess.call(["mv", entry.path, music_folder])     
            elif entry.name.endswith(".pdf") or entry.name.endswith(".docx"):
                subprocess.call(["mv", entry.path, doc_folder])        
        elif entry.is_dir():
            with os.scandir(down_folder + "/" + entry.name) as entries2:
                move(entries2)

#scan for files in download folder
def scan():
    while True:
        with os.scandir(down_folder) as entries:
            move(entries)

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            # Take any action here when a file is first created.
            scan()


def monitor():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    path = down_folder
    e_handler = Handler()
    watch = Observer()
    watch.schedule(e_handler, path, recursive=True)
    watch.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
            watch.stop()
    watch.join()
monitor()


#main
if __name__ == "__main__":
    #firt full scan
    scan()

    # monitoring changes in download folder
    monitor()
