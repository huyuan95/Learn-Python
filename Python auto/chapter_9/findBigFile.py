import shutil, os


def findBigFile(folder):
    folder = os.path.abspath(folder)

    for foldername, subfolderNames, filenames in os.walk(folder):
        for filename in filenames:
            filesize = os.path.getsize(os.path.join(foldername, filename))
            if filename[0] != '.' and filesize > 100000000:
                print(os.path.join(foldername, filename), filesize)


if __name__ == '__main__':
    findBigFile('/Users')
