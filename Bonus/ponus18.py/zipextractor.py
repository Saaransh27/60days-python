import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)
        
if __name__ == "__main__":
    extract_archive("Bonus\ponus18.py\compressed.zip", 
                    "D:\60days pyhton\Bonus\ponus18.py")
