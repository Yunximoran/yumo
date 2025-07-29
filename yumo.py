import sys, subprocess
from services import yumoback
from pathlib import Path


class Start:
    def __init__(self):
        subprocess.Popen("npm run dev", shell=True, cwd= Path(__file__).parent / Path("services", "yumovue"))
        yumoback.startasgi()

if __name__ == '__main__':
    Start()