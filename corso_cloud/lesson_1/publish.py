import shutil
import glob
import os.path


if __name__ == '__main__':
    for fname in glob.glob('dist/*'):
        shutil.copy(fname, os.path.expanduser('~/Dropbox/'))
