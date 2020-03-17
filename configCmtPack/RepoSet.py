import os
import ConfigParser
class MyConfigParser(ConfigParser.ConfigParser):
    """set ConfigParser options for case sensitive."""
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=defaults)
    def optionxform(self, optionstr):
        return optionstr

default = {
    "BeamInfoSvc": "https://github.com/xxmawhu/BeamInfoSvc.git",
    "BesStdSelector": "https://github.com/xxmawhu/BesStdSelector.git",
    "BesStdSelector": "https://github.com/xxmawhu/BestCandidateSE.git",
    "HadronInfo": "https://github.com/xxmawhu/HadronInfo.git",
    "MCTruthInfo": "https://github.com/xxmawhu/MCTruthInfo.git",
    "MCTruthMatchSvc": "https://github.com/xxmawhu/MCTruthMatchSvc.git",
    "McDecayModeSvc": "https://github.com/xxmawhu/McDecayModeSvc.git",
    "PhotonConverSvc": "https://github.com/xxmawhu/PhotonConverSvc.git",
    "TupleSvc": "https://github.com/xxmawhu/TupleSvc.git",
    "DCListSvc": "https://github.com/xxmawhu/DCListSvc.git",
}

def initConfig(repoSet):
    local_config = MyConfigParser()
    local_config.add_section('Repository')
    for k in repoSet:
        local_config.set('Repository', k, repoSet[k])
    if not os.path.exists(os.path.expanduser("~/.configCmtPack")):
        os.mkdir(os.path.expanduser("~/.configCmtPack"))
    localFile = os.path.expanduser("~/.configCmtPack/repo")
    with open(localFile, 'w') as configFile:
        local_config.write(configFile)

def init(configfile):
    if not os.path.exists(configfile):
        initConfig(default)

def ReadConfig(configfile):
    init(configfile)
    local_config = MyConfigParser()
    local_config.read(configfile)
    d = {}
    for item in local_config.items("Repository"):
        d[item[0]] = item[1]
    return d

localConfigFile = os.path.expanduser("~/.configCmtPack/repo")
remote = ReadConfig(localConfigFile)

if __name__ == "__main__":
    for i in remote:
        print("{} --> {}".format(i, remote[i]))
