from PyQt4.QtCore import QObject, SIGNAL
from Wave import Wave

class Waves(list):
    def __init__(self, wavesIn=[], mainWindow=QObject(), keepWavesUnique=True):
        list.__init__(self)
        self.mainWindow = mainWindow
        self.keepWavesUnique = keepWavesUnique
        for wave in wavesIn:
            self.append(wave)

    # returns values:
    # True  = successful
    # False = value already exists
    def append(self, wave):
        if self.keepWavesUnique:
           if self.goodWaveName(wave.getName()):
                return self.addWave(wave)
        else:
            return self.addWave(wave)
        return False
    
    def addWave(self,  wave):
        list.append(self, wave)
        self.mainWindow.emit(SIGNAL("waveAdded"), wave)
        return True

    # returns True if wave is removed, False if wave is not removed
    def removeWave(self, wave):
        for index in range(len(self)):
            if self[index].getName() == wave.getName():
                self.pop(index)
                self.mainWindow.emit(SIGNAL("waveRemoved"), wave)
                return True
        return False

    # returns wave if found, and False if not found
    def getWaveByName(self, name):
        for wave in self:
            if name == wave.getName():
                return wave
        return False

    # returns True if waveName is a good name, and False if it is a bad name
    def goodWaveName(self, waveName):
        if (waveName == ""):
            return False
        for w in self:
            if waveName == w.getName():
                return False
        return True

    def findGoodWaveName(self):
        numWaves = len(self)
        baseName = "Wave"
        allWaveNames = map(Wave.getNameStatic, self)
        while True:
            if (baseName + str(numWaves)) not in allWaveNames:
                return baseName + str(numWaves)
            else:
                numWaves += 1
