import os

def find(path, filename):
    if os.path.isdir(path):
        for name in os.listdir(path):
            if filename in name:
                print(os.path.join(path, name))
            childpath = os.path.join(path, name)
            find(childpath, filename)

if __name__ == '__main__':
    find('/Users/dreamyang', 'python')
