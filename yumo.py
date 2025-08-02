import sys, subprocess
from services import yumoback
from pathlib import Path


class Start:
    STDOUT = Path("")
    def __init__(self):
        subprocess.Popen("npm run dev", shell=True, cwd= Path(__file__).parent / Path("services", "yumoviews"))
        yumoback.startasgi()

if __name__ == '__main__':
    Start()
