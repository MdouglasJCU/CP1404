import os


def main():
    """Move files into folders"""
    os.chdir("FilesToSort")

    ext_to_category = {}

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        ext = filename.split('.')[-1]
        # used to testing
        # print(ext)

        if ext not in ext_to_category:
            category = input("What category would you like to sort {} files into? ".format(ext))
            ext_to_category[ext] = category
            try:
                os.mkdir(category)
            except EnvironmentError:
                pass

        os.rename(filename, "{}/{}".format(ext_to_category[ext], filename))

main()
