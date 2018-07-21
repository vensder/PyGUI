#!/usr/bin/env python3

from os import path
import subprocess

CURRENT_FOLDER = path.dirname(path.abspath(__file__))
sound_file = path.join(CURRENT_FOLDER, 'bell.wav')

def bell():
    subprocess.Popen(["aplay", sound_file])


if __name__ == "__main__":
    bell()

