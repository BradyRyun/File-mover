from builtins import staticmethod
from file_mover import FileMover

from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        file_mover = FileMover()
        if event.is_directory:
            return None
        else:
            # Event is created, you can process it now
            file_mover.doFileMovement()
