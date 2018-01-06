import shutil, os

def selectCopy(folder, destFolder, ext):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    
    for foldername, subfolderNames, filenames in os.walk(folder):
        print('Copying files in %s...' % (foldername))
        for filename in filenames:
            print(filename)
            if filename.endswith(('.' + ext)):
                shutil.copy(os.path.join(foldername, filename), os.path.join(
                        destFolder, filename))
                
if __name__ == '__main__':
    selectCopy('../../', '../../copy', 'py')
            
