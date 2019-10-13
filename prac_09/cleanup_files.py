import os

def main():
    """Make all filenames consistent"""
    # set correct directory
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        # Test current name of files
         print("Directory:", directory_name)
         print("\tcontains subdirectories:", subdirectories)
         print("\tand files:", filenames)
         print("(Current working directory is: {})".format(os.getcwd()))

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

main()