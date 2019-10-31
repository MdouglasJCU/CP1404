import os


def main():
    """Move files into folders"""
    os.chdir("FilesToSort")

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        ext = filename.split('.')[-1]
        # used to testing
        # print(ext)

        # if folder doesn't exist for ext name, create folder
        try:
            os.mkdir(ext)
        except EnvironmentError:
            pass

        print("{}/{}".format(ext, filename))
        os.rename(filename, "{}/{}".format(ext, filename))



main()