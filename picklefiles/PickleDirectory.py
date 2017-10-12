import os

class PickleDirectory(object):


    def getPickleFile(self, RelativePath):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, RelativePath)
        return filename



