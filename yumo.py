import os, sys
from services import startup
from lib.sys.processing import Process



class Start:
    services = [
        startup.Django
    ]

    services_runing = []
    def __init__(self):
        for service in self.services:
            Process(target=service).start()

if __name__ == "__main__":
    Start()