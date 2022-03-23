#import libraries
import os
from pathlib import Path
#Dictionary (Add more if you want)
DIRECTORIES = {
    "IMAGENS": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png"],
    
    "PHOTOSHOP": [".psd"],

    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".mpeg", ".3gp"],
    
    "WORD": [".docx", ".doc"],
    
    "PDF": [".pdf"],
    
    "ARQUIVOS": [".iso", ".rar", ".zip"],
    
    "AUDIO": [".aac", ".aa", ".aac", ".m4a", ".mp3", ".wav", ".wma"],
    
    "TEXTO": [".txt", ".in", ".out"],
    
    "PDF": [".pdf"],
    
    "JAVA": [".java", ".class"],
    
    "PYTHON": [".py"],
    
    "EXE": [".exe"],
    
    "WEB": [".html", ".js", ".css", ".xml"]
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
#This will organise your files
def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
   #if extension not present in the dctionary than create a folder name "OTHER"
    try:
        os.mkdir("OTHER")
    except:
        pass
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER/' + str(Path(dir)))
        except:
            pass
if __name__ == "__main__":
    organize()