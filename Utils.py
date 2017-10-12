import os

class Utils(object):

    def __init__(self):
        pass

    def getPathToFile(self,RelativePath):
        dirr = os.getcwd()
        ROOT_DIR = os.path.abspath(dirr)
        folder = os.path.join(ROOT_DIR, RelativePath)
        return folder