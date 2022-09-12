
## Replaces spaces in file names with underscores
## Targets single file or contents of entire folder

import sys, os


def main(flag, Path):

    if flag == "-multi":
        files = os.listdir(Path)
        
        for file in files:
            os.rename(file, file.replace(" ", "_"))

    if flag == "-single":
        os.rename(file, file.replace(" ", "_"))


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("No path to folder given. Use '-usage' for help.")

    elif sys.argv[1].lower() == "-usage":
        print("$ filename_RSwU.py   -multi    <path to folder, replace spaces with underscore in all file names within folder")
        print("$ filename_RSwU.py   -single   <path to file, replace spaces with underscore in single file.")
        print("Path example, e.g. \"C:\Users\<username>\Desktop\<infolder>\"")

    else:
        main(sys.argv[1], sys.argv[2])
