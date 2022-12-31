#!/usr/bin/python3
import os 
import sys
import shutil 

source_path = "/home/neul/Downloads"
target_path = "/home/neul/Pictures/"
extension = input("What is the extension of file: ")

def main(source, target, ext):
    images = find_all_ext(ext, source)

    for image in images:
        move_files(image, target)


def find_all_ext(ext, source):
    images = []
    for root, dirs, files, in os.walk(source):
        for name in files:
            if ext in name:
                path = os.path.join(root, name)
                images.append(path)
        break
    return images


def move_files(source, target):
    shutil.move(source, target)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        main(source_path, target_path, extension)
    else:
        source, target = args[1:]
        main(source, target, extension)
