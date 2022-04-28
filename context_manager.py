from contextlib import contextmanager
import os

"""cwd = os.getcwd()
os.chdir('Sample-Dir_Two')
print(os.listdir)
os.chdir(cwd)"""

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())