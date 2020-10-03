import time
from builtins import KeyboardInterrupt

from watchdog.observers import Observer
from handler import Handler

if __name__ == "__main__":
    path = "C://Users/Brady.DESKTOP-TDBOV83/Downloads/"
    observer = Observer()
    handler = Handler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()