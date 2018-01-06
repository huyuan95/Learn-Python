import zipfile, os

def backuptoZip(folder):
    
    folder = os.path.abspath(folder)
    
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    print('Creating %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    for foldername, subfoldernames, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startwith(newBase) and filename.endwith('.zip'):
            continue
        backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
    
    print('done')

if __name__ == '__main__':
    backuptoZip('C:\\delicious')
