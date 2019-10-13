import os


def main():
    """Move files into folders"""
    os.chdir("FilesToSort")

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        
        ext = filename.split('.')[-1]
        # used to testing
        #print(ext)



main()