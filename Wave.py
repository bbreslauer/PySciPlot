from PyQt4.QtCore import SIGNAL

class Wave(list):
    def __init__(self, waveName, dataIn=[]):
        list.__init__(self)
        if self.validateWaveName(waveName):
            self.name = self.validateWaveName(waveName)
            if dataIn == []:
                self.append(0)
            else:
                self.extend(dataIn)

    def getName(self):
        return self.name

    @staticmethod
    def getNameStatic(wave):
        return wave.name

    def validateWaveName(self, waveName):
        waveName = waveName.strip()
        waveName = waveName.replace(" ","_")
        return waveName

    def rename(self, newName, mainWindow):
        tmpName = self.validateWaveName(newName)
        if mainWindow.waves.goodWaveName(tmpName):
            self.name = tmpName
            mainWindow.emit(SIGNAL("waveRenamed"))
            return True
        return False

    def convertToFloatList(self):
        floats = []
        for row in self:
            if isinstance(row, int):
                floats.append(row)
            else:
                floats.append(0)
        
        return floats
