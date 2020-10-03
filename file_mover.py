from builtins import FileNotFoundError, FileExistsError
import os


# This file will check to see if there are any files in the downloads folder.
# It will check various file types and then move them to the corresponding folders
class FileMover:

    def __init__(self):

        # Defining the locations to move files to and the path to watch
        self.downloads_folder_location = "C://Users/Brady.DESKTOP-TDBOV83/Downloads/"
        self.pictures_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Pictures/")
        self.documents_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Documents/")
        self.exectuable_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Downloads/Executables/")
        self.zip_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Downloads/Zips/")
        self.video_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Videos/")
        self.sounds_location = os.path.join("C://Users/Brady.DESKTOP-TDBOV83/Music/")

        # Defining file extensions
        self.picture_extensions = [".png", ".jpg", ".jpeg"]
        self.exe_extensions = [".exe", ".msi", ".tar.gz"]
        self.document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx"]
        self.zip_extension = [".zip"]
        self.video_extension = [".mp4"]
        self.sound_extension = [".wav", ".mp3"]

    def determine_file_type(self, ext_split):
        if ext_split in self.picture_extensions:
            return self.pictures_location
        elif ext_split in self.document_extensions:
            return self.documents_location
        elif ext_split in self.zip_extension:
            return self.zip_location
        elif ext_split in self.exe_extensions:
            return self.exectuable_location
        elif ext_split in self.video_extension:
            return self.video_location
        elif ext_split in self.sound_extension:
            return self.sounds_location
        else:
            return self.downloads_folder_location

    def doFileMovement(self):
        for f in os.listdir(self.downloads_folder_location):
            file = os.path.join(self.downloads_folder_location, f)
            if os.path.isfile(file):
                filename, file_extension = os.path.splitext(file)
                new_file_location = self.determine_file_type(file_extension)
                try:
                    if new_file_location != self.downloads_folder_location:
                        os.rename(file, os.path.join(new_file_location, f))
                        print("Moved file: " + f + " to " + new_file_location)
                except FileNotFoundError:
                    print("File Not Found error")
                except FileExistsError:
                    print("The file already exists in the new location")
                    print("Deleting file:" + filename + file_extension)
                    os.remove(file)
